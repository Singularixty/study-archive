#include <stdio.h>
#include <string.h>

int main(){
    char fruits[][10] = {"Apple", "Banana","Guava"};
    strcpy(fruits[0], "Pineapple");

    int array_size = sizeof(fruits);
    int array_mem_size = sizeof(fruits[0]);

    printf("Array Size: %d, Member Size: %d\n", array_size, array_mem_size);

    for (int i = 0; i < sizeof(fruits)/sizeof(fruits[0]); i++){
        printf("%s\n", fruits[i]);
    }

    getchar();
    return 0;
}