package Objects;

import Loger.defaultLog;
import MiniProperties.DrawobjImage;
import MiniProperties.Framesize;
import MiniProperties.Waypoint;

/**
 * Created by zyvis on 2017/3/5.
 */
public class Tag extends Actor {
    private static Framesize defaultFramesize = new Framesize(14,14);
    private static DrawobjImage defaulttagImage = null;
    double floatNumber;
    static int updateGap_ms;
    public static void setDefaultImage(DrawobjImage image){
        defaulttagImage=image;
    }
    protected Tag(String description, Framesize framesize, Waypoint waypoint, DrawobjImage drawobjImage) {
        super(description, framesize, waypoint, drawobjImage);
    }
    public Tag(Waypoint waypoint){
        super(waypoint);
        this.drawobjImage=defaulttagImage;
    }

}
