> [!NOTE]
> Mức độ: Rất dễ 
> Loại: Crypto
> Url: https://app.hackthebox.com/challenges/The%2520Last%2520Dance
> Tình huống: Để được chấp nhận vào tầng lớp thượng lưu của Đế chế Berford, bạn phải tham dự Vũ hội Cha-Cha thường niên tại Triều đình. Bạn không hề hay biết rằng, giữa vô số quý tộc được mời, lại xuất hiện một điệp viên địch – kẻ đã bị lộ danh tính. Mục tiêu của bạn nhanh chóng trở thành việc bắt giữ hắn; bạn đã thực hiện thành công sau khi lén bỏ thứ gì đó vào đồ uống của hắn. Sau nhiều giờ thẩm vấn tại phòng hỏi cung của cơ quan, cuối cùng bạn cũng thu thập được những thông tin quan trọng về các kênh liên lạc bí mật của tổ chức địch. Liệu bạn có thể tận dụng những gì đã biết để giải mã phần còn lại của các thông điệp đó không?

> Giải nén thu được 2 file 
> - File source.py chứa thuật toán mã hóa 
> - File out.txt chứa thông tin đã mã hóa 

> `source.py` sử dụng thuật toán ChaCha20 để mã hóa thông điệp 
> https://en.wikipedia.org/wiki/ChaCha20-Poly1305
> ChaCha20 là thuật toán mã hóa đối xứng dạng dòng (stream cipher) được thiết kế bởi Daniel J. Bernstein. Nó dùng một khóa bí mật để tạo ra chuỗi byte giả ngẫu nhiên (keystream), sau đó XOR chuỗi này với dữ liệu gốc để tạo ra dữ liệu đã mã hóa.
> 
> Chương trình tạo cặp key(32 byte) và iv(12 byte) ngẫu nhiên dùng cho thuật toán ChaCha20 
> Sau đó mã hóa message, flag bằng cùng key, iv 
> Lưu trữ thông điệp mã hóa vào file `out.txt`

```python
from Crypto.Cipher import ChaCha20
from secret import FLAG
import os

def encryptMessage(message, key, nonce):

	cipher = ChaCha20.new(key=key, nonce=iv)
	ciphertext = cipher.encrypt(message)
	
	return ciphertext

def writeData(data):

	with open("out.txt", "w") as f:
	f.write(data)

if __name__ == "__main__":

	message = b"Our counter agencies have intercepted your messages and a lot "
	message += b"of your agent's identities have been exposed. In a matter of "
	message += b"days all of them will be captured"
	
	key, iv = os.urandom(32), os.urandom(12)
	
	encrypted_message = encryptMessage(message, key, iv)
	encrypted_flag = encryptMessage(FLAG, key, iv)
	
	data = iv.hex() + "\n" + encrypted_message.hex() + "\n" + encrypted_flag.hex()
	
	writeData(data)
```

> Việc tái sử dụng key, iv cùng với ta biết được bản rõ của message và encrypted_message từ đó lấy được key_stream của thuật toán 
> Từ key_stream sẽ giải mã và lấy được flag 
> 
> Công thức mã hóa: C = P XOR K
> Công thức giải mã: P = C XOR K 
> Trong đó:
> + \(P\): plaintext — dữ liệu gốc.
> + \(K\): keystream — chuỗi byte được tạo từ ChaCha20.
> + \(C\): ciphertext — bản mã.

> Chương trình giải mã 
> - Đọc các thông tin từ file out.txt 
> - Lấy `key_stream = message xor encrypted_message`
> - Giải mã `flag = key-stream xor encrypted_flag`

```python
message = b"Our counter agencies have intercepted your messages and a lot "
message += b"of your agent's identities have been exposed. In a matter of "
message += b"days all of them will be captured"

with open("out.txt", "r", encoding='utf-8') as file:
	
	iv = file.readline().strip()
	encrypted_message = file.readline().strip()
	encrypted_flag = file.readline().strip()
	print(f'[+] iv: {iv}')
	print(f'[+] encrypted_message: {encrypted_message}')
	print(f'[+] encrypted_flag: {encrypted_flag}')
	
	encrypted_message = bytes.fromhex(encrypted_message)
	encrypted_flag = bytes.fromhex(encrypted_flag)
	print(f'[+] message length: {len(message)}')
	print(f'[+] encrypted_message length: {len(encrypted_message)}')
	print(f'[+] encrypted_flag length: {len(encrypted_flag)}')
	
	key_stream = bytes(a ^ b for a, b in zip(message, encrypted_message))
	flag = bytes(a ^ b for a, b in zip(encrypted_flag, key_stream))
	
	print(f'[+] Flag: {flag}')
```

> Lấy được flag

```python
❯ python3 decrypt.py
[+] iv: c4a66edfe80227b4fa24d431
[+] encrypted_message: 7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990
[+] encrypted_flag: 7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7
[+] message length: 156
[+] encrypted_message length: 156
[+] encrypted_flag length: 51
[+] Flag: b'HTB{und3r57AnD1n9_57R3aM_C1PH3R5_15_51mPl3_a5_7Ha7}'
```