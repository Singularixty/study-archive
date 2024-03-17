#include <stdio.h>

int main(){
    double prices[] = {5.00, 2.13, 25.40};
    char currency = '$';

    for (int i = 1; i < sizeof(prices)/sizeof(prices[0]); i++){
        printf("%.2lf%c\n", prices[i], currency);
    }
    getchar();
    return 0;
}