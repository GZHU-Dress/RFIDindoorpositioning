package Network;

import Loger.Log;
import Loger.defaultLog;

import java.io.IOException;
import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Created by zyvis on 2017/4/10.
 */
public class SocketReceiver {
    Socket insideSocket;
    Scanner scanner;

    public SocketReceiver(String IP,int port) throws IOException {
        insideSocket=new Socket(IP,port);
        defaultLog.report("connection successfully : "+IP.toString()+":"+port);
        scanner = new Scanner(insideSocket.getInputStream());
        defaultLog.report("scanner ready");
    }
    public String getData() throws IOException {
        String tmp = scanner.nextLine();
        //defaultLog.report("data get : "+tmp);
        return tmp;
    }

}
