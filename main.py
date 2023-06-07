import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_ADVANTAGE_API_KEY = "90JOVLHP8JT5Y79M"
NEWS_API_KEY = "851c6534ec874cf39cf5b19c2025da4a"


# get the stock prices
response = requests.get(
    f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={ALPHA_ADVANTAGE_API_KEY}')

stock_time_series =  response.json()["Time Series (Daily)"]
stock_time_series = list(stock_time_series.items())[0:2]

stock_closing_price = float(stock_time_series[0][1]["4. close"])
stock_opening_price = float(stock_time_series[1][1]["1. open"])

stock_price_difference = round(stock_opening_price - stock_closing_price , 2)

percentage = round( ( stock_price_difference / stock_closing_price ) * 100, 2)
print(stock_closing_price, stock_opening_price,stock_price_difference, percentage)


# Get the news
response = requests.get(f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&sortBy=popularity&apiKey={NEWS_API_KEY}')
news = response.json()["articles"][0:3]



message = f"""
TSLA: { "🔺"if percentage > 0 else "🔻" } {percentage}%
Headline_1: {news[0]["title"]}
Headline_2: {news[1]["title"]}
Headline_3: {news[2]["title"]}
"""

print(message)


# we are supposed to send message when its higher or lower than 5%

if percentage > 4.9 or percentage < - 4.9:
    pass
else :
    pass

# send SMS

account_sid = 'ACace2eee01e00fc26e23784b5b5da8773'
auth_token = '5e1b1b38af2fb17cbb9e642ea0c6e686'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+13613143843',
    body=f'{message}',
    to='+923428239578'
)

print(message.sid)

# Optional: Format the SMS message like this:

