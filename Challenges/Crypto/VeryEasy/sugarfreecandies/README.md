> [!NOTE]
> - Mức độ: Rất dễ 
> - Loại: Crypto
> - Url: [sugar free candies](https://app.hackthebox.com/challenges/sugar%2520free%2520candies)
> - Mô tả: Suốt nhiều năm, những tín hiệu kỳ lạ vẫn lan truyền trong không gian vào đêm trước ngày 31 tháng 10. Có người cho rằng đó là giọng nói của một mụ phù thủy cổ xưa, trong khi số khác lại tin rằng đó là thông điệp từ một thế lực tà ác hơn nhiều. Một thông điệp bí ẩn, chia thành ba phần, đã bị một nhóm dân làng gan dạ chặn được. Truyền thuyết kể về một thỏa thuận giữa mụ phù thủy và một nhân vật đầy bóng tối; thế nhưng, ý định thực sự đằng sau bí mật ấy chỉ có thể được hé lộ bởi những ai đủ dũng cảm để giải mã nó trước nửa đêm – thời điểm mà bức màn ngăn cách giữa các thế giới trở nên mỏng manh nhất.

> - Thuật toán mã hóa chia flag ra làm 3 phần 
> - Chuyển đổi các phần dữ liệu đó thành giá trị long 
> - Lưu các giá trị phương trình được tạo từ các mảnh flag 


```python
from Crypto.Util.number import bytes_to_long

FLAG = open("flag.txt", "rb").read()
step = len(FLAG) // 3
candies = [bytes_to_long(FLAG[i:i+step]) for i in range(0, len(FLAG), step)]

cnd1, cnd2, cnd3 = candies

with open('output.txt', 'w') as f:
	f.write(f'v1 = {cnd1**3 + cnd3**2 + cnd2}\n')
	f.write(f'v2 = {cnd2**3 + cnd1**2 + cnd3}\n')
	f.write(f'v3 = {cnd3**3 + cnd2**2 + cnd1}\n')
	f.write(f'v4 = {cnd1 + cnd2 + cnd3}\n')
```

```
v1 = 1181239096013650837744125294978177790419553719590172794906535790528758829840751110126012179328061375399196613652870424327167341710919767887891371258453
v2 = 2710472017687233737830986182523923794327361982506952801148259340657557362009893794103841036477555389231149721438246037558380601526471290201500759382599
v3 = 3448392481703214771250575110613977019995990789986191254013989726393898522179975576074870115491914882384518345287960772371387233225699632815814340359065
v4 = 396216122131701300135834622026808509913659513306193
```

> - Tạo chương trình giải hệ phương trình sử dụng thư viện `sympy` trong python
> - Đọc các giá trị phương trình trong python 
> - Tìm nghiệm hệ phương trình đó 
> - Ghép các mảnh flag thu được flag `HTB{solving_equations_for_parts_of_the_flag_over_the_integers!}`

```python
import sympy as sp

v = [0]
with open('output.txt', 'r') as f:
	for i in range(1,5):
		encrypt = f.readline()
		v.append(int(encrypt.split(' ')[2]))
		print(f"[+] v{i}: {v[i]}")
	f.close()

vo, v1, v2, v3, v4 = v
cnd1, cnd2, cnd3 = sp.symbols("cnd1 cnd2 cnd3")

eq1 = sp.Eq(cnd1**3 + cnd3**2 + cnd2, v1)
eq2 = sp.Eq(cnd2**3 + cnd1**2 + cnd3, v2)
eq3 = sp.Eq(cnd3**3 + cnd2**2 + cnd1, v3)
eq4 = sp.Eq(cnd1 + cnd2 + cnd3, v4)

solutions = sp.nonlinsolve([eq1, eq2, eq3, eq4], [cnd1, cnd2, cnd3])

cnd1, cnd2, cnd3 = map(int, next(iter(solutions)))

strbyte = (
cnd1.to_bytes((cnd1.bit_length() + 7) // 8, byteorder="big")
+ cnd2.to_bytes((cnd2.bit_length() + 7) // 8, byteorder="big")
+ cnd3.to_bytes((cnd3.bit_length() + 7) // 8, byteorder="big"))

flag = strbyte.decode('utf-8')
print(f"[+] Flag: {flag}")
```