#include <iostream>

namespace first{
    int g = 20;
}

int main(){
    int g = 12;
    std::cout << "Local Scope:" << g << '\n';
    std::cout << "First Namespace:" << first::g << '\n';
    system("pause");
    return 0;
}