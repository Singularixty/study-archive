#include <stdio.h>

int main(){
    int age = 14;
    int *PAge = &age;

    printf("%d", *PAge);
    return 0;
}