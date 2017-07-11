package Kernel;

import Loger.defaultLog;
import MiniProperties.Waypoint;
import Objects.Actor;
import Objects.Tag;
import Windows.BasePanel;

/**
 * Created by zyvis on 2017/4/13.
 */
public class CommandCoder {
    public final static String settag="settag";
    public final static String setactor="setactor";
    protected BasePanel basePanel;
    protected String code;

    public CommandCoder(BasePanel basePanel) {
        this.basePanel = basePanel;
    }
    public void run(String command){
        defaultLog.report("cmd need to run : "+command);
        if(command=="end"){
            defaultLog.report("cmd run :end");
            return;
        }
        String cmd[]=command.split(" ");
        String waypoint[]=cmd[1].split(",");
        if(cmd[0].equals(settag)){
            basePanel.add(new Tag(new Waypoint(Integer.parseInt(waypoint[0]),Integer.parseInt(waypoint[1]))));
            defaultLog.report("cmd run : set tag");
        }
        if(cmd[0].equals(setactor)){
            basePanel.add(new Actor(new Waypoint(Integer.parseInt(waypoint[0]),Integer.parseInt(waypoint[1]))));
            defaultLog.report("cmd run : set actor");
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        else return;
        return;


    }
}
