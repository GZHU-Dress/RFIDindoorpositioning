package MiniProperties;

import java.awt.image.BufferedImage;

/**
 * Created by zyvis on 2017/3/5.
 */
public class DrawobjImage {
  //  protected String description;
    protected BufferedImage image;

  public BufferedImage getImage() {
    return image;
  }

  public void setImage(BufferedImage image) {
    this.image = image;
  }

  public DrawobjImage(BufferedImage image) {
    this.image = image;
  }
}
