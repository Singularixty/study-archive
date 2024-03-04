#include <iostream>

typedef std::string MyVariable;

using Age_t = int;

int main() {
    MyVariable myVar = "HELLO";
    Age_t age = 15;
    std::cout << myVar << '\n' << age << " years old" << '\n';
    system("pause");
    return 0;
}
