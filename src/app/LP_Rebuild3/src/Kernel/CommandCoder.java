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
    public final static String SETTAG ="settag";
    public final static String SETACTOR ="setactor";
    public final static String CLEAR ="clear";
    public final static String END ="end";
    public final static String WAIT ="wait";
    /**
     * 暂存一个基础窗口，用于对其中对象进行操作
     */
    protected BasePanel basePanel;

    public CommandCoder(BasePanel basePanel) {
        this.basePanel = basePanel;
    }
    public void run(String command){
        defaultLog.report("cmd need to run : "+command);
        if(command==END){
            defaultLog.report("cmd run :end");
            return;
        }else if(command==CLEAR){
            basePanel.clear();
            defaultLog.report("cmd run : "+CLEAR);
            return;
        }
        String cmd[]=command.split(" ");
        if(cmd.length==2&&cmd[0].equals(WAIT)){
            try {
                Thread.sleep(Integer.parseInt(cmd[1]));
                return;
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        String waypoint[]=cmd[1].split(",");
        if(cmd[0].equals(SETTAG)){
            basePanel.add(new Tag(new Waypoint(Integer.parseInt(waypoint[0]),Integer.parseInt(waypoint[1]))));
            defaultLog.report("cmd run : "+SETTAG);
        }
        if(cmd[0].equals(SETACTOR)){
            basePanel.add(new Actor(new Waypoint(Integer.parseInt(waypoint[0]),Integer.parseInt(waypoint[1]))));
            defaultLog.report("cmd run : "+SETACTOR);
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        else return;
        return;


    }
}
