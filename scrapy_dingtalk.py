import requests
import random


class ScrapyDingTalk:
    def __init__(self, cookie):
        self.cookie = str(cookie)
        self.url = "https://docs.dingtalk.com/i/nodes/KOEmgBoGwD78vlMygqw7VndLerP9b30a"

    def askURL(self):
        head = {
            "Accept": """text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9""",
            "Cookie": self.cookie,
            "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"""
        }
        print(head.get("Cookie"))
        try:
            request = requests.get(self.url, headers=head)
            html = request.content.decode("utf-8")
        except:
            html = ""
        print(html)
