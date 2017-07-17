package Kernel;

import Objects.Drawobj;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by zyvis on 2017/3/5.
 */
public class DrawobjManager {
    protected List<Drawobj> Taglist =new ArrayList<>();
    public void addTag(Drawobj drawobj){
        Taglist.add(drawobj);
    }
}
