#include <iostream>

int main(){
    const int ARRAY_SIZE = 100;
    std::string foods[ARRAY_SIZE];
    fill(foods, foods + (ARRAY_SIZE/3), "Pizza");
    fill(foods + (ARRAY_SIZE/3), foods + (ARRAY_SIZE/3)*2, "Hamburger");
    fill(foods + (ARRAY_SIZE/3)*2, foods + ARRAY_SIZE, "Hotdog");
    for (std::string food : foods){
        std::cout << food << '\n';
    }
    system("pause");
    return 0;
}