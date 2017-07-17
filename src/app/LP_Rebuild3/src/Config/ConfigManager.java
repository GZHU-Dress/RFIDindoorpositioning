package Config;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

/**
 * Created by visn on 17-3-22.
 * 配置管理器，暂未用上
 */
public class ConfigManager {
    /**
     * 组建了一个字符串映射到属性配置表 的hashmap
     */
    protected Map<String,Properties> ConfigMap =new HashMap<>();
    /**
     *指定了一个单独对待配置表的输入流
     * 后期可以改进专门交由一个模块来做
     */
    protected FileInputStream fileInputStream;

    public ConfigManager() {

    }
    public void importConfig(String key, String filepath)throws IOException{
        fileInputStream=new FileInputStream(filepath);
    }
}
