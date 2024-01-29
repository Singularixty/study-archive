#include <stdio.h>
#include <stdlib.h>

int main() {
    long long size_in_bytes = 2LL * 1024 * 1024 * 1024;

    void *ptr = malloc(size_in_bytes);

    if (ptr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    printf("Memory allocated successfully\n");

    free(ptr);
    system("pause");

    return 0;
}
