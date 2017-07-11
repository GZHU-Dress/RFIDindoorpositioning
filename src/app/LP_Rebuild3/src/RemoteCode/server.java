package RemoteCode;
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.NoSuchElementException;
import java.util.Scanner;
/**
 * Created by zyvis on 2017/4/14.
 * 此代码运行在服务端，作为中间代理服务器
 * 3345作为客户端接入，3346作为数据提供端接入
 * 由于写得仓促，需要先运行这个，
 * 再运行客户端，最终启动数据提供端
 */
public class server {
    public static void main(String[] args) throws IOException {
        ServerSocket lpClient=new ServerSocket(3345);//LP Client;
        ServerSocket lpDataSender=new ServerSocket(3346);

        PrintStream clientPrinter;
        Scanner dataScanner;
        Socket clientSocket=null;
        Socket dataSenderSocket=null;
        while(true){
            System.out.println("wait for connection");
            if(clientSocket==null){
                clientSocket=lpClient.accept();
                System.out.println("client connect !");
            }
            if(dataSenderSocket==null){
                dataSenderSocket=lpDataSender.accept();
                System.out.println("data sender connect !");
            }
            if(clientSocket==null||dataSenderSocket==null)continue;
            System.out.println("client && data sender is ready");
            dataScanner = new Scanner(dataSenderSocket.getInputStream());
            clientPrinter = new PrintStream(clientSocket.getOutputStream());
            for(;;) {
                try{
                    clientPrinter.println(dataScanner.nextLine());
                    System.out.println("double send");
                } catch (NoSuchElementException e){
                    System.out.println("DATA END");
                    dataSenderSocket=null;
                    System.out.println("data sender out of connection !");
                    break;
                }

            }
        }

    }
}
