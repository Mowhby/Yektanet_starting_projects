from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    advertisers = []

    def __init__(self, id: int, name: str):
        super().__init__()
        self.name = name
        self.id = id
        Advertiser.advertisers.append(self)

    @staticmethod
    def getTotalClicks() -> int:
        total_clicks = 0
        for advertiser in Advertiser.advertisers:
            total_clicks += advertiser.getClicks()
        return total_clicks

    @staticmethod
    def help() -> str:
        print('you can add a new ad with this command: Ad ad1 = new Ad(id, "title", "img-url", "link", advertiser)')

    def describeMe(self) -> str:
        print(
            "This is 'Advertiser class'. This class provides data about Advertisers such as name , clicks_count , views_count and also can set and get this fields.")

    def incClicks(self):
        super().incClicks()

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> str:
        self.name = name

    def getId(self) -> int:
        return self.id
