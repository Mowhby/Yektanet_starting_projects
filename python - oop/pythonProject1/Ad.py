from BaseAdvertising import BaseAdvertising
from Advertiser import Advertiser


class Ad(BaseAdvertising):
    def __init__(self, id: int, title: str, imgURL: str, link: str, advertiser: Advertiser):
        super().__init__()
        self.id = id
        self.title = title
        self.imgURL = imgURL
        self.link = link
        self.advertiser = advertiser

    def describeMe(self) -> str:
        print(
            "This is 'Ad class'. This class provides data about Ads such as title , imgURL , link , advertiser and also can set and get this fields.")

    def incClicks(self):
        super().incClicks()
        self.advertiser.incClicks()

    def getTitle(self) -> str:
        return self.title

    def setTitle(self, title: str) -> str:
        self.title = title

    def getImgURL(self) -> str:
        return self.imgURL

    def setImgURL(self, imgURL: str) -> str:
        self.imgURL = imgURL

    def getLink(self) -> str:
        return self.link

    def setLink(self, link: str) -> str:
        self.link = link
