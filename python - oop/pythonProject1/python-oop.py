class BaseAdvertising:
    def __init__(self):
        self.views = 0
        self.clicks = 0

    @staticmethod
    def describeMe():
        print('Its the base class! other classes will use my fields and methods. I can make this code cleaner!')

    def getClicks(self):
        return self.clicks

    def getViews(self):
        return self.views

    def incViews(self):
        self.views += 1

    def incClicks(self):
        self.clicks += 1


class Advertiser(BaseAdvertising):
    totalClicks = 0

    def __init__(self, id, name):
        super().__init__()
        self.name = name
        self.id = id

    @staticmethod
    def getTotalClicks():
        return Advertiser.totalClicks

    @staticmethod
    def help():
        print('you can add a new ad with this command: Ad ad1 = new Ad(id, "title", "img-url", "link", advertiser)')

    def describeMe(self):
        print(f"Hi! it\'s advertiser with id {self.id} and my name is {self.name} enjoy our Ads!")

    def incClicks(self):
        BaseAdvertising.incClicks(self)
        Advertiser.totalClicks += 1

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id


class Ad(BaseAdvertising):
    def __init__(self, id, title, imgURL, link, advertiser):
        super().__init__()
        self.id = id
        self.title = title
        self.imgURL = imgURL
        self.link = link
        self.advertiser = advertiser

    def describeMe(self):
        print(f"Hi! it\'s an Ad. my advertiser\'s id is {self.advertiser.getId()} hope you enjoy!")

    def incClicks(self):
        BaseAdvertising.incClicks(self)
        self.advertiser.incClicks()

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getImgURL(self):
        return self.imgURL

    def setImgURL(self, imgURL):
        self.imgURL = imgURL

    def getLink(self):
        return self.link

    def setLink(self, link):
        self.link = link


baseAdvertising = BaseAdvertising()
advertiser1 = Advertiser(1, "name1")
advertiser2 = Advertiser(2, "name2")
ad1 = Ad(1, "title1", "img-url1", "link1", advertiser1)
ad2 = Ad(2, "title2", "img-url2", "link2", advertiser2)
BaseAdvertising.describeMe()
ad2.describeMe()
advertiser1.describeMe()
ad1.incViews()
ad1.incViews()
ad1.incViews()
ad1.incViews()
ad2.incViews()
ad1.incClicks()
ad1.incClicks()
ad2.incClicks()
print(advertiser2.getName())
advertiser2.setName("new name")
print(advertiser2.getName())
print(ad1.getClicks())
print(advertiser2.getClicks())
print(Advertiser.getTotalClicks())
Advertiser.help()
