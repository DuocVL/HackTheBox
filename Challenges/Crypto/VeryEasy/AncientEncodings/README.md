> [!NOTE]
> - Mức độ: Rất dễ 
> - Loại: Crypto 
> - Url: [Ancient Encodings](https://app.hackthebox.com/challenges/Ancient%2520Encodings)
> - Mô tả: Quy trình khởi tạo của bạn đòi hỏi phải nạp nhiều chương trình khác nhau để thu thập kiến ​​thức và kỹ năng cần thiết cho hành trình của mình. Nhiệm vụ đầu tiên của bạn là tìm hiểu các hệ thống mã hóa cổ xưa mà người ngoài hành tinh sử dụng trong giao tiếp.

> - Chương trình mã hóa có logic rất đơn giản 
> - Mã hóa base64 dữ liệu flag thành dạng hex và lưu vào `output.txt` 

```python 
from Crypto.Util.number import bytes_to_long
from base64 import b64encode
from secret import FLAG

def encode(message):
	return hex(bytes_to_long(b64encode(message)))

def main():
	encoded_flag = encode(FLAG)
	with open("output.txt", "w") as f:
		f.write(encoded_flag)

if __name__ == "__main__":
	main()
```

> - Tạo chương trình giải mã nhận vào chuỗi base64 đã mã hóa và giải mã 
> - Thu được flag `HTB{411_7h3_3nc0d1n9_423_h323_70_574y}` 

```python
import base64

encode_flag = "53465243657a51784d56383361444e664d32356a4d475178626a6c664e44497a5832677a4d6a4e664e7a42664e5463306558303d"

print(f"[+] Encode Flag: {encode_flag}")

raw_bytes = bytes.fromhex(encode_flag)

flag = base64.b64decode(raw_bytes).decode("utf-8")

print(f"Flag: {flag}")
```