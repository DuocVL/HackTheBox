> [!NOTE]
> Mức độ: Rất dễ 
> Loại: Crypto
> Url: https://app.hackthebox.com/challenges/BabyEncryption
> Mô tả: Bạn đang truy đuổi một tổ chức tội phạm có liên quan đến thị trường vũ khí bất hợp pháp tại quốc gia của mình. Với tư cách là một đặc vụ bí mật, bạn đã thâm nhập sâu vào tổ chức này đến mức được phép tham gia các cuộc họp với khách hàng. Trong lần thương thảo gần nhất, bạn đã tìm thấy một thông điệp mật dành cho khách hàng. Thông điệp này chứa đựng những thông tin quan trọng về việc giao hàng. Liệu bạn có thể giải mã được nó không?

> Giải nén thu được 2 file 
> File chall.py dùng để mã hóa dữ liệu 
> File msg.enc chứa dữ liệu mã hóa 

> File chall.py chứa thuật toán mã hóa 
> - Đọc dữ liệu cần mã hóa 
> - Mã hóa từng kí tự bằng thuật toán `(123 * char + 18) % 256`
> - Lưu dữ liệu dưới dạng hexa vào file `msg.enc`

```python
import string
from secret import MSG

def encryption(msg):
	ct = []
	
	for char in msg:
	ct.append((123 * char + 18) % 256)
	
	return bytes(ct)

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()
```

> Tạo chương trình giải mã 
> - Đọc mảng dữ liệu hexa từ file và chuyển sang kiểu bytes 
> - Tạo 1 từ điển ánh xạ từng kí tự có thể in với đầu ra của thuật toán `(123 * ord(char) + 18) % 256` và kiểm tra ta thấy không có kí tự nào bị trùng đầu ra 
> - Xây dựng dữ liệu bản rõ bằng cách tra cứu từ điển 

```python
import string

with open('msg.enc', 'r') as file:

	encrypted_hex = file.read()
	encrypted_bytes = bytes.fromhex(encrypted_hex)
	
	print(f'[+] Encrypted hex: {encrypted_hex}')
	print(f'[+] Encrypted bytes: {encrypted_bytes}')
	print(f'[+] Encrypted length: {len(encrypted_bytes)}')
	
	printable_chars = string.printable
	reverse_lookup = {}
	
	for char in printable_chars:
		encrypted_value = (123 * ord(char) + 18) % 256
		reverse_lookup[encrypted_value] = char
	
	print(f'[+] Printable characters count: {len(printable_chars)}')
	print(f'[+] Reverse lookup entries: {len(reverse_lookup)}')
	
	plaintext = ""
	
	for encrypted_byte in encrypted_bytes:
	plaintext += reverse_lookup[encrypted_byte]
	
	print(f'[+] Decrypted plaintext: {plaintext}')
```

> Chạy chương trình thu được flag 

```python
❯ python3 decryption.py
[+] Encrypted hex: 6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921
[+] Encrypted bytes: b'n\n\x93r\xecI\xa3\xf6\x93\x0e\xd8r?\x9d\xf6\xf6r\x0e\xd8\xd8\x9d\xc4\x93r"\xecr\x14\xd8\x9d\x1e\x0e5,\xe0\xaan\xc8+\xf6""{\xb7\x0e\x7f\xb75"I\xb7\xd8\x93\xc4\x93\xd8S\x9d\xec\x8f\xb7\x93]I\x0e\x7f\x9d"\xec\x89\xb7\xa3"\xec\x8f\xd8\x0e\x7f\x89!'
[+] Encrypted length: 80
[+] Printable characters count: 100
[+] Reverse lookup entries: 100
[+] Decrypted plaintext: Th3 nucl34r w1ll 4rr1v3 0n fr1d4y.
HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}
```