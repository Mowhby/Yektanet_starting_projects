public class Advertiser extends BaseAdvertising {
    private static int totalClicks = 0;
    private String name;

    public Advertiser(int id, String name) {
        this.name = name;
        this.id = id;
        this.clicks = 0;
        this.views = 0;
    }

    public static int getTotalClicks() {
        return totalClicks;
    }

    public static String help() {
        return "you can add a new ad with this command: Ad ad1 = new Ad(id, \"title\", \"img-url\", \"link\", advertiser);";
    }

    @Override
    public String describeMe() {
        return "Hi! it's advertiser with id " + id + " and my name is " + name + " enjoy our Ads!";
    }

    @Override
    protected void incClicks() {
        super.incClicks();
        totalClicks++;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getId(){
        return this.id;
    }
}
