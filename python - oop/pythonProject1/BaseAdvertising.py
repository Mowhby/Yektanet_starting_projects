class BaseAdvertising:
    def __init__(self):
        self.views_count = 0
        self.clicks_count = 0

    @staticmethod
    def describeMe() -> str:
        print('This is the base class! other classes will use my fields and methods. I can make this code cleaner!')

    def getClicks(self) -> int:
        return self.clicks_count

    def getViews(self) -> int:
        return self.views_count

    def incViews(self):
        self.views_count += 1

    def incClicks(self):
        self.clicks_count += 1
