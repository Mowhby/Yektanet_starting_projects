import java.util.ArrayList;

public class Advertiser extends BaseAdvertising {
    private static ArrayList<Advertiser> advertisers = new ArrayList<>();
    private String name;

    public Advertiser(int id, String name) {
        this.name = name;
        this.id = id;
        this.clicks_count = 0;
        this.views_count = 0;
        advertisers.add(this);
    }

    public static int getTotalClicks() {
        int totalClicks = 0;
        for (int i = 0; i < advertisers.size(); i++) {
            totalClicks += advertisers.get(i).clicks_count;
        }
        return totalClicks;
    }

    public static String help() {
        return "you can add a new ad with this command: Ad ad1 = new Ad(id, \"title\", \"img-url\", \"link\", advertiser);";
    }

    @Override
    public String describeMe() {
        return "This is 'Advertiser class'. This class provides data about Advertisers such as name , clicks_count , views_count and also can set and get this fields.";
    }

    @Override
    protected void incClicks() {
        super.incClicks();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getId() {
        return this.id;
    }
}
