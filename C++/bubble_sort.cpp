#include <iostream>
void bubble_sort(int unsorted_array[], int unsorted_array_size);

int main(){
    int unsorted_array[] = {1, 3, 2, 9, 4, 6, 7, 8, 5, 10};
    int unsorted_array_size =  sizeof(unsorted_array)/sizeof(unsorted_array[0]);
    bubble_sort(unsorted_array, unsorted_array_size);
    for (int unsorted_array_element : unsorted_array){
        std::cout << unsorted_array_element << ' ';
    }
    system("pause");
    return 0;
}

void bubble_sort(std::string unsorted_array[], int unsorted_array_size){
    int temp;
    for (int i = 0; i < unsorted_array_size - 1; i++){
        for (int j = 0; j < unsorted_array_size - i - 1; j++){
            if (unsorted_array[j] > unsorted_array[j + 1]){
                temp = unsorted_array[j];
                unsorted_array[j] = unsorted_array[j+1];
                unsorted_array[j+1] = temp;
            }
        }
    }
}
