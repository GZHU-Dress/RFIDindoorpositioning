package Windows;

import MiniProperties.Framesize;
import MiniProperties.Waypoint;

import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

/**
 * Created by zyvis on 2016/12/7.
 */
public class MainWindow {
    private JFrame mainWindow;
    private JMenuBar menuBar;
    private JMenu menuFile,menuEdit,menuView,menuPoint,menuAbout;

    public BasePanel getLocalBasePanel() {
        return localBasePanel;
    }

    private BasePanel localBasePanel=new BasePanel();

    public MainWindow(){
        mainWindow = new JFrame("D");
        mainWindow.setResizable(false);
        Framesize frameSize=new Framesize(1024,768);
        System.out.println(getScreenMidPoint().getMidX() - frameSize.getWidth()/ 2);
        System.out.println(frameSize.getWidth());
        System.out.println(getScreenMidPoint().getMidX()-frameSize.getHeight()/2);
        System.out.println(frameSize.getHeight());

        mainWindow.setBounds(getScreenMidPoint().getMidX() - frameSize.getWidth()/ 2, getScreenMidPoint().getMidY()-frameSize.getHeight()/2, frameSize.getWidth(),frameSize.getHeight());
        //localBasePanel = new BasePanel(0, 0);

        importMenu();
        mainWindow.setJMenuBar(menuBar);
        //mainWindow.add(localBasePanel);
        mainWindow.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosed(WindowEvent e) {
                super.windowClosed(e);
                System.exit(0);
            }
        });
        mainWindow.add(localBasePanel);
        mainWindow.setVisible(true);

    }
    public static Waypoint getScreenMidPoint(){
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        return new Waypoint(screenSize.width/2,screenSize.height/2);
    }
    private void importMenu() {
        menuBar = new JMenuBar();
        menuFile = new JMenu("menuFile");
        JMenuItem menuFile_load = new JMenuItem("menuFile1");
        menuView = new JMenu("menuView");
        menuPoint = new JMenu("menuPoint");
        menuAbout = new JMenu("menuAbout");
        menuBar.add(menuFile);
        menuFile.add(menuFile_load);
        menuBar.add(menuView);

        //FileDialog loader = new FileDialog(mainWindow, "load the file", FileDialog.LOAD);



    }



}
