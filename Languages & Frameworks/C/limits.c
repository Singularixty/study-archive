#include <stdio.h>
#include <limits.h>

int main() {
    printf("Number of bits in a char: %d\n", CHAR_BIT);
    printf("Minimum value of a char: %d\n", SCHAR_MIN);
    printf("Maximum value of a char: %d\n", SCHAR_MAX);
    printf("Maximum value of an unsigned char: %u\n", UCHAR_MAX);
    printf("Minimum value of a short: %d\n", SHRT_MIN);
    printf("Maximum value of a short: %d\n", SHRT_MAX);
    printf("Maximum value of an unsigned short: %u\n", USHRT_MAX);
    printf("Minimum value of an int: %d\n", INT_MIN);
    printf("Maximum value of an int: %d\n", INT_MAX);
    printf("Maximum value of an unsigned int: %u\n", UINT_MAX);
    printf("Minimum value of a long: %ld\n", LONG_MIN);
    printf("Maximum value of a long: %ld\n", LONG_MAX);
    printf("Maximum value of an unsigned long: %lu\n", ULONG_MAX);
    return 0;
}
