> [!NOTE]
> - Mức độ: Rất dễ 
> - Loại: Reversing
> - Url: [CryptOfTheUndead](https://app.hackthebox.com/challenges/CryptOfTheUndead)
> - Mô tả: Tất cả các tệp tin quan trọng của tôi đã bị biến thành "thây ma" bởi băng nhóm tội phạm mạng khét tiếng Zombie. Bạn có thể giúp chúng được yên nghỉ và khôi phục lại các tệp tin của tôi không?

> - Hàm ends_with() nhận 2 chuỗi đầu vào param_1, param_2 
> - Kiểm tra xem param1 có kết thúc bằng param_2 không 
> - Nếu param_1 kết thúc bằng param_2 trả về true nếu không trả về false  

```c
bool ends_with(char *param_1,char *param_2)
{
	int iVar1;
	size_t sVar2;
	size_t __n;
	bool bVar3;
	
	sVar2 = strlen(param_1);
	__n = strlen(param_2);
	bVar3 = false;
	if (__n <= sVar2) {
		iVar1 = strncmp(param_1 + (sVar2 - __n),param_2,__n);
		bVar3 = iVar1 == 0;
	}
	return bVar3;
}
```

```c
int read_file(char *param_1,long *param_2,undefined8 *param_3)

{
  int __fd;
  void *__ptr;
  ssize_t sVar1;
  long lVar2;
  size_t __size;
  int iVar3;
  
  __fd = open(param_1,0);
  iVar3 = __fd;
  if (-1 < __fd) {
    __size = 0x400;
    lVar2 = 0;
    __ptr = malloc(0x400);
    do {
      sVar1 = read(__fd,(void *)((long)__ptr + lVar2),__size - lVar2);
      if (sVar1 < 0) {
        close(__fd);
        free(__ptr);
        return (int)sVar1;
      }
      lVar2 = lVar2 + sVar1;
      if (sVar1 == 0) {
        close(__fd);
        *param_3 = __ptr;
        *param_2 = lVar2;
        return 0;
      }
      __size = __size + 0x400;
      __ptr = realloc(__ptr,__size);
    } while (__ptr != (void *)0x0);
    iVar3 = 1;
    close(__fd);
  }
  return iVar3;
}
```

> - Hàm này nhận vào dữ liệu đã mã hóa(param_2) , kích thước dữ liệu(param_1) và khóa(param_3) 
> - Duwx liệu mã hóa dùng thuật toán ChaCha20 để mã hóa 

```c
void encrypt_buf(undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long in_FS_OFFSET;
  undefined1 auStack_f8 [204];
  undefined8 local_2c;
  undefined4 local_24;
  long local_20;
  
  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  local_2c = 0;
  local_24 = 0;
  chacha20_init_context(auStack_f8,param_3,&local_2c,0);
  chacha20_xor(auStack_f8,param_1,param_2);
  if (local_20 == *(long *)(in_FS_OFFSET + 0x28)) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}
```

> - Chương trình nhận vào tên 1 file không có đuôi `.undead` nếu không trả về lỗi 
> - Sau đó đọc file đó giải mã dữ liệu theo thuật toán ChaCha20 , thuật toán này có tính chất 2 chiều nên có thể chạy lại để giải mã dữ liệu 
> - Đổi tên file đầu vào và ghi dữ liệu vào file đó 

```c

undefined4 main(int param_1,undefined8 *param_2)

{
  int iVar1;
  size_t sVar2;
  char *__dest;
  char *pcVar3;
  undefined4 uVar4;
  long in_FS_OFFSET;
  void *local_40;
  size_t local_38;
  long local_30;
  
  local_30 = *(long *)(in_FS_OFFSET + 0x28);
  
  // Kiểm tra chương trình gồm 1 tham số đầu vào là tên file 
  if (param_1 < 2) {
    pcVar3 = "crypt";
    if (param_1 == 1) {
      pcVar3 = (char *)*param_2;
    }
    uVar4 = 1;
    printf("Usage: %s file_to_encrypt\n",pcVar3);
  }
  else {
	//Lấy tên file được truyền vào, kiểm tra xem tên file có kết thúc bằng '.undead' không nếu không mới xủ lý tiếp 
    pcVar3 = (char *)param_2[1];
    iVar1 = ends_with(pcVar3,".undead");
    if (iVar1 == 0) {// Tên file được truyền vào không kết thúc bởi '.undead'
      
      //Tạo 1 vùng nhớ dùng có độ dài là độ dài tên file + 9 để lưu tên file chỉ cần +8 (cho .undead và 1 byte \0) nhưng không hiểu sao +9  
      sVar2 = strlen(pcVar3);
      __dest = malloc(sVar2 + 9);
      strncpy(__dest,pcVar3,sVar2 + 9);
      //Nối thêm '.undead' vào cuối tên chuỗi đầu vào 
      sVar2 = strlen(__dest);
      builtin_strncpy(__dest + sVar2,".undead",8);
      
      #Đọc dữ liệu từ file đầu vào vào local38 với kích thước local40
      iVar1 = read_file(pcVar3,&local_38,&local_40);
      if (iVar1 == 0) {//Nếu hàm đọc file trả về 0 là đọc thành công 
	    //Giải mã dữ liệu mã hóa ChaCha20 với khóa `BRAAAAAAAAAAAAAAAAAAAAAAAAAINS!!`
        encrypt_buf(local_40,local_38,"BRAAAAAAAAAAAAAAAAAAAAAAAAAINS!!");
        //Đổi tên file đầu vào thành tên file + ".undead"
        iVar1 = rename(pcVar3,__dest);
        //Mở file đã đổi tên và ghi dữ liệu đã giải mã vào file 
        if (iVar1 == 0) {
          iVar1 = open(__dest,0x201);
          if (iVar1 < 0) {
            uVar4 = 5;
            perror("error opening new file");
          }
          else {
            write(iVar1,local_40,local_38);
            close(iVar1);
            puts("successfully zombified your file!");
            uVar4 = 0;
          }
        }
        else {
          uVar4 = 4;
          perror("error renaming file");
        }
      }
      else {
        uVar4 = 3;
        perror("error reading file");
      }
    }
    else {
      uVar4 = 2;
      puts("error: that which is undead may not be encrypted");
    }
  }
  if (local_30 == *(long *)(in_FS_OFFSET + 0x28)) {
    return uVar4;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}
```


> - Do có tính 2 chiều nên nếu chạy lại chương trình sẽ lấy được thông tin gốc 
> - Đổi tên file `fla.txt.undead` thành `flag.txt` hoặc tên bất kì không kết thúc bằng `.undead`
> - Chạy chương trình thu được flag 

```shell
❯ ./crypt flag.txt           
successfully zombified your file!
❯ cat flag.txt.undead 
HTB{und01ng_th3_curs3_0f_und34th}
```
