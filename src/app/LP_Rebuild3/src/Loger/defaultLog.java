package Loger;

import java.util.Objects;

/**
 * Created by zyvis on 2017/4/10.
 */
public class defaultLog implements Log{

    protected static Log loger = new defaultLog();
    @Override
    public void reportLog(Object... something) {
        String tmp ="";
        for(Object i:something){
            tmp+=i.toString();
        }
        System.out.println(tmp);
    }

    public static void report(Object... something ){
        loger.reportLog(something);
    }
}
