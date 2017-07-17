package MiniProperties;

/**
 * Created by zyvis on 2016/12/5.
 */
public class Framesize {
    private int Width;
    private int Height;

    public int getHeight() {
        return Height;
    }

    public int getWidth() {
        return Width;
    }

    public Framesize(int Width, int Height) {
        this.Width = Width;
        this.Height = Height;
    }

    public void setSize(int width,int height) {
        Width = width;
        this.Height=height;
    }

}




