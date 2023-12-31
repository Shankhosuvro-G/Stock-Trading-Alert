import requests
from twilio.rest import Client
STOCK_NAME = "TCS"
COMPANY_NAME = "TATA CONSULTANCY S"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY="2COZNLIA16M387KU"
NEWS_API="989533d3fbd94f4ba2b9f183faf34c8a"
TWILIO_SID="AC7c5f427ad7b452408ee8628fd5273f6c"
TWILIO_AUTH_TOKEN="1632778e8de3684d82a7a362f8c4389c"
   
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY ,                                                                                                                                                                                                                                                                        
}
response=requests.get(STOCK_ENDPOINT,stock_params)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference=float(yesterday_closing_price)-float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"


diff_percent=(difference/float(yesterday_closing_price))*100
rounded_number=round(diff_percent,2)
print(rounded_number)

if diff_percent>0.1:
    news_params={
        "apiKey":NEWS_API,
        "q":COMPANY_NAME,
    }
    news_response=requests.get(NEWS_ENDPOINT,news_params)
    articles=news_response.json()["articles"]
    three_articles=articles[:3]
    print(three_articles)
    formatted_articles = [f"{STOCK_NAME}: {up_down} {rounded_number}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    client=Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message=client.messages.create(
            body=article,
            from_=+12059274647,
            to=+919831976758


        )




