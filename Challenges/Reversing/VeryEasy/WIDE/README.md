> [!NOTE]
> - Mức độ: Rất dễ 
> - Loại: Reverse 
> - Mô tả: Chúng tôi nhận được thông tin rằng Draeger đã cất giấu một kho vũ khí khổng lồ trong chiều không gian bỏ túi có tên là Flaggle Alpha. Bạn đã xoay xở lấy được một thiết bị truy cập (vốn đã bị loại bỏ) dùng cho công cụ "Trình chỉnh sửa chiều không gian mở rộng" (Widely Inflated Dimension Editor) từ tổng hành dinh của hắn, nhưng mục dữ liệu về chiều không gian này lại đang bị mã hóa. Liệu bạn có thể thâm nhập vào bên trong và giành quyền kiểm soát nó không?

# Static analyst

> - Dùng Ghidra dịch ngược mã nguồn được hàm main()
> - Đọc file `db.ex` chia thành từng khối dữ liệu 
> - In ra tùy chọn để người dùng chọn in ra nội dung tương ứng 

```c
undefined8 main(int param_1,undefined8 *param_2)

{
  int iVar1;
  FILE *__stream;
  ulong uVar2;
  void *__ptr;
  uint uVar3;
  int local_28;
  
  // Kiểm tra số lượng tham số đầu vào dạng ./wide file_name
  if (param_1 < 2) {
    printf("Usage: %s db.ex\n",*param_2);
                    /* WARNING: Subroutine does not return */
    exit(-1);
  }
  puts("[*] Welcome user: kr4eq4L2$12xb, to the Widely Inflated Dimension Editor [*]");
  puts("[*]    Serving your pocket dimension storage needs since 14,012.5 B      [*]");
	//Mở file chế độ đọc file name là tham số truyền vào 
  __stream = fopen((char *)param_2[1],"r");
  if (__stream == (FILE *)0x0) {// Kiểm tra lỗi mở file 
    puts("[x] There was a problem accessing your database [x]");
                    /* WARNING: Subroutine does not return */
    exit(-1);
  }
  //Di chuyển con trỏ file về cuối tệp để  tính kích thước file theo byte
  fseek(__stream,0,2);// Di chuyển con trỏ về cuối file 
  uVar2 = ftell(__stream);//Tính độ lệch so với đầu file 

  fseek(__stream,0,0);// Di chuyển con trỏ file lại về đầu 
  uVar2 = (uVar2 - uVar2 % 0xb4) / 0xb4;// Tính số khối byte có kích thước 180
  iVar1 = (int)uVar2;
  
  __ptr = calloc((long)iVar1,0xb4);//Cấp phát bộ nhớ với số phần tử là iVar1, mỗi phần tử 180 byte 
  fread(__ptr,0xb4,(long)iVar1,__stream);// Đọc file và ghi vào phần bộ nhớ vừa cấp phát 
  fclose(__stream);
  
  puts("[*]                       Displaying Dimensions....                      [*]");
  puts("[*]       Name       |              Code                |   Encrypted    [*]");
  
  // In ra các khối dữ liệu trong file 
  for (local_28 = 0; local_28 < iVar1; local_28 = local_28 + 1) {
    if (*(int *)((long)__ptr + (long)local_28 * 0xb4) == 0) {
      uVar3 = 0x20;
    }
    else {
      uVar3 = 0x2a;
    }
    printf("[X] %-16s | %-32s | %6s%c%7s [*]\n",(long)__ptr + (long)local_28 * 0xb4 + 4,
           (long)__ptr + (long)local_28 * 0xb4 + 0x14,&DAT_0010132d,(ulong)uVar3,&DAT_0010132d);
  }
  // Gọi hàm menu() với con trỏ đến bộ nhớ cấp phát và số khối dữ liệu (&ffffffff số nguyên)
  menu(__ptr,uVar2 & 0xffffffff);
  return 0;
}
```

> - Xác định xem có bao nhiêu khối dữ liệu 180 byte trong file `db.ex` có 7 khối dữ liệu 
```shell
❯ ls -al db.ex 
-rw-r--r-- 1 cachyos cachyos 1260 24 Thg 5   2022 db.ex
❯ python3
Python 3.14.8 (main, Oct 13 2026, 10:33:10) [GCC 16.2.1 20260810] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(1260 // 180)
7
```

> - Hàm menu() nhận dữ liệu tùy chọn người dùng và in ra kết quả 
> - Có tùy chọn số 6 tùy chọn in khối dữ liệu cuối yêu cầu nhập thông tin xác thực nếu chính xác in ra flag 

