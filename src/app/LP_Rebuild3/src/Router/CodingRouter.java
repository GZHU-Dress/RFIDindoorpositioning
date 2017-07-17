package Router;

/**
 * Created by zyvis on 2017/1/14.
 */
public interface CodingRouter<T> {
    /**
     * using interface encode(T s) as a loop
     * maybe you need to adjust something
     * between the data you want to write
     *
     * this interface won`t implement the IO operation
     *
     * @param Ts    a set of object
     * @return      encoded String to write to file
     */
    String encodeFile(T... Ts);

    /**
     * this interface need you to implement the
     * encode rude for single object
     * this interface will be used in encodeFile(T... s)
     * to encode number of objects
     *
     * @param s     single object
     * @return      single object encoded String
     */
    String encode(T s);

    /**
     * using interface decode(String complexData) as a loop
     * something you adjust in encodeFile(T... Ts)
     * you need to implement your own coding rule to decode
     *
     * this interface won`t implement the IO operation
     *
     * @param complexData   the data from file
     * @return              a array of object
     */
    T[] decodeFile(String complexData);
    /**
     * need you to implement the decode rude
     * for single object
     * this interface will be used in
     * decodeFile(String complexData) to decode
     * number of objects
     *
     * @param complexData   the single data from file
     * @return              single object from encoded String
     */
    T decode(String complexData);
}
