package twitter.controller;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import org.springframework.scheduling.annotation.Async;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.*;
import java.util.List;
import java.util.Properties;
import com.alibaba.fastjson.JSONObject;

@RestController
public class TwitterController {

    // database configuration
    String dbConfiguration = "src/main/java/twitter/db_config.properties";
    String username;
    String password;
    String node0;
    String port;
    String oldDBName;
    String newDBName;

    /**
     * The initialzier which set up the database configuration
     */
    public TwitterController() {
        try {
            // read the configuration file .properties
            InputStream file = new BufferedInputStream(new FileInputStream(dbConfiguration));
            Properties properties = new Properties();
            properties.load(file);
            // assign configuration
            username = (String)properties.get("username");
            password = (String)properties.get("password");
            node0 = (String)properties.get("node0");
            port = (String)properties.get("port");
            oldDBName = (String)properties.get("old_db_name");
            newDBName = (String)properties.get("new_db_name");
        } catch (IOException e){
            System.out.println("DB Configuration does not exist");
        }
    }

    /**
     * Get the dataset from the couchdb
     */
    @Async
    @RequestMapping("/twitter/get_data")
    public List<JSONObject> getData(){
        // generate the request
        String url = "http://" + username + ":" + password + "@" + node0 + ":" + port + "/" + newDBName + "/_all_docs";
        String[] cmds = {"curl", "-X", "GET", url};
        // send request to couchdb and get the response
        String resp = execCurl(cmds);
        // transfer response from String to Json
        JSONObject respJson = JSON.parseObject(resp);
        // get the data
        List<JSONObject> rows = JSONArray.parseArray(JSON.toJSONString(respJson.get("rows")), JSONObject.class);

        return rows;
    }

    /**
     * Send curl request and get response
     * @param cmds the curl request
     * @return response from server
     */
    private static String execCurl(String[] cmds) {
        ProcessBuilder process = new ProcessBuilder(cmds);
        Process p;
        try {
            p = process.start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
            StringBuilder builder = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                builder.append(line);
                builder.append(System.getProperty("line.separator"));
            }
            return builder.toString();

        } catch (IOException e) {
            System.out.print("error");
            e.printStackTrace();
        }
        return null;
    }
}