```c
void menu(long param_1,int param_2)

{
  int iVar1;
  long lVar2;
  undefined8 *puVar3;
  long in_FS_OFFSET;
  uint local_1d4;
  wchar_t local_1c8 [16];
  undefined8 local_188;
  undefined8 local_180;
  undefined8 local_178;
  undefined8 local_170;
  undefined8 local_168;
  undefined8 local_160;
  undefined4 local_158;
  undefined4 uStack_154;
  undefined4 local_150;
  undefined4 uStack_14c;
  undefined4 local_148;
  undefined4 uStack_144;
  undefined4 local_140;
  undefined4 uStack_13c;
  undefined4 local_138;
  undefined4 uStack_134;
  undefined4 local_130;
  undefined4 uStack_12c;
  undefined4 local_128;
  undefined4 uStack_124;
  undefined4 local_120;
  undefined4 uStack_11c;
  undefined4 local_118;
  undefined4 uStack_114;
  undefined4 local_110;
  undefined4 uStack_10c;
  undefined4 local_108;
  undefined4 uStack_104;
  undefined4 local_100;
  undefined4 uStack_fc;
  undefined4 local_f8;
  undefined4 uStack_f4;
  undefined4 local_f0;
  undefined4 uStack_ec;
  undefined4 local_e8;
  undefined4 uStack_e4;
  undefined4 local_e0;
  undefined4 uStack_dc;
  undefined4 local_d8;
  char local_c8 [16];
  char local_b8 [32];
  undefined8 local_98;
  undefined8 local_90;
  undefined8 local_88;
  undefined8 local_80;
  undefined8 local_78;
  undefined8 local_70;
  undefined8 local_68;
  undefined8 local_60;
  undefined8 local_58;
  undefined8 local_50;
  undefined8 local_48;
  undefined8 local_40;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  undefined8 local_10;
  
  local_10 = *(undefined8 *)(in_FS_OFFSET + 0x28);
  local_b8[0] = '\0';
  local_b8[1] = '\0';
  local_b8[2] = '\0';
  local_b8[3] = '\0';
  local_b8[4] = '\0';
  local_b8[5] = '\0';
  local_b8[6] = '\0';
  local_b8[7] = '\0';
  local_b8[8] = '\0';
  local_b8[9] = '\0';
  local_b8[10] = '\0';
  local_b8[0xb] = '\0';
  local_b8[0xc] = '\0';
  local_b8[0xd] = '\0';
  local_b8[0xe] = '\0';
  local_b8[0xf] = '\0';
  local_b8[0x10] = '\0';
  local_b8[0x11] = '\0';
  local_b8[0x12] = '\0';
  local_b8[0x13] = '\0';
  local_b8[0x14] = '\0';
  local_b8[0x15] = '\0';
  local_b8[0x16] = '\0';
  local_b8[0x17] = '\0';
  local_b8[0x18] = '\0';
  local_b8[0x19] = '\0';
  local_b8[0x1a] = '\0';
  local_b8[0x1b] = '\0';
  local_b8[0x1c] = '\0';
  local_b8[0x1d] = '\0';
  local_b8[0x1e] = '\0';
  local_b8[0x1f] = '\0';
  do {
    while( true ) {
	  //Vòng lặp nhận đầu vào từ người dùng từ đó in ra nội dung tương ứng đảm bảo < số khối 180 byte (7) nên đầu vào 0-6
      while( true ) {
        printf("Which dimension would you like to examine? ");
        fgets(local_b8,0x20,stdin);
        lVar2 = strtol(local_b8,(char **)0x0,10);
        iVar1 = (int)lVar2;
        if ((-1 < iVar1) && (iVar1 < param_2)) break;
        puts("That option was invalid.");
      }
      puVar3 = (undefined8 *)(param_1 + (long)iVar1 * 0xb4);
      local_188 = *puVar3;
      local_180 = puVar3[1];
      local_178 = puVar3[2];
      local_170 = puVar3[3];
      local_168 = puVar3[4];
      local_160 = puVar3[5];
      local_158 = (undefined4)puVar3[6];
      uStack_154 = (undefined4)((ulong)puVar3[6] >> 0x20);
      local_150 = (undefined4)puVar3[7];
      uStack_14c = (undefined4)((ulong)puVar3[7] >> 0x20);
      local_148 = (undefined4)puVar3[8];
      uStack_144 = (undefined4)((ulong)puVar3[8] >> 0x20);
      local_140 = (undefined4)puVar3[9];
      uStack_13c = (undefined4)((ulong)puVar3[9] >> 0x20);
      local_138 = (undefined4)puVar3[10];
      uStack_134 = (undefined4)((ulong)puVar3[10] >> 0x20);
      local_130 = (undefined4)puVar3[0xb];
      uStack_12c = (undefined4)((ulong)puVar3[0xb] >> 0x20);
      local_128 = (undefined4)puVar3[0xc];
      uStack_124 = (undefined4)((ulong)puVar3[0xc] >> 0x20);
      local_120 = (undefined4)puVar3[0xd];
      uStack_11c = (undefined4)((ulong)puVar3[0xd] >> 0x20);
      local_118 = (undefined4)puVar3[0xe];
      uStack_114 = (undefined4)((ulong)puVar3[0xe] >> 0x20);
      local_110 = (undefined4)puVar3[0xf];
      uStack_10c = (undefined4)((ulong)puVar3[0xf] >> 0x20);
      local_108 = (undefined4)puVar3[0x10];
      uStack_104 = (undefined4)((ulong)puVar3[0x10] >> 0x20);
      local_100 = (undefined4)puVar3[0x11];
      uStack_fc = (undefined4)((ulong)puVar3[0x11] >> 0x20);
      local_f8 = (undefined4)puVar3[0x12];
      uStack_f4 = (undefined4)((ulong)puVar3[0x12] >> 0x20);
      local_f0 = (undefined4)puVar3[0x13];
      uStack_ec = (undefined4)((ulong)puVar3[0x13] >> 0x20);
      local_e8 = (undefined4)puVar3[0x14];
      uStack_e4 = (undefined4)((ulong)puVar3[0x14] >> 0x20);
      local_e0 = (undefined4)puVar3[0x15];
      uStack_dc = (undefined4)((ulong)puVar3[0x15] >> 0x20);
      local_d8 = *(undefined4 *)(puVar3 + 0x16);
      if ((int)local_188 != 0) break;
      puts((char *)&uStack_154);
    }
    local_98 = CONCAT44(local_150,uStack_154);
    local_90 = CONCAT44(local_148,uStack_14c);
    local_88 = CONCAT44(local_140,uStack_144);
    local_80 = CONCAT44(local_138,uStack_13c);
    local_78 = CONCAT44(local_130,uStack_134);
    local_70 = CONCAT44(local_128,uStack_12c);
    local_68 = CONCAT44(local_120,uStack_124);
    local_60 = CONCAT44(local_118,uStack_11c);
    local_58 = CONCAT44(local_110,uStack_114);
    local_50 = CONCAT44(local_108,uStack_10c);
    local_48 = CONCAT44(local_100,uStack_104);
    local_40 = CONCAT44(local_f8,uStack_fc);
    local_38 = CONCAT44(local_f0,uStack_f4);
    local_30 = CONCAT44(local_e8,uStack_ec);
    local_28 = CONCAT44(local_e0,uStack_e4);
    local_20 = CONCAT44(local_d8,uStack_dc);
    
    // Yêu cầu người dùng nhập thông tin xác thực `sup3rs3cr3tw1d3` nếu chính xác in ra flag 
    printf("[X] That entry is encrypted - please enter your WIDE decryption key: ");
    fgets(local_c8,0x10,stdin);
    mbstowcs(local_1c8,local_c8,0x10);
    iVar1 = wcscmp(local_1c8,L"sup3rs3cr3tw1d3");
    if (iVar1 == 0) {
      for (local_1d4 = 0;
          (local_1d4 < 0x80 && (*(char *)((long)&local_98 + (long)(int)local_1d4) != '\0'));
          local_1d4 = local_1d4 + 1) {
        *(byte *)((long)&local_98 + (long)(int)local_1d4) =
             *(byte *)((long)&local_98 + (long)(int)local_1d4) ^
             (char)(local_1d4 * 0x1b) + (char)((int)(local_1d4 * 0x1b) / 0xff);
      }
      puts((char *)&local_98);
    }
    else {
      puts("[X]                          Key was incorrect                           [X]");
    }
  } while( true );
}
```

