from BaseAdvertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    totalClicks = 0

    def __init__(self, id: int, name: str):
        super().__init__()
        self.name = name
        self.id = id

    @staticmethod
    def getTotalClicks() -> int:
        for instance in Advertiser.instances:
            print(instance.name)

    @staticmethod
    def help() -> str:
        print('you can add a new ad with this command: Ad ad1 = new Ad(id, "title", "img-url", "link", advertiser)')

    def describeMe(self) -> str:
        print(
            "This is 'Advertiser class'. This class provides data about Advertisers such as name , clicks_count , views_count and also can set and get this fields.")

    def incClicks(self):
        super().incClicks()
        Advertiser.totalClicks += 1

    def getName(self) -> str:
        return self.name

    def setName(self, name: str) -> str:
        self.name = name

    def getId(self) -> int:
        return self.id
