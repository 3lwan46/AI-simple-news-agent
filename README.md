# 🚀 Daily Cyber/AI/IT News Digest Agent

A simple Python-based automation agent that fetches the **latest IT, Cybersecurity, and AI news** from multiple sources and sends them to your email every morning.  

This project started from the idea:  
_"Instead of manually reading newspapers or tech sites every day, why not let an agent do it for me automatically?"_

---

## ✨ Features
- Collects top news from selected **RSS feeds** (e.g., The Hacker News, DarkReading, Wired).  
- Sends a daily digest email with **titles + URLs**.  
- Easy to extend with **AI summarization and filtering**.  
- Can be scheduled to run daily via **Task Scheduler (Windows)** or **Cron (Linux/WSL)**.  

---

## 📂 Project Structure
news_agent/
│
├─ config.py # Email & RSS feed settings
├─ fetch_news.py # Fetches top news from RSS feeds
├─ send_email.py # Sends email with the news digest
└─ main.py # Orchestrates the agent



---

## ⚙️ Installation & Setup

### 1. Clone the repo
`bash
git clone https://github.com/YOUR_USERNAME/news-agent.git
cd news-agent
pip install feedparser yagmail
EMAIL_SENDER = "your_gmail@gmail.com"
EMAIL_PASSWORD = "your_app_password"   # See Gmail setup below
EMAIL_RECEIVER = "your_email@example.com"

RSS_FEEDS = [
    "https://thehackernews.com/feeds/posts/default",
    "https://www.darkreading.com/rss_simple.asp",
    "https://www.wired.com/feed/rss"
]


smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted...')


This happens because Google blocks normal passwords for third-party apps.
To fix it, you need to use a Gmail App Password instead of your regular Gmail password.

Steps to create a Gmail App Password:

Go to Google Account → Security

Enable 2-Step Verification

Under "Signing in to Google", choose App Passwords

Select:

App: Mail

Device: Windows (or anything)

Generate → copy the 16-character password (e.g., abcd efgh ijkl mnop)

Use this password in config.py as EMAIL_PASSWORD

✅ Now your script can send emails securely.

▶️ Run the Agent
python main.py


If everything is correct, you’ll see:

Email sent successfully!

⏰ Automation (Optional)

Windows: Use Task Scheduler → Run daily at 7 AM.

Linux/WSL: Add cron job:

0 7 * * * python3 /path/to/news_agent/main.py

🔮 Future Improvements

Add AI summarization for shorter, smarter news.

Filter by keywords (e.g., "0-day", "AI model", "ransomware").

Save sent news in SQLite to avoid duplicates.

Create a simple dashboard to browse past digests.

