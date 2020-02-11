import json


class Config:
    @staticmethod
    def get():
        with open('config.json') as conf:
            result = json.load(conf)
        return result
