#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(void)
{
    FILE *f;
    uint32_t seed;
    long len;
    uint8_t *data;

    // Đọc flag.enc 
    f = fopen("flag.enc", "rb");

    if (f == NULL) {
        perror("flag.enc");
        return 1;
    }

    //4 byte đầu là seed 
    fread(&seed, sizeof(seed), 1, f);

    // Lấy kích thước encrypted data 
    fseek(f, 0, SEEK_END);
    len = ftell(f) - 4;
    fseek(f, 4, SEEK_SET);

    //đọc dữ liệu mã hóa
    data = malloc(len);
    fread(data, 1, len, f);

    fclose(f);

    printf("Seed: %u\n", seed);
    printf("Encrypted size: %ld bytes\n", len);

    srand(seed);

    for (long i = 0; i < len; i++) {
        int ran1 = rand();
        int ran2 = rand();
        ran2 &= 7;
        data[i] = (data[i] >> ran2) | (data[i] << (8 - ran2));
        data[i] ^= ran1;
    }
    //Pain text
    printf("\nDecrypted:\n");
    fwrite(data, 1, len, stdout);
    printf("\n");

    free(data);

    return 0;
}