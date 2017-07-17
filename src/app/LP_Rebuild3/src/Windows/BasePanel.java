package Windows;

import Loger.defaultLog;
import MiniProperties.Framesize;
import MiniProperties.Waypoint;
import Objects.Actor;
import Objects.Drawobj;

import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.Iterator;
import java.util.LinkedList;

/**
 * Created by zyvis on 2016/11/28.
 */
public class BasePanel extends JPanel {

    protected BufferedImage baseImage=null;

    public void setImageFloor(BufferedImage imageFloor) {
        this.imageFloor = imageFloor;
    }

    protected BufferedImage imageFloor=null;
    protected LinkedList<Actor> objlist =new LinkedList<>();
    public  BufferedImage getBaseImage() {
       return baseImage;
    }
    public void setBaseImage(BufferedImage baseImage) {
       this.baseImage = baseImage;
        defaultLog.report("baseimage installed");
    }
    protected Framesize framesize;
    public BasePanel() {
        if(baseImage!=null)
            framesize=new Framesize(baseImage.getWidth(),baseImage.getHeight());
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        //g.drawImage(imageFloor,0,0,null);
    }
    public void add(Actor tmp){
        objlist.add(tmp);
        defaultLog.report("actor obj added successfully");
        Graphics g = null;
        defaultLog.report("draw obj");
        g.drawImage(tmp.getDrawobjImage().getImage(),
                tmp.getWaypoint().getMidX()-tmp.getFramesize().getWidth()/2,
                tmp.getWaypoint().getMidY()-tmp.getFramesize().getHeight()/2,
                null);
        this.update(g);
    }
    public void clear(){
        paint(baseImage.getGraphics());
    }
}

