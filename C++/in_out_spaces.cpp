#include <iostream>

int main(){
    std::string username;
    int age;
    std::cout << "What's your age: ";
    std::cin >> age;

    std::cout << "What's your full name?: ";
    std::getline(std::cin >> std::ws, username);
    
    std::cout << "Hello, " << username << ", You are " << age << " years old." << '\n';
    system("pause");
    return 0;
}