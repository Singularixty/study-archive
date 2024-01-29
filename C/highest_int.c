#include <stdio.h>

int main(){
    int num1;
    int num2;
    printf("Number 1: ");
    scanf("%d", &num1);
    printf("Number 2: ");
    scanf("%d", &num2);
    if (num1 > num2){
        printf("Number 1 is greater than 2!");
    }
    else if (num2 > num1){
        printf("Number 2 is greater than 1!\n");
    }
    else{
        printf("Those two numbers are equal!\n");
    }
    
    system("pause");
    return 0;
}