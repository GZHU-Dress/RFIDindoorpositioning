package Router;

import java.io.File;
import java.io.IOException;

/**
 * Created by zyvis on 2017/1/14.
 * Usage:
 *  you can include
 *      a coding object which can encode and decode
 *      a protected file object to save the save filepath
 */
public interface IORouter<T> {
    /**
     * read object from selected file
     * String but not the only type for returning
     * @param file  import the file to
     * @return      return the data you want
     *              (metadata,or decoded data)
     * @throws IOException
     */
    T readFile(File file) throws IOException;

    /**
     * the interface to write objects into the file
     * @param file      the file you want to write
     * @param datas     the datas you want to write
     * @throws IOException
     */
    void writeFile(File file, T... datas)throws IOException;
}
