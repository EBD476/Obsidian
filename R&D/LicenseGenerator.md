get unique id from Linux machine
```bash
dmidecode
dmidecode -t 4 | grep ID
```

```bash
cat /etc/machine-id
```


```java

package com.licensor.licensor;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jws;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;
import java.security.Key;
import java.time.Duration;
import java.time.Instant;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.UUID;

import javax.crypto.SecretKey;

public class LicenseGenerator {
    
    private String secret;

    private static final int EXPIRATION_DAYS = 30; // Change this to set the number of days until the license expires
    private static final String ISSUER = "MySoftwareCompany";
    private static final String SUBJECT = "YOUR_SUBJECT";
    private static final long expirationTimeMillis = System.currentTimeMillis() + 86400000; // 24 hours
    
    private Key getSigningKey() {
        byte[] keyBytes = Decoders.BASE64.decode(this.secret);
        return Keys.hmacShaKeyFor(keyBytes);
    }

    

    public static String generateLicense(String licensee, Duration duration) {
        Instant now = Instant.now();
        Instant expiration = now.plus(duration);
        
       return   Jwts.builder()
        .setSubject(SUBJECT)
        .setIssuer(ISSUER)
        .setExpiration(new Date(expirationTimeMillis))
        .signWith(SignatureAlgorithm.HS256, licensee)
        .compact();
    }
    
    public static boolean verifyLicense(String license) {
        //  SecretKey SECRET_KEY = Keys.secretKeyFor(SignatureAlgorithm.HS256);
        try {

                     String licenseKey = "license";
                    // String licenseToken = "YOUR_LICENSE_TOKEN";

                    // Verify the license token
                    Jws<Claims> jws = Jwts.parser()
                            .setSigningKey(licenseKey)
                            .parseClaimsJws(license);

                    // Get the license claims
                    Claims claims = jws.getBody();

                    System.out.println(claims.getExpiration().toString());
            
            return claims.getExpiration().after(new Date());
        } catch (Exception e) {
            return false;
        }
    }    

  public static String generateLicenseKey() {
    LocalDate expirationDate = LocalDate.now().plusDays(EXPIRATION_DAYS);
    String expirationDateString = expirationDate.format(DateTimeFormatter.ISO_LOCAL_DATE);
    UUID uuid = UUID.randomUUID();
    String licenseKey = uuid.toString().replace("-", "") + "-" + expirationDateString;
    return licenseKey;
  }

}
```

Generate License 
```java

 String generatedLicense = LicenseGenerator.generateLicense("license", Duration.ofDays(30));  
  
  LOG.info(generatedLicense);
```

Verify License 
```java
  Boolean verify = LicenseGenerator.verifyLicense("eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJZT1VSX1NVQkpFQ1QiLCJpc3MiOiJNeVNvZnR3YXJlQ29tcGFueSIsImV4cCI6MTY5MDcwNDQ1M30.VcGbFa-BtSrFZTvvU8PDo_jxYJHnaglqg0HheUQhWHA");

        LOG.info(verify)
```