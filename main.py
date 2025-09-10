from fetch_news import get_news
from send_email import send_email

def run_agent():
    # Step 1: Fetch news
    news_list = get_news()

    # Step 2: Send email
    send_email(news_list)

if __name__ == "__main__":
    run_agent()
