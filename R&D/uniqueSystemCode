
public static uniqueCode(){

         //method 4 ----------------------------
          System.out.println("plugin loader----------------------------------");
          String jarPath = "/usr/share/elasticsearch/lib/app.jar"; // Update with the actual path to your JAR file
          String data = fetchDataFromJar(jarPath);
          System.out.println(data);

        //method 3 ----------------------------
         getDmiMessages();

        //method 2 ----------------------------
         try{
           String content = new String(Files.readAllBytes(Paths.get("/sys/class/dmi/id/product_uuid")));
           System.out.println("DMI info: " + content);
         } catch (IOException e) {
             e.printStackTrace();
         }


        //method 1 ----------------------------
         String command = "dmesg | grep DMI | sha256sum";                
         try{        
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
             String output = reader.lines().collect(Collectors.joining());
             System.out.println(output);     

         }catch (Exception e) {
             e.printStackTrace();            
         } 

}


public static String fetchDataFromJar(String jarPath) {
        try {            
            File jarFile = new File(jarPath);
            URL jarUrl = jarFile.toURI().toURL();
            System.out.println(jarUrl);
            URLClassLoader classLoader = new URLClassLoader(new URL[]{jarUrl});    
            Class<?> clazz = classLoader.loadClass("lcs.loader.App"); // Update with the actual class name            
            Object instance = clazz.getDeclaredConstructor().newInstance();            
            Method method = clazz.getMethod("getSystCode");
            return (String) method.invoke(instance);

        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void getDmiMessages(){
        ProcessBuilder processBuilder = new ProcessBuilder();    
        processBuilder.command("dmesg");

        try {
            // Start the process
            Process process = processBuilder.start();            
            BufferedReader reader = 
                    new BufferedReader(new InputStreamReader(process.getInputStream()));
            // String output = reader.lines().collect(Collectors.joining());
            // System.out.println(output);
            // String sha256Hash = computeSHA256(output);
            // System.out.println(sha256Hash);
            String line;
            StringBuilder lBuilder = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                if (line.contains("DMI")) {                    
                    lBuilder.append(line + "\n");                   
                }
            }

            System.out.println(lBuilder.toString());
            String sha256Hash = computeSHA256(lBuilder.toString());
            System.out.println("SHA-256 Hash: " + sha256Hash);

            // Wait for the process to finish and get the exit code
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                System.err.println("Error: dmesg command failed with exit code " + exitCode);
            }

        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
            Thread.currentThread().interrupt(); // Restore interrupted state
        }
    }

      private static String computeSHA256(String input)  {
        try {
            // Create a MessageDigest instance for SHA-256            
            MessageDigest digest = MessageDigest.getInstance("SHA-256");                    
            // Hash the input string
            byte[] hashBytes = digest.digest(input.getBytes());            
            // Convert the byte array into a hexadecimal string
            return bytesToHex(hashBytes);
        } catch (Exception e) {
            throw new RuntimeException("SHA-256 algorithm not found!", e);
        }
    }

    private static String bytesToHex(byte[] bytes) {
        Formatter formatter = new Formatter();
        for (byte b : bytes) {
            formatter.format("%02x", b);
        }
        return formatter.toString();
    }
 
