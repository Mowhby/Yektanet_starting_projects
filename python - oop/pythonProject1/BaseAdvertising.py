class BaseAdvertising:
    def __init__(self):
        self.views_count = 0
        self.clicks_count = 0

    @staticmethod
    def describeMe() -> str:
        print(
            'This is \'Base Advertising\'. Other classes use my fields(views_count & clicks_count) and methods. Classes use functions for getting and increamenting fields in this class. This class make this code cleaner!')

    def getClicks(self) -> int:
        return self.clicks_count

    def getViews(self) -> int:
        return self.views_count

    def incViews(self):
        self.views_count += 1

    def incClicks(self):
        self.clicks_count += 1
