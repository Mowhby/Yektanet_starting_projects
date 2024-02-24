public class BaseAdvertising {
    protected int id;
    protected int views_count;
    protected int clicks_count;

    protected int getClicks() {
        return clicks_count;
    }

    protected int getViews() {
        return views_count;
    }

    protected void incViews() {
        views_count++;
    }

    protected void incClicks() {
        clicks_count++;
    }

    public String describeMe() {
        return "'This is 'Base Advertising class'. Other classes use my fields(views_count & clicks_count) and methods. Classes use functions for getting and incrementing fields in this class. This class make this code cleaner!')";
    }
}
