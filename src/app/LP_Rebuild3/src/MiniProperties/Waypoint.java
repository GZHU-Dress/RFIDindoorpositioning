package MiniProperties;

/**
 * Created by zyvis on 2016/12/14.
 */
public class Waypoint {
    protected int midX,midY;

    public int getMidX() {
        return midX;
    }

    public void setMidPoint(int midX,int midY) {
        this.midX = midX;
        this.midY = midY;
    }

    public int getMidY() {
        return midY;
    }

    public Waypoint(int midX, int midY) {
        this.midX = midX;
        this.midY = midY;
    }

    /**
     * change the waypoint (add)
     * @param x
     * @param y
     */
    public void move(int x,int y){
        this.midX+=x;
        this.midY+=y;
    }
}
