#include <iostream>

int main(){
    std::string names[] = {"Patrick", "Spongbob"};
    for (std::string name : names){
        std::cout << name << '\n';
    }
    std::cout << '\n';
    system("pause");
    return 0;
}