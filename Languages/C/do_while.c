#include <stdio.h>

int main(){
    int n = 0;
    int last_n = 1000;
    do{
        n++;
        if (n % 2 == 0){
            printf("%d is even number\n", n);
        }
        else{
            printf("%d is odd number\n", n);
        }
    }while (n != last_n);
}