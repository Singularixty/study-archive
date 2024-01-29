#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    srand(time(0));
    int num_1 = (rand() % 6 + 1);
    int num_2 = (rand() % 6 + 1);
    int num_3 = (rand() % 6 + 1);
    printf("%d\n", num_1);
    printf("%d\n", num_2);
    printf("%d\n", num_3);
    getchar();
    return 0;
}