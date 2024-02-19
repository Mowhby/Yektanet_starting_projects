import javax.swing.text.View;

public class BaseAdvertising {
    protected int id;
    protected int views;
    protected int clicks;
    protected int getClicks(){
        return clicks;
    }
    protected int getViews(){
        return views;
    }
    protected void incViews(){
        views++;
    }
    protected void incClicks(){
        clicks++;
    }
    public String describeMe(){
        return "Its the base class! other classes will use my fields and methods. I can make this code cleaner!";
    }
}
