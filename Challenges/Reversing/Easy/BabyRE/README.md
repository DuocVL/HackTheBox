> [!NOTE]
> - Mức độ: Easy
> - Loại: Reversing
> - Url: [Baby RE](https://app.hackthebox.com/challenges/Baby%2520RE)
> - Mô tả: Hãy cho chúng tôi thấy các kỹ năng cơ bản của bạn! (Tái bút: Có 4 cách để giải bài này, bạn có sẵn lòng thử hết cả 4 cách không?)

> - Xác định loại file đây là file ELF
> - Chưa xóa thông tin gỡ lồi (not stripped)

```shell
❯ file baby 
baby: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=25adc53b89f781335a27bf1b81f5c4cb74581022, for GNU/Linux 3.2.0, not stripped
```

> - Decompiler banwgf Ghidra 
> - Yêu cầu người dùng nhập thông tin xác thực `abcde122313` nếu chính xác in ra flag `HTB{B4BY_R3V_TH4TS_EZ}`

```c
undefined8 main(void)

{
  int iVar1;
  char local_48 [32];
  char local_28 [24];
  char *local_10;
  
  local_10 = "Dont run `strings` on this challenge, that is not the way!!!!";
  puts("Insert key: ");
  fgets(local_28,0x14,stdin);
  iVar1 = strcmp(local_28,"abcde122313\n");
  if (iVar1 == 0) {
    builtin_strncpy(local_48,"HTB{B4BY_R3V_TH4TS_EZ}",0x16);
    puts(local_48);
  }
  else {
    puts("Try again later.");
  }
  return 0;
}
```

```shell
❯ ./baby
Insert key: 
abcde122313
HTB{B4BY_R3V_TH4TS_EZ}
```