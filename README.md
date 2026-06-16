# BigQuery Release Notes Hub

A clean, modern, dark-themed Single Page Web Application built using Python Flask, vanilla HTML5, CSS3, and JavaScript. It aggregates the official BigQuery Release Notes RSS feed, parses items granularly by category, and allows developers to easily customize and post updates to X (Twitter).

---

## ✨ Features

- **Granular Parsing**: Splitting compound daily notes into standalone cards categorized as **Feature**, **Change**, **Issue**, or **Deprecation**.
- **Real-Time Client Filter & Search**: Search keywords or filter by release categories instantly with count tracking badges.
- **Tweet Composer Drawer**: Custom slide-out panel that pre-fills a concise update text with links and popular developer hashtags. Includes character counting up to the 280-character limit.
- **Smart Memory Caching**: Implements a 10-minute server cache to protect against rate limits and ensure low-latency loads, with error fallback and manual force-refresh options.
- **Premium Aesthetics**: Glassmorphism dashboard aesthetics, customized scrollbars, tag indicator colors, and micro-interactive animations.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Flask, `feedparser` (RSS/Atom Parsing), `beautifulsoup4` (HTML traversal).
- **Frontend**: Vanilla HTML5, CSS3, JavaScript (no external framework required).
- **Icons**: FontAwesome 6 (loaded via CDN).
- **Fonts**: Google Fonts (Outfit, Plus Jakarta Sans).

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher installed on your local system.
- Git (optional, for version control).

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pandey-mithun/antigravity-event-talks-app.git
   cd antigravity-event-talks-app
   ```

2. **Set up a Virtual Environment**:
   - **Windows**:
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Running the Application

Start the Flask development server:
```bash
python app.py
```

Open your browser and navigate to:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📂 Project Structure

```
.
├── static/
│   └── style.css            # Stylesheet with layout grid, variables & dark theme
├── templates/
│   └── index.html           # Frontend SPA controller and HTML structure
├── app.py                   # Flask server, route controller & XML parser
├── requirements.txt         # Project requirements listing python libraries
├── .gitignore               # System, editor, and venv ignores
└── README.md                # Project documentation
```
