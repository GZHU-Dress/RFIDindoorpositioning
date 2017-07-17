package Kernel;

import Loger.defaultLog;

import java.awt.*;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;

/**
 * Created by zyvis on 2017/4/13.
 */
public class PanelUpdate implements Runnable {
    protected LinkedList<Component> list=new LinkedList<Component>();
    @Override
    public void run() {
        while(true) {
                allUpdate();
                //defaultLog.report("PanelUpdate thread update successfully");
        }
    }
    public void addComp(Component c){
        list.add(c);
    }
    public void allUpdate(){
        for (Component e:
             list) {
            e.repaint();
        }
    }

}
