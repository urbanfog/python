from twilioSMS import TwilioSMS
from stocks import StockGetter
from news import NewsGetter

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
LIMIT = 1

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
tsla = StockGetter(ticker=STOCK)
tsla.get_stock_price()


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
tsla_news = NewsGetter(name=COMPANY_NAME)
articles = tsla_news.top_news()

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
# twilio = TwilioSMS()
twilio = TwilioSMS()
change = tsla.price_change()

if change > LIMIT or change < -LIMIT:
    for article in articles:
        twilio.send_sms(f"{STOCK} {int(change)}%\n{article}")
else:
    twilio.send_sms(f"{STOCK}: No significant news to report.")


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
