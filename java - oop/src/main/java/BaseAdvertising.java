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
        return "This is the base class! other classes will use my fields and methods. I can make this code cleaner!";
    }
}
