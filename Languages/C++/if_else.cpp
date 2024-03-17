#include <iostream>

int main(){
    int age;
    std::cout << "What's your age: ";
    std::cin >> age;
    if (age > 18 && age < 100){
        std::cout << '\n' << "Welcome to age-restricted site!\n";
    }
    else{
        std::cout << '\n' << "You are not allowed to enter this site\n";
    }
    system("pause");
    return 0;
}