package Kernel.Routers;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

/**
 * Created by zyvis on 2017/1/13.
 * JSON路由器，用于翻译本地json文件到对象
 * 同时翻译对象到json格式
 */
public class JsonRouter<T>
{
    private class JsonFormatRouter<T>  implements StorageFormatRouter<T> {
        @Override
        public synchronized String encodeFile(T... Ts) {
            JSONArray objArray = new JSONArray();
            for (T s : Ts) {
                objArray.put(encode(s));
            }
            return objArray.toString();
        }

        @Override
        public synchronized String encode(T student) {
            JSONObject obj = new JSONObject();
            //obj.put("Sex", Sex.Man.toString());
            return obj.toString();
        }

        @Override
        public synchronized T decode(String json) {
            JSONObject student = new JSONObject(json);
//        JSONObject scoreList = new JSONObject(student.get("Score").toString());
//        ScoreList tmpList = new ScoreList();
//        for(StudyObject studyObject:StudyObject.getStudyObjectsList()){
//            int i=studyObject.getIdentifier();
//            try {
//                if (scoreList.get(String.valueOf(i)) != null) {
//                    try {
//                        tmpList.addScore(StudyObject.fetchStudyObject(i), Double.parseDouble(scoreList.get(String.valueOf(i)).toString()));
//                    } catch (DataNotFoundException e) {
//                    }
//                }
//            }catch (JSONException e){
//                continue;
//            }
//        }
//        Log.print("Debuger","decode: Student Object Create"+student.get("name"));
         //   return new Student(student.get("name").toString(), Sex.get(student.get("Sex").toString()), student.getInt("studentCode"), tmpList);
            return null;
        }

        @Override
        public synchronized T[] decodeFile(String json) {
            JSONArray objArray = new JSONArray(json);
            ArrayList<String> tmpArray = new ArrayList<>();
            for (int i = 0; ; i++) {
                try {
                    tmpArray.add(objArray.get(i).toString());
                } catch (JSONException e) {
                    break;
                }
            }
            ArrayList<T> Tlist = new ArrayList<>();
            int size = tmpArray.size();
            for (int i = 0; i < size; i++)
                Tlist.add(decode(tmpArray.get(i)));
            // Log.print("Debuger","decodeFile: Student Object Create Finished");
            return (T[]) Tlist.toArray();
        }
    }
}
