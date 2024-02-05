#include <iostream>

int main(){
    int grade;
    std::cout << "Your grade: ";
    std::cin >> grade;
    grade >= 60 ? std::cout << "You pass!\n" : std::cout << "You failed!\n";
    system("pause");
    return 0;
}