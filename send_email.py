import yagmail
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

def send_email(news_list):
    """
    Send an email containing the list of news.
    news_list: list of dicts with 'title' and 'link'
    """
    yag = yagmail.SMTP(EMAIL_SENDER, EMAIL_PASSWORD)

    # Create email body
    body = ""
    for i, news in enumerate(news_list, 1):
        body += f"{i}. {news['title']} -> {news['link']}\n"

    # Send email
    yag.send(
        to=EMAIL_RECEIVER,
        subject="🚀 Daily Cyber/AI/IT News Digest",
        contents=body
    )
    print("Email sent successfully!")
