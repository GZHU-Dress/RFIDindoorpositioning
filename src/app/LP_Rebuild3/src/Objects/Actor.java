package Objects;

import Loger.defaultLog;
import MiniProperties.DrawobjImage;
import MiniProperties.Framesize;
import MiniProperties.Waypoint;

import java.awt.*;

/**
 * Created by zyvis on 2017/3/5.
 */
public class Actor extends Drawobj {
    private static Framesize defaultFramesize = new Framesize(14,14);
    private static DrawobjImage defaultactorImage = null;
    protected DrawobjImage drawobjImage;

    public DrawobjImage getDrawobjImage() {
        return drawobjImage;
    }

    public void setDrawobjImage(DrawobjImage drawobjImage) {
        this.drawobjImage = drawobjImage;
    }

    public static void setDefaultImage(DrawobjImage image){
        defaultactorImage=image;
    }
    protected Actor(String description, Framesize framesize, Waypoint waypoint, DrawobjImage drawobjImage) {
        super(description, framesize, waypoint);
        this.drawobjImage = drawobjImage;
    }
    public Actor(Waypoint waypoint){
        super("no description",defaultFramesize,waypoint);
        this.drawobjImage=defaultactorImage;
        if(defaultactorImage==null){
            defaultLog.report("defaultImage==null");
            return;
        }
        this.waypoint=waypoint;
    }
}
