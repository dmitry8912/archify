from slack_webhook import Slack
from config import Config
import datetime


class Notifier:
    @staticmethod
    def notify(message):
        now = datetime.datetime.now()
        config = Config.get()
        slack = Slack(url=config['slack']['webhook'])
        slack.post(attachments=[{
                        "author_name": config['slack']['author_name'],
                        "title": f"Archify feedback {now}",
                        "text": message,
                   }])