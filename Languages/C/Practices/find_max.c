#include <stdio.h>

int FindMaxNum(int num1, int num2){
    return (num1 > num2) ? num1 : num2;
}
int main(){
    int max = FindMaxNum(1, 2);
    printf("%d", max);

    return 0;
}