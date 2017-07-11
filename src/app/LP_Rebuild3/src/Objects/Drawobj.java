package Objects;

import MiniProperties.Framesize;
import MiniProperties.Waypoint;

import javax.swing.*;
import java.awt.*;

/**
 * Created by zyvis on 2017/3/5.
 */
public abstract class Drawobj {
    protected Waypoint waypoint;
    protected Framesize framesize;
    protected String description;

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Framesize getFramesize() {
        return framesize;
    }

    public void setFramesize(Framesize framesize) {
        this.framesize = framesize;
    }

    public Waypoint getWaypoint() {
        return waypoint;
    }

    public void setWaypoint(Waypoint waypoint) {
        this.waypoint = waypoint;
    }

    protected Drawobj(String description, Framesize framesize, Waypoint waypoint) {
        this.description = description;
        this.framesize = framesize;
        this.waypoint = waypoint;
    }
}
