# 🌐 Intelligent News Reader

A Python-based **interactive news reader** that fetches the latest articles from **trusted sources** (BBC, Reuters, Al Jazeera, AP News, India Times, etc.), displays them neatly in the terminal, and optionally **narrates them using text-to-speech (TTS)**.

---

## ✨ Features
- 📰 Fetches real-time news from multiple categories:
  - Politics  
  - Gaming  
  - Entertainment  
  - Sports  
  - Technology  
  - Business  
  - Science  
- ⏳ Choose how far back in time to search (in hours, or all available news).  
- 🔊 Narrates articles using built-in text-to-speech.  
- 🌍 Retrieves content from trusted international domains.  
- 🎛️ Interactive terminal interface with easy navigation.  

---

## 🛠️ Requirements
- Python 3.8+
- Dependencies:
  ```bash
  pip install requests pyttsx3
```
🚀 Usage
``
Add your NewsAPI
NEWS_API_KEY = "your_api_key_here"


Run the script:

python news_reader.py
```

🎮 Example Workflow
```
🌐 WELCOME TO THE INTELLIGENT NEWS READER
==================================================
Stay informed with the latest news from trusted sources worldwide

Available News Categories:
1. Politics
2. Gaming
3. Entertainment
4. Sports
5. Technology
6. Business
7. Science

Select a category by number: 5

How far back would you like to search for news? (Enter hours, or 0 for all available): 24
Fetching the latest news...

📰 TECHNOLOGY NEWS (The Past 24 Hours)
==================================================
Found 35 articles. Displaying top results:

------1. AI Revolutionizes Healthcare------
AI-powered diagnostics are now being adopted globally...
Published: Aug 20, 2025 at 09:45 PM IST

🔊 Narration Feature

After fetching and displaying articles, you’ll be prompted:

Would you like to hear the news narrated? (y/n): y


The program will start reading aloud each article headline and description.

Press Ctrl+C anytime to stop narration.
```
