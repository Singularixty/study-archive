#include <stdio.h>

double square(double num){
    double result = num * num;
    return result;
}

int main(){
    double num = square(3);
    printf("%f", num);
    getchar();
    return 0;
}