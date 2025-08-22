import requests
import pyttsx3
from datetime import datetime, timedelta, timezone
import time

NEWS_API_KEY = "Your API Key"
NEWS_API_URL = "https://newsapi.org/v2/everything"
DOMAINS = "indiatimes.com,bbc.com,reuters.com,aljazeera.com,apnews.com"

NEWS_CATEGORIES = {
    'politics': 'government OR election OR parliament OR legislation OR policy OR diplomacy',
    'gaming': 'video games OR esports OR gaming industry OR game release OR Steam OR PlayStation OR Xbox',
    'entertainment': 'film OR cinema OR Hollywood OR Bollywood OR celebrity OR movie release OR entertainment industry',
    'sports': 'sports OR cricket OR football OR basketball OR Olympics OR tournament OR championship OR athletics',
    'technology': 'artificial intelligence OR tech innovation OR software OR hardware OR cybersecurity OR digital transformation',
    'business': 'economy OR stock market OR finance OR corporate OR startup OR investment OR trade',
    'science': 'research OR discovery OR space exploration OR climate science OR medical breakthrough'
}

def get_news_timeframe():
    """Get the desired timeframe for news retrieval from user"""
    while True:
        try:
            hours = int(input('\nHow far back would you like to search for news? (Enter hours, or 0 for all available): '))
            if hours >= 0:
                break
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Please enter a valid number.")
    
    ist_timezone = timezone(timedelta(hours=5, minutes=30))
    current_time = datetime.now(ist_timezone)
    
    if hours == 0:
        return current_time.isoformat(), None
    else:
        past_time = current_time - timedelta(days=int(hours)/24)
        return current_time.isoformat(), past_time.isoformat()

def select_news_category():
    """Allow user to select a news category"""
    print("\n\033[1mAvailable News Categories:\033[0m")
    for i, category in enumerate(NEWS_CATEGORIES.keys(), 1):
        print(f"{i}. {category.title()}")
    
    while True:
        try:
            choice = int(input('\nSelect a category by number: '))
            if 1 <= choice <= len(NEWS_CATEGORIES):
                selected_category = list(NEWS_CATEGORIES.keys())[choice-1]
                return selected_category
            else:
                print(f"Please enter a number between 1 and {len(NEWS_CATEGORIES)}.")
        except ValueError:
            print("Please enter a valid number.")

def retrieve_news_articles(end_time, start_time, category):
    """Fetch news articles from the API based on parameters"""
    headers = {"Authorization": NEWS_API_KEY}
    params = {
        'q': NEWS_CATEGORIES[category],
        'domains': DOMAINS,
        'to': end_time,
        'pages':50,
        'language': 'en',
        'sortBy': 'publishedAt'
    }
    
    if start_time:
        params['from'] = start_time
    
    try:
        print("Fetching the latest news...")
        response = requests.get(NEWS_API_URL, headers=headers, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving news: {e}")
        return None

def display_news_results(news_data, category, timeframe_hours):
    if not news_data or news_data.get('status') != 'ok':
        error_msg = news_data.get('message', 'Unknown error occurred') if news_data else 'No data received from server'
        print(f"Error: {error_msg}")
        return False
    
    if news_data['totalResults'] == 0:
        print("No news articles found matching your criteria.")
        print("Try expanding your timeframe or selecting a different category.")
        return False
    
    timeframe_desc = "all available news" if timeframe_hours == 0 else f"the past {timeframe_hours} hours"
    print(f"\n\033[1m📰 {category.upper()} NEWS ({timeframe_desc.title()})\033[0m")
    print("=" * 60)
    print(f"Found {news_data['totalResults']} articles. Displaying top results:\n")
    
    for index, article in enumerate(news_data['articles'], 1):
        print(f"------\033[1m{index}. {article['title']}\033[0m------")
        print(f"{article['description']}")
        if article.get('publishedAt'):
            published_time = datetime.fromisoformat(article['publishedAt'].replace('Z', '+00:00'))
            ist_time = published_time.astimezone(timezone(timedelta(hours=5, minutes=30)))
            print(f"Published: {ist_time.strftime('%b %d, %Y at %I:%M %p IST')}\n")
    return True

def narrate_news_articles(news_data):
    if not news_data or news_data.get('status') != 'ok':
        return
    
    try:
        
        
        starting_point=input('From which article no would you like the news to be narrated: ')
        print("\n\033[1mStarting news narration... Press Ctrl+C to stop at any time.\033[0m")
        for index in range(len(news_data['articles'])-int(starting_point)+1):
            index+=int(starting_point)
            article=news_data['articles'][index-1]
            narration_text = f"Article {index}. {article['title']}. "
            if article.get('description'):
                narration_text += article['description']
                
            print(f"\nNarrating article {index} of {len(news_data['articles'])}...")
            pyttsx3.speak(narration_text)

    except KeyboardInterrupt:
        print("\nNews narration stopped by user.")
    except Exception as e:
        print(f"Text-to-speech error: {e}")

def main_news_reader():
    """Main function to orchestrate the news reading application"""
    print("\n\033[1m🌐 WELCOME TO THE INTELLIGENT NEWS READER\033[0m")
    print("=" * 50)
    print("Stay informed with the latest news from trusted sources worldwide\n")
    
    selected_category = select_news_category()
    end_time, start_time = get_news_timeframe()
    timeframe_hours = 0 if start_time is None else int((datetime.fromisoformat(end_time) - datetime.fromisoformat(start_time)).total_seconds() / 3600)
    
    
    news_results = retrieve_news_articles(end_time, start_time, selected_category)
    
    
    if news_results and display_news_results(news_results, selected_category, timeframe_hours):
        
        while True:
            narration_choice = input("\nWould you like to hear the news narrated? (y/n): ").lower().strip()
            if narration_choice in ['y', 'yes']:
                narrate_news_articles(news_results)
                break
            elif narration_choice in ['n', 'no']:
                print("\nThank you for using the Intelligent News Reader. Stay informed!")
                break
            else:
                print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main_news_reader()
