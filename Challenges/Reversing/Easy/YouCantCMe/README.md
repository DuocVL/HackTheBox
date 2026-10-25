> [!NOTE]
> - Mức độ: Easy 
> - Loại: Reversing 
> - Url: [You Cant C Me ](https://app.hackthebox.com/challenges/You%2520Cant%2520C%2520Me)

> - Hàm entry() là điểm khởi đầu khi chương trình chạy 
> - Hàm FUN_00401160() được gọi khi chương trình chạy

```c
void processEntry entry(undefined8 param_1,undefined8 param_2)

{
  undefined1 auStack_8[8];
__libc_start_main(FUN_00401160,param_2,&stack0x00000008,FUN_00401290,FUN_00401300,param_1,
                    auStack_8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```

> - Hàm `FUN_00401160()` yêu cầu nhập thông tin xác thực  
> - `builtin_strncpy(local_28,"this_is_the_password",0x15);` chỉ là code gây rối 
> - Thông tin xác thực được tạo bằng cách lập qua tất cả các kí tự trong chuỗi `m^&&fi\x17Uo&kUZ\'ZUYUc)` sau đó dịch chuyển các kí tự đó 10 kí tự trong bẳng mã ASCII `+ '\n` 
> - Flag được tạo từ chính thông tin xác thực đó 

```c
undefined4 FUN_00401160(void)

{
  int iVar1;
  char local_48 [24];
  char *local_30;
  char local_28 [24];
  int local_10;
  undefined4 local_c;
  
  local_c = 0;
  local_10 = 0;
  printf("Welcome!\n");
  
  builtin_strncpy(local_28,"this_is_the_password",0x15);
  
  local_30 = malloc(0x15);
  
  // Tạo thông tin xác thực 
  builtin_strncpy(local_48,"m^&&fi\x17Uo&kUZ\'ZUYUc)",0x14);
  for (local_10 = 0; local_10 < 0x14; local_10 = local_10 + 1) {
    local_28[local_10] = local_48[local_10] + '\n';
  }
  
  fgets(local_30,0x15,stdin);
  iVar1 = strcmp(local_28,local_30);
  if (iVar1 == 0) {
    printf("HTB{%s}\n",local_30);
  }
  else {
    printf("I said, you can\'t c me!\n");
  }
  return local_c;
}
```

> - Tạo chương trình thu được thông tin xác thực 

```python
s = "m^&&fi\x17Uo&kUZ\'ZUYUc)"
key = ""
for i in range(0, len(s)):
    key += chr(ord(s[i]) + ord('\n'))
print(key) 

wh00ps!_y0u_d1d_c_m3
```

```shell
❯ ./auth
Welcome!
wh00ps!_y0u_d1d_c_m3
HTB{wh00ps!_y0u_d1d_c_m3}
```