```bash
❯ ./wide db.ex 
[*] Welcome user: kr4eq4L2$12xb, to the Widely Inflated Dimension Editor [*]
[*]    Serving your pocket dimension storage needs since 14,012.5 B      [*]
[*]                       Displaying Dimensions....                      [*]
[*]       Name       |              Code                |   Encrypted    [*]
[X] Primus           | people breathe variety practice  |                [*]
[X] Cheagaz          | scene control river importance   |                [*]
[X] Byenoovia        | fighting cast it parallel        |                [*]
[X] Cloteprea        | facing motor unusual heavy       |                [*]
[X] Maraqa           | stomach motion sale valuable     |                [*]
[X] Aidor            | feathers stream sides gate       |                [*]
[X] Flaggle Alpha    | admin secret power hidden        |       *        [*]
Which dimension would you like to examine? 0
Our home dimension
Which dimension would you like to examine? 1
The Ice Dimension
Which dimension would you like to examine? 2
The Berserk Dimension
Which dimension would you like to examine? 3
The Hungry Dimension
Which dimension would you like to examine? 4
The Water Dimension
Which dimension would you like to examine? 5
The Bone Dimension
Which dimension would you like to examine? 6
[X] That entry is encrypted - please enter your WIDE decryption key: sup3rs3cr3tw1d3
HTB{som3_str1ng5_4r3_w1d3}
```
