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
        DataReceiverLinstener dataReceiverLinstener=new DataReceiverLinstener();
        DataSenderLinstener dataSenderLinstener=new DataSenderLinstener();



        while(true){
            System.out.println("wait for connection");
            dataReceiverLinstener.start();
            dataSenderLinstener.start();

            if(!(dataReceiverLinstener.isLink()&&dataSenderLinstener.isLink()))continue;
            new Send(new PrintStream(dataReceiverLinstener.clientSocket.getOutputStream()),new Scanner(dataSenderLinstener.dataSenderSocket.getInputStream())).start();

        }

    }
    private static class Send extends Thread{
        PrintStream clientPrinter;
        Scanner dataScanner;

        public Send(PrintStream clientPrinter, Scanner dataScanner) {
            this.clientPrinter = clientPrinter;
            this.dataScanner = dataScanner;
        }

        @Override
        public synchronized void start() {
            super.start();
            System.out.println("client && data sender is ready");
            for(;;) {
                try{
                    clientPrinter.println(dataScanner.nextLine());
                    System.out.println("double send");
                } catch (NoSuchElementException e){
                    System.out.println("DATA END");
                    //dataSenderLinstener.interruptLink();
                    System.out.println("data sender out of connection !");
                    break;
                }

            }
        }
    }
    private static class DataReceiverLinstener extends Thread{
        ServerSocket lpClient=new ServerSocket(3345);//LP Client;
        Socket clientSocket=null;

        private DataReceiverLinstener() throws IOException {
        }

        @Override
        public synchronized void start() {
            super.start();
            for(;;) {
                if (clientSocket == null) {
                    try {
                        clientSocket = lpClient.accept();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    System.out.println("client connect !");
                }
            }
        }
        boolean isLink(){
            return clientSocket!=null;
        }
        void interruptLink(){
            clientSocket=null;
        }
    }
    private static class DataSenderLinstener extends Thread{
        ServerSocket lpDataSender=new ServerSocket(3346);
        Socket dataSenderSocket=null;
        private DataSenderLinstener() throws IOException {
        }

        @Override
        public synchronized void start() {
            super.start();
            if(dataSenderSocket==null){
                try {
                    dataSenderSocket=lpDataSender.accept();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                System.out.println("data sender connect !");
            }
        }
        void interruptLink(){
            dataSenderSocket=null;
        }
        boolean isLink(){
            return dataSenderSocket!=null;
        }
    }
}
