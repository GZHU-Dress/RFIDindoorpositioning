import Network.SocketReceiver;

import java.net.UnknownHostException;

/**
 * Created by zyvis on 2017/3/5.
 */
public class main {
    public static void main(String[] args) throws UnknownHostException {
        System.out.println("helloworld");
        new Kernel.Run().run();
    }
}
