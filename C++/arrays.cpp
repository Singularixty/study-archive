#include <iostream>

int main(){
    std::string cars[] = {"Mustan", "Tesla"};
    cars[2] = "NewCar";
    std::cout << cars[0] << '\n';
    std::cout << cars[1] << '\n';
    std::cout << cars[2] << '\n';
    system("pause");
    return 0;
}