#include "header.h"
#include <iostream>
#include <string> 

void bubblesort(int Array[], int ArraySize) {
    int temp;
    for (int i = 0; i < ArraySize - 1; i++){
        for (int j = 0; j < ArraySize - i - 1; j++){
            if (Array[j] > Array[j + 1]){
                temp = Array[j];
                Array[j] = Array[j+1];
                Array[j+1] = temp;
            }
        }
    }
}