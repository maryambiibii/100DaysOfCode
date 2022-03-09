import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = your_key_from_newspai

# Twilio
account_sid = your_sid
auth_token = your_token_number

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=60min&apikey=yourapikey'
r = requests.get(url)
data = r.json()
hour_stocks = data["Time Series (60min)"]

yesterday_closing = list(hour_stocks.values())[0]["4. close"]
print(yesterday_closing)

previous_day_closing = list(hour_stocks.values())[16]["4. close"]
print(previous_day_closing)

percentage_change = (float(yesterday_closing) - float(previous_day_closing)) / float(previous_day_closing) * 100
print(percentage_change)


if percentage_change >= 2 or percentage_change <= -2:

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    newsapi_url =  "https://newsapi.org/v2/everything?q=Tesla Inc&language=en&sortBy=relevancy&apiKey=yournewsapikey"
    r_news = requests.get(newsapi_url)
    news_data = r_news.json()
    first_three_news_articles = news_data["articles"][:3]
    for article in first_three_news_articles:
        article_title = article["title"]
        print(article_title)
        article_description = article["description"]
        print(article_description)

    ## STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
        if percentage_change > 0:
            text_format = f"TSLA: 🔺{round(percentage_change)}% \nHeadline: {article_title}. \nBrief: {article_description}"
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=text_format,
                from_=your_number_from_twilio,
                to=to_number
            )

            print(message.status)
        else:
            text_format = f"TSLA: 🔻{round(percentage_change)}% \nHeadline: {article_title}. \nBrief: {article_description}"
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=text_format,
                from_='your_number_from_twilio,
                to=to_number
            )

            print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

