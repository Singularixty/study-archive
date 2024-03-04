#include <iostream>

void swap(std::string &x, std::string &y);

int main(){
    std::string var_x = "Varible_X";
    std::string var_y = "Variable_Y";
    swap(var_x, var_y);

    std::cout << "X: " << var_x << '\n';
    std::cout << "Y: " << var_y << '\n';

    system("pause");
    return 0;
}


void swap(std::string &x, std::string &y){
    std::string temp;
    temp = x;
    x = y;
    y = temp;
}