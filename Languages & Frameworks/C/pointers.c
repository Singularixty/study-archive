#include <stdio.h>

int main(){
    int age = 14;
    int *pAge = &age;

    printf("%d", *pAge);
    getchar();
    return 0;
}