#include <stdio.h>
#include <float.h>

int main() {
    printf("Float minimum positive value: %e\n", FLT_MIN);
    printf("Float maximum value: %e\n", FLT_MAX);
    printf("Float epsilon: %e\n", FLT_EPSILON);
    printf("Number of decimal digits of precision: %d\n", FLT_DIG);
    return 0;
}
