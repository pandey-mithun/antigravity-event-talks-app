from flask import Flask, jsonify, render_template, request
import feedparser
from bs4 import BeautifulSoup
import time
import requests

app = Flask(__name__)

# Cache structure to avoid hammering the Google feed API
cache = {
    "data": None,
    "last_fetched": 0
}
CACHE_DURATION_SECS = 600  # 10 minutes
FEED_URL = "https://docs.cloud.google.com/feeds/bigquery-release-notes.xml"

def fetch_and_parse_feed():
    try:
        # Fetch raw data using requests to ensure proper headers/timeouts
        response = requests.get(FEED_URL, timeout=10)
        response.raise_for_status()
        
        # Parse with feedparser
        feed = feedparser.parse(response.content)
        updates = []
        
        for entry in feed.entries:
            date_str = entry.get('title', 'Unknown Date')
            updated_raw = entry.get('updated', entry.get('published', ''))
            link = entry.get('link', 'https://cloud.google.com/bigquery/docs/release-notes')
            
            # Use BeautifulSoup to parse HTML summary
            summary_html = entry.get('summary', '')
            soup = BeautifulSoup(summary_html, 'html.parser')
            
            current_type = None
            current_content = []
            
            # Split by h3 header tags to extract individual updates
            for child in soup.contents:
                if child.name == 'h3':
                    if current_type and current_content:
                        html_text = "".join(str(c) for c in current_content)
                        # We use separator=' ' to avoid joined words
                        plain_text = BeautifulSoup(html_text, 'html.parser').get_text(separator=' ', strip=True)
                        updates.append({
                            'date': date_str,
                            'updated_raw': updated_raw,
                            'type': current_type,
                            'html': html_text.strip(),
                            'text': plain_text,
                            'link': link
                        })
                    current_type = child.get_text(strip=True)
                    current_content = []
                else:
                    current_content.append(child)
                    
            # Add the trailing update
            if current_type and current_content:
                html_text = "".join(str(c) for c in current_content)
                plain_text = BeautifulSoup(html_text, 'html.parser').get_text(separator=' ', strip=True)
                updates.append({
                    'date': date_str,
                    'updated_raw': updated_raw,
                    'type': current_type,
                    'html': html_text.strip(),
                    'text': plain_text,
                    'link': link
                })
                
        return updates, None
    except Exception as e:
        return None, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/release-notes')
def get_release_notes():
    force_refresh = request.args.get('refresh', 'false').lower() == 'true'
    now = time.time()
    
    if force_refresh or not cache["data"] or (now - cache["last_fetched"] > CACHE_DURATION_SECS):
        data, error = fetch_and_parse_feed()
        if error:
            # If fetch fails but we have cached data, fall back to it
            if cache["data"]:
                return jsonify({
                    "success": True,
                    "updates": cache["data"],
                    "cached_at": cache["last_fetched"],
                    "warning": f"Failed to refresh feed ({error}). Using cached data."
                })
            return jsonify({"success": False, "error": error}), 500
        
        cache["data"] = data
        cache["last_fetched"] = now
        
    return jsonify({
        "success": True,
        "updates": cache["data"],
        "cached_at": cache["last_fetched"]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
