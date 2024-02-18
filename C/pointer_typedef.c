#include <stdio.h>

typedef float MyFloat;
typedef float* FloatPtr;

int main(){
    MyFloat money = 100.24;
    FloatPtr Pointer_1 = &money;
    printf("Your wallet: $%.2f\n", *Pointer_1);
    system("pause");
    return 0;
}