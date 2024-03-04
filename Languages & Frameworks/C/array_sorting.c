#include <stdio.h>
#include <string.h>

void sort_array(int array[], int size){
    for (int i = 0; i < size - 1; i++){
        for (int k = 0; k < size - 1; k++){
            if (array[k] > array [k+1]){
                int temp = array[k];
                array[k] = array[k+1];
                array[k+1] = temp;
            }
        }
    }
}

void Print(int array[], int size){
    for(int i = 0; i < size; i++){
        printf("%d", array[i]);
        if (i != size - 1){
            printf(", ");
        }
        else{
            printf("\n");
        }
    }
}

int main(){
    int array[] = {2, 3, 5, 1, 5, 9, 7, 1, 5, 53, 21, 235};
    int size = sizeof(array)/sizeof(array[0]);
    sort_array(array, size);
    Print(array, size);
    getchar();
    return 0;
}