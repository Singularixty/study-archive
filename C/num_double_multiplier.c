#include <stdio.h>

int main(){
    int num = 2;
    for (int i=1; i<10; i+=2){
        num *= i;
    }
    printf("Result is %d", num);
    getchar();
    return 0;
}