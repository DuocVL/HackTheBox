> [!NOTE]
> - Mức độ: Rất dễ 
> - Loại: Reversing
> - Mô tả: Sâu trong một ngôi mộ cổ, bạn tìm thấy một phiến đá chứa thông tin bí mật về vị trí của những di vật khác. Thế nhưng, trong lúc né tránh một mũi tên tẩm độc, phiến đá đã tuột khỏi tay bạn và vỡ tan thành hàng trăm mảnh. Liệu bạn có thể ghép nó lại như cũ để đọc được các manh mối đó không?

> - Chương trình nhận đầu vào của người dùng và kiểm tra đầu vào từ đó in ra kết quả 
> - Logic kiểm tra đầu vào được làm rối gây khó khăn cho gỡ lỗi 

```c

undefined8 main(void)

{
  char local_48 [64];
  
  local_48[0] = '\0';
  local_48[1] = '\0';
  local_48[2] = '\0';
  local_48[3] = '\0';
  local_48[4] = '\0';
  local_48[5] = '\0';
  local_48[6] = '\0';
  local_48[7] = '\0';
  local_48[8] = '\0';
  local_48[9] = '\0';
  local_48[10] = '\0';
  local_48[0xb] = '\0';
  local_48[0xc] = '\0';
  local_48[0xd] = '\0';
  local_48[0xe] = '\0';
  local_48[0xf] = '\0';
  local_48[0x10] = '\0';
  local_48[0x11] = '\0';
  local_48[0x12] = '\0';
  local_48[0x13] = '\0';
  local_48[0x14] = '\0';
  local_48[0x15] = '\0';
  local_48[0x16] = '\0';
  local_48[0x17] = '\0';
  local_48[0x18] = '\0';
  local_48[0x19] = '\0';
  local_48[0x1a] = '\0';
  local_48[0x1b] = '\0';
  local_48[0x1c] = '\0';
  local_48[0x1d] = '\0';
  local_48[0x1e] = '\0';
  local_48[0x1f] = '\0';
  local_48[0x20] = '\0';
  local_48[0x21] = '\0';
  local_48[0x22] = '\0';
  local_48[0x23] = '\0';
  local_48[0x24] = '\0';
  local_48[0x25] = '\0';
  local_48[0x26] = '\0';
  local_48[0x27] = '\0';
  local_48[0x28] = '\0';
  local_48[0x29] = '\0';
  local_48[0x2a] = '\0';
  local_48[0x2b] = '\0';
  local_48[0x2c] = '\0';
  local_48[0x2d] = '\0';
  local_48[0x2e] = '\0';
  local_48[0x2f] = '\0';
  local_48[0x30] = '\0';
  local_48[0x31] = '\0';
  local_48[0x32] = '\0';
  local_48[0x33] = '\0';
  local_48[0x34] = '\0';
  local_48[0x35] = '\0';
  local_48[0x36] = '\0';
  local_48[0x37] = '\0';
  local_48[0x38] = '\0';
  local_48[0x39] = '\0';
  local_48[0x3a] = '\0';
  local_48[0x3b] = '\0';
  local_48[0x3c] = '\0';
  local_48[0x3d] = '\0';
  local_48[0x3e] = '\0';
  local_48[0x3f] = '\0';
  printf("Hmmmm... I think the tablet says: ");
  fgets(local_48,0x40,stdin);
  if (((((local_48[0x22] == '4') && (local_48[0x14] == '3')) && (local_48[0x24] == 'r')) &&
      ((((local_48[1] == 'T' && (local_48[0x15] == 'v')) &&
        ((local_48[6] == '0' && ((local_48[0x27] == '}' && (local_48[0x26] == 'd')))))) &&
       (local_48[0x1f] == 'r')))) &&
     ((((((local_48[0x1d] == '3' && (local_48[8] == '3')) && (local_48[0x16] == 'e')) &&
        ((local_48[0x23] == '1' && (local_48[5] == 'r')))) &&
       ((local_48[0] == 'H' && ((local_48[0x20] == '3' && (local_48[0x12] == '.')))))) &&
      (((((local_48[0xd] == '4' &&
          (((((local_48[3] == '{' && (local_48[10] == '_')) && (local_48[0x10] == '.')) &&
            ((local_48[4] == 'b' && (local_48[7] == 'k')))) && (local_48[0xf] == 't')))) &&
         (((local_48[0xe] == 'r' && (local_48[0x13] == 'n')) &&
          ((local_48[0x19] == 't' &&
           (((local_48[0x11] == '.' && (local_48[9] == 'n')) && (local_48[0x1e] == '_')))))))) &&
        (((local_48[0x1a] == '0' && (local_48[0x18] == '_')) && (local_48[0xc] == 'p')))) &&
       ((((local_48[0x17] == 'r' && (local_48[0x1c] == 'b')) &&
         ((local_48[0x21] == 'p' &&
          (((local_48[2] == 'B' && (local_48[0x1b] == '_')) && (local_48[0xb] == '4')))))) &&
        (local_48[0x25] == '3')))))))) {
    puts("Yes! That\'s right!");
  }
  else {
    puts("No... not that");
  }
  return 0;
}
```

> - Viết lại mã ta thu được flag 
```c 
undefined8 main(void)

  char local_48[64] = {0};
  
  printf("Hmmmm... I think the tablet says: ");
  fgets(local_48,0x40,stdin);
  char *flag = "HTB{br0k3n_4p4rt...n3ver_t0_b3_r3p41r3d}"
  
  if (strcmp(local_48, flag) == 0)
    puts("Yes! That\'s right!");
  }
  else {
    puts("No... not that");
  }
  return 0;
}
```

```shell 
❯ ./tablet                               
Hmmmm... I think the tablet says: HTB{br0k3n_4p4rt...n3ver_t0_b3_r3p41r3d}
Yes! That's right!
```