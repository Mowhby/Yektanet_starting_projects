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
        this.clicks = 0;
        this.views = 0;
    }

    @Override
    public String describeMe() {
        return "Hi! it's an Ad. my advertiser's id is " + advertiser.getId() + " hope you enjoy!";
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
