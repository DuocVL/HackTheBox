> [!NOTE]
> - Mức độ: Dễ 
> - Loại: OSINT 
> - Tình huống: Khách hàng của secure-startup.com đã nhận được một số email lừa đảo (phishing) trông rất đáng tin; bạn có biết tại sao không?

> Truy vấn các bản ghi DNS đến tên miền lấy được 1 phần của lá cờ `HTB{RIP_SPF_Always_2nd`

```
❯ dig ANY secure-startup.com

; <<>> DiG 9.20.29 <<>> ANY secure-startup.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 11056
;; flags: qr rd ra; QUERY: 1, ANSWER: 6, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;secure-startup.com.		IN	ANY

;; ANSWER SECTION:
secure-startup.com.	228	IN	A	15.197.148.33
secure-startup.com.	228	IN	A	3.33.130.190
secure-startup.com.	3528	IN	NS	ns69.domaincontrol.com.
secure-startup.com.	3528	IN	NS	ns70.domaincontrol.com.
secure-startup.com.	3528	IN	SOA	ns69.domaincontrol.com. dns.jomax.net. 2023051000 28800 7200 604800 600
secure-startup.com.	1728	IN	TXT	"v=spf1 a mx ?all - HTB{RIP_SPF_Always_2nd"

;; Query time: 97 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (TCP)
;; WHEN: Wed Oct 21 14:23:40 +07 2026
;; MSG SIZE  rcvd: 234
```

> - Vì khách hàng nhận được email lừa đảo nó có thể liên quan đến SDF, DMARC 
> - DMARC là viết tắt của Domain-based Message Authentication, Reporting and Conformance. Đây là cơ chế xác thực email, quy định cách xử lý email không vượt qua xác thực và hỗ trợ thu thập báo cáo về tình trạng giả mạo email
> - Truy cập domain `_dmarc.secure-startup.com` chứa cấu hinhd DMARC của tên miền gửi email 
> thu được phần còn lại của flag `_F1ddl3_2_DMARC}`

```
❯ dig _dmarc.secure-startup.com TXT

; <<>> DiG 9.20.29 <<>> _dmarc.secure-startup.com TXT
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 21053
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;_dmarc.secure-startup.com.	IN	TXT

;; ANSWER SECTION:
_dmarc.secure-startup.com. 1800	IN	TXT	"v=DMARC1;p=none;_F1ddl3_2_DMARC}"

;; Query time: 34 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Wed Oct 21 14:31:17 +07 2026
;; MSG SIZE  rcvd: 99
```

> Flag `HTB{RIP_SPF_Always_2nd_F1ddl3_2_DMARC}`