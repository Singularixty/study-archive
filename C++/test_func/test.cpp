#include "header.h"
#include <iostream>

int main() {
    int arrays[] = {1, 3, 2, 9, 4, 6, 7, 8, 5, 10};
    int size = sizeof(arrays)/sizeof(arrays[0]);
    bubblesort(arrays, size);
    for (int array : arrays){
        std::cout << array << ' ';
    }
    system("pause");
    return 0;
}