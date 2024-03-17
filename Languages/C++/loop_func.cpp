#include <iostream>

void say(std::string message){
    std::cout << message << '\n';
}

int main(){
    std::string input;
    std::cout << "What do you want to announce?: ";
    std::cin >> input;
    for (int i = 1; i < 10; i++){
        say(input);
    }
    system("pause");
    return 0;
}