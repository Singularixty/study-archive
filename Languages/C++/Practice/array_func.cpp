#include <iostream>

double CalcTotal(double prices[], int size);

int main(){
    double prices[] = {15.20, 40.12, 42.62, 15.23};
    int size = sizeof(prices) / sizeof(double);
    double total = CalcTotal(prices, size);

    std::cout << "Total : $" << total << '\n';
    system("pause");
    return 0;
}

double CalcTotal(double prices[], int size){
    double total = 0;

    for (int i = 0; i < size; i++){
        total += prices[i];
    }
    return total;
}
