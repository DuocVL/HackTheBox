> [!NOTE]
> - Mức độ: Dễ 
> - Loại: Challenge - Mobile
> - Url: [APKrypt](https://app.hackthebox.com/challenges/APKrypt)
> - Mô tả: Phân tích tĩnh tệp APK khôi phục logic giải mã chuỗi mã hóa flag 

> Decompiler file apk bằng JADX 

- Hàm md5(str) nhận vào 1 chuỗi số trả về chuỗi hexa mã hash MD5 của chuỗi đầu vào 

``` java
    public static String md5(String str) {  
        try {  
            MessageDigest messageDigest = MessageDigest.getInstance("MD5");  
            messageDigest.update(str.getBytes());  
            byte[] bArrDigest = messageDigest.digest();  
            StringBuffer stringBuffer = new StringBuffer();  
            for (byte b : bArrDigest) {  
                stringBuffer.append(Integer.toHexString(b & 255));  
            }  
            return stringBuffer.toString();  
        } catch (NoSuchAlgorithmException e) {  
            e.printStackTrace();  
            return "";  
        }  
    }
```

- Hàm generateKey() tạo 1 SecretKey AES khóa được hard code trong file `Dgu8Trf6Ge4Ki9Lb`
```java
    private static Key generateKey() throws Exception {  
        return new SecretKeySpec("Dgu8Trf6Ge4Ki9Lb".getBytes(), "AES");  
    }
```

- Hàm decrypt(str) nhận vào 1 chuỗi , giải mã base64 chuỗi đầy vào, giải mã dữ liệu đó bằng khóa AES 
```java
    public static String decrypt(String str) throws Exception {  
        Key keyGenerateKey = generateKey();  
        Cipher cipher = Cipher.getInstance("AES");  
        cipher.init(2, keyGenerateKey);  
        return new String(cipher.doFinal(Base64.decode(str, 0)), "utf-8");  
    }
```

> - Chương trình nhận 1 chuỗi đầu vào từ người dùng 
> - Tính hash MD5 từ chuỗi đó so sánh với `735c3628699822c4c1c09219f317a8e9`
> - Nếu chính xác gọi hàm `decrypt("k+RLD5J86JRYnluaZLF3Zs/yJrVdVfGo1CQy5k0+tCZDJZTozBWPn2lExQYDHH1l")` và in ra flag 
> - Việc tìm dữ liệu đầu vào có mã băm `735c3628699822c4c1c09219f317a8e9` khó , nên chỉ cần khôi phục logic giải mã `k+RLD5J86JRYnluaZLF3Zs/yJrVdVfGo1CQy5k0+tCZDJZTozBWPn2lExQYDHH1l` để lấy flag 

```java
    Button b1;  
    EditText ed1;  
  
    @Override // android.app.Activity  
    protected void onCreate(Bundle bundle) {  
        super.onCreate(bundle);  
        setContentView(R.layout.activity_main);  
        this.b1 = (Button) findViewById(R.id.button);  
        this.ed1 = (EditText) findViewById(R.id.editTextVipCode);  
        this.b1.setOnClickListener(new View.OnClickListener() { // from class: com.example.apkrypt.MainActivity.1  
            @Override // android.view.View.OnClickListener  
            public void onClick(View view) {  
                try {  
                    if (MainActivity.md5(MainActivity.this.ed1.getText().toString()).equals("735c3628699822c4c1c09219f317a8e9")) {  
                        Toast.makeText(MainActivity.this.getApplicationContext(), MainActivity.decrypt("k+RLD5J86JRYnluaZLF3Zs/yJrVdVfGo1CQy5k0+tCZDJZTozBWPn2lExQYDHH1l"), 1).show();  
                    } else {  
                        Toast.makeText(MainActivity.this.getApplicationContext(), "Wrong VIP code!", 0).show();  
                    }  
                } catch (Exception e) {  
                    e.printStackTrace();  
                }  
            }  
        });  
    }
```

> - Tạo chương trình giải mã 
> - Sau khi chạy thu được flag `HTB{3nj0y_y0ur_v1p_subscr1pt1on}`

```java
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.Key;
import java.util.Base64;
import java.nio.charset.StandardCharsets;

public class Main {

    public static String decrypt(String str) throws Exception {
        Key keyGenerateKey = generateKey();

        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.DECRYPT_MODE, keyGenerateKey);

        byte[] encryptedBytes = Base64.getDecoder().decode(str);
        byte[] decryptedBytes = cipher.doFinal(encryptedBytes);

        return new String(decryptedBytes, StandardCharsets.UTF_8);
    }

    private static Key generateKey() {
        return new SecretKeySpec(
            "Dgu8Trf6Ge4Ki9Lb".getBytes(StandardCharsets.UTF_8),
            "AES"
        );
    }

    public static void main(String[] args) {
        try {
            String encrypted = "k+RLD5J86JRYnluaZLF3Zs/yJrVdVfGo1CQy5k0+tCZDJZTozBWPn2lExQYDHH1l";
            String decrypted = decrypt(encrypted);

            System.out.println("Decrypted: " + decrypted);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```