public class Ad extends BaseAdvertising {
    private String title;
    private String imgURL;
    private String link;
    private Advertiser advertiser;

    public Ad(int id, String title, String imgURL, String link, Advertiser advertiser) {
        this.id = id;
        this.title = title;
        this.imgURL = imgURL;
        this.link = link;
        this.advertiser = advertiser;
        this.clicks_count = 0;
        this.views_count = 0;
    }

    @Override
    public String describeMe() {
        return "This is 'Ad class'. This class provides data about Ads such as title , imgURL , link ,clicks_count , views_count , advertiser and also can set and get this fields.";
    }

    @Override
    protected void incClicks() {
        super.incClicks();
        advertiser.incClicks();
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getImgURL() {
        return imgURL;
    }

    public void setImgURL(String imgURL) {
        this.imgURL = imgURL;
    }

    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }
}
