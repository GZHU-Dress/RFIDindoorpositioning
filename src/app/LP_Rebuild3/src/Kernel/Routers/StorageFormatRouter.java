package Kernel.Routers;

/**
 * Created by zyvis on 2017/1/14.
 */
public interface StorageFormatRouter<T> {
    /**
     * 传入一系列对象，对每个对象执行encode
     * 再汇总到一起，此函数完成总存储编码的整合与输出
     *
     * @param Ts    一系列对象
     * @return      系列对象用于写入文件的编码
     */
    String encodeFile(T... Ts);

    /**
     * 用于对传入对象进行单个编码
     * 并非最终的存储对象
     *
     * @param s     对象
     * @return      对象的json格式编码
     */
    String encode(T s);

    /**
     * 用于解码单个对象
     * 可由单个对象的json格式编码反求出对象
     *
     * @param complexData   json格式编码
     * @return              对象
     */
    T decode(String complexData);

    /**
     * 用于从文件读取批量对象json格式
     * 对每句话进行解码，从而反求出系列的对象
     *
     * @param complexData   json格式编码
     * @return              对象组
     */
    T[] decodeFile(String complexData);
}
