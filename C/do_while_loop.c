#include <stdio.h>
 
int main(){

    int number = 0;
    int sum = 0;

    do{
        printf("Enter your number (0 to stop): ");
        scanf("%d", &number);
        if (number == 0){
            break;
        }
        else if(number > 0){
            sum += number;
        }
    }while(number > 0);
    getchar();
    printf("sum: %d\n", sum);
    getchar();
    return 0;
}