package twitter.controller;

import org.springframework.scheduling.annotation.Async;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.*;
import java.util.Properties;
import java.net.URL;

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
            System.out.println(port);
        } catch (IOException e){
            System.out.println("DB Configuration does not exist");
        }
    }

    /**
     * Get the dataset from the couchdb
     */
    @Async
    @RequestMapping("/twitter/get_processed_data")
    public String getProcessedData(){
        // generate the request
        String[] cmds = {"curl", "-X", "GET",  "http://user:pass@127.0.0.1:5984/demo"};
        // send request to couchdb

        return execCurl(cmds);
    }

    /**
     * Send curl request and get response
     * @param cmds the curl request
     * @return response from server
     */
    public static String execCurl(String[] cmds) {
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