#include <stdio.h>

int calc(int a, int b){
    return a + b;
}

int main(){
    int result = calc(5, 3);
    printf("%d", result);
    return 0;
}