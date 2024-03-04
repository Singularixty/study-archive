#include <stdio.h>
#include <string.h>

int main(){
    int num_1 = 2;
    int num_2 = 3;
    

    printf("Numbers: %d,%d\n", num_1, num_2);

    int temp_num = num_1;
    num_1 = num_2;
    num_2 = temp_num;

    printf("Numbers: %d,%d\n", num_1, num_2);

    getchar();
    return 0;
}