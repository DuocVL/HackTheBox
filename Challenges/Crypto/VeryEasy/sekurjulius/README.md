> [!NOTE]
> - Mức độ: Rất dễ 
> - Loại: Crypto 
> - Url: [sekur julius](https://app.hackthebox.com/challenges/sekur%2520julius)
> - Mô tả: Ẩn sâu trong khu rừng là một cuộn giấy cổ, tương truyền rằng ai có thể đọc được những ký tự luôn biến đổi trên đó sẽ sở hữu sức mạnh vô biên. Vào đêm Halloween, một lữ khách tò mò đã tìm thấy cuộn giấy, nơi các con chữ nằm ở những vị trí kỳ lạ, chẳng theo trật tự nào. Khi người này giải mã thông điệp, các từ ngữ dần tự sắp xếp lại, hé lộ một lời nguyền hắc ám. Nhưng ngay khi sự thay đổi cuối cùng hoàn tất, lữ khách cảm nhận được một luồng hiện diện lạnh lẽo phía sau mình, thì thầm: "Ngươi vốn không bao giờ được phép hiểu những điều này." Khu rừng chìm vào tĩnh lặng, nhưng lời nguyền thì đã được thi triển.

> - Chương trình mã hóa flag sử dụng thuật toán mã hóa Caesar 
> - Tạo 1 khóa 1337 byte ngẫu nhiên 
> - Tạo vòng lặp lặp qua từng byte trong khóa mỗi byte lặp qua tất cả các kí tự trong thông tin bản rõ 
> - Thay các kí tự khoảng trắng bằng `0` các kí tự không trong khoảng 'A-Z' giữ nguyên
> - Nếu kí tự trong `A-Z` thực hiện dịch chuyển kí tự trong khoảng `A-Z` theo key giống thuật toán Caesar
> - Mã hóa Caesar nhiều vòng với các khóa ngẫu nhiên 
> -> Mật mã Caesar dù mã hóa nhiều vòng dữ liệu trong plain text đều được dịch chuyển cùng 1 khoảng trong bảng ASCII và vẫn trong khoảng `A-Z` 
> -> các khóa chỉ nằm trong khoảng 0-25 ((o + shift) % 26)

```python
from random import choices
import os

def julius_encrypt(msg, shift):

	ct = ''
	for p in msg:
		if p == ' ':
			ct += '0'
		elif not ord('A') <= ord(p) <= ord('Z'):
			ct += p
		else:
			o = ord(p) - 65# 0 - 25
			ct += chr(65 + (o + shift) % 26)
	return ct

def encrypt(msg, key):

	for shift in key:
		msg = julius_encrypt(msg, shift)
return msg

msg = open('secret.txt').read().upper()
secure_key = os.urandom(1337)

	f.write(encrypt(msg, secure_key))
```

```
JRYPBZR0GB0UNPXGUROBB0GJBGUBHFNAQGJRAGLSBHE!0GUVF0VF0N0CEBBS0BS0PBAPRCG0GB0CEBIR0LBH0GUNG0GUR0PNRFNE0PVCURE0VF0VAFRPHER0AB0ZNGGRE0UBJ0ZNAL0GVZRF0LBH0NCCYL0VG.0GUR0FRPHEVGL0BS0N0GUBHFNAQ0QVFGVAPG0FUVSGF0VF0RIRAGHNYYL0GUR0FNZR0NF0GUNG0BS0N0FVATYR0FUVSG.0RABHTU0ZHZOYVAT,0GNXR0LBHE0SYNT0NAQ0RAWBL0GUR0ERFG0BS0GUR0PBAGRFG.0ZNXR0FHER0LBH0JENC0GUR0SBYYBJVAT0GRKG0JVGU0GUR0UGO0SYNT0SBEZNG0GURRSSRPGVIRXRLFCNPRBSPNRFNEQRCRAQFBAGURFVMRBSGURNYCUNORG.
```

> - Tạo chương trình giải mã 
> - Vòng lặp 0-25 giá trị khóa, xử lý theo thuật toán Caesar với các khóa đó 
> - Thay thế '0' thành khoảng trắng 
> - Các kí tự không trong khoảng `A-Z` giữ nguyên 

```python
with open('output.txt', 'r') as f:

	encrypt_data = f.read()
	for key in range(0,25):
		ct = ''
	for p in encrypt_data:
	
		if p == '0':
			ct += ' '
		
		elif not ord('A') <= ord(p) <= ord('Z'):
			ct += p
		
		else:
			o = ord(p) - 65# 0 - 25
			ct += chr(65 + (o + key) % 26)
	
	print(f"[+]{key} - {ct}")
```

> - Thu được plain text với khóa chính xác là 13
> - Thu được flag `HTB{THEEFFECTIVEKEYSPACEOFCAESARDEPENDSONTHESIZEOFTHEALPHABET}`

```
[+]13 - WELCOME TO HACKTHEBOO TWOTHOUSANDTWENTYFOUR! THIS IS A PROOF OF CONCEPT TO PROVE YOU THAT THE CAESAR CIPHER IS INSECURE NO MATTER HOW MANY TIMES YOU APPLY IT. THE SECURITY OF A THOUSAND DISTINCT SHIFTS IS EVENTUALLY THE SAME AS THAT OF A SINGLE SHIFT. ENOUGH MUMBLING, TAKE YOUR FLAG AND ENJOY THE REST OF THE CONTEST. MAKE SURE YOU WRAP THE FOLLOWING TEXT WITH THE HTB FLAG FORMAT THEEFFECTIVEKEYSPACEOFCAESARDEPENDSONTHESIZEOFTHEALPHABET.
```

