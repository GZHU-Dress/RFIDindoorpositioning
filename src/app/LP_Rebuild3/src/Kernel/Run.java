package Kernel;

import Loger.defaultLog;
import MiniProperties.DrawobjImage;
import MiniProperties.Waypoint;
import Network.SocketReceiver;
import Objects.Actor;
import Objects.Tag;
import Windows.MainWindow;

import java.io.IOException;
import java.net.Socket;

/**
 * Created by zyvis on 2017/3/5.
 */
public class Run implements Runnable {
    ImageManager im =new ImageManager();
    SocketReceiver socketReceiver;
    CommandCoder commandCoder;
    @Override
    public void run() {
        try {
            im.importImage("BaseImage", "src/ImageFolder/base.jpg");
            im.importImage("TagImage", "src/ImageFolder/tag.png");
            im.importImage("ActorImage", "src/ImageFolder/actor.png");
            Actor.setDefaultImage(new DrawobjImage(im.fecth("ActorImage")));
            Tag.setDefaultImage(new DrawobjImage(im.fecth("TagImage")));
            defaultLog.report("Import image successfully");
        }catch (IOException e){
            e.printStackTrace();
        }
        MainWindow mainWindow=new MainWindow();
        mainWindow.getLocalBasePanel().setBaseImage(im.fecth("BaseImage"));
        defaultLog.report("Panel ready ");
        try {
            socketReceiver=new SocketReceiver("119.29.245.150",3345);
            defaultLog.report("Socket ready");
        } catch (IOException e) {
            e.printStackTrace();
        }
        commandCoder=new CommandCoder(mainWindow.getLocalBasePanel());
        try {
            for(;;)
            commandCoder.run(socketReceiver.getData());
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

}
