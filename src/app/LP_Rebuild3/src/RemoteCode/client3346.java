//package RemoteCode;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;
import java.net.Socket;
import java.util.Scanner;

/**
 * Created by zyvis on 2017/4/11.
 * 数据提供端的代码，运行后读取同目录下的sendfile
 * 发送到119.29.245.150：3346，需要服务器上运行服务程序
 * 格式详见其中
 */
public class client3346 {
    public static void main(String[] args) throws IOException {
        Socket s=new Socket("119.29.245.150",3346);
        BufferedReader br=new BufferedReader(new FileReader("./sendfile"));
        PrintStream ps = new PrintStream(s.getOutputStream());
        String string;
        while ((string = br.readLine() )!=null) {
            System.out.println("sent:"+string);
            ps.println(string);
        }
        System.out.println("sent all , exit");
    }
}


