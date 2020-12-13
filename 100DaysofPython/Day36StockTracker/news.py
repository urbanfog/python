from os import name
import requests


class NewsGetter:

    def __init__(self, name: str):
        self.name = name
        self.news = {}

    def get_news(self):
        params = {
            "qInTitle": self.name,
            "apiKey": ENV_VAR,
            "language": "en",
        }

        response = requests.get(
            "https://newsapi.org/v2/everything", params=params)
        response.raise_for_status()
        self.news = response.json()['articles']

    def top_news(self) -> list:
        self.get_news()
        articles = [
            f"Headline: {item['title']}\nBrief: {item['description']}\n" for item in self.news[:2]]
        return articles


# tsla = NewsGetter(name='Tesla')
# print(tsla.top_news())
