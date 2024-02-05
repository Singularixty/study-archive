#include <iostream>

int main(){
    std::string name;
    std::cout << "What's your name?: ";
    std::cin >> name;
    std::cout << '\n' << "Hello!, " << name << '\n';
    system("pause");
    return 0;
}
