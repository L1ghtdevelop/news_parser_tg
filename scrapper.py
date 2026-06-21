import requests

from bs4 import BeautifulSoup
from typing import List, Dict
from datetime import datetime

class NewsScraper:

    def __init__(self, url: str) -> None:
        self.url = url
        self.headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    
    def fetch_news(self) -> List[Dict[str, str]]:
        try:
            response = requests.get(self.url, self.headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "lxml")
            # TODO: Parser
            article = []
            # TODO: parsed info to list
            return article
        except requests.exceptions.ConnectTimeout:
            print("Время ожидания превышено.")
            return []
        except requests.exceptions.RequestException:
            print("Ошибка при получении страницы сайта.")
            return []
        except Exception as e:
            print("Возникла непредвиденная ошибка.")
            return []
