#include <iostream>

int main(){
    std::string favorite_foods[3];
    int size = sizeof(favorite_foods)/sizeof(favorite_foods[0]);
    std::cout << "Please specify your top 3 favorite foods\n";

    for (int i = 0; i < size; i++){
        std::cout << "Enter Food #" << i+1 << " : ";
        std::getline(std::cin, favorite_foods[i]);
    }

    // disply

    for (std::string food : favorite_foods){
        std::cout << food << '\n';
    }
    system("pause");
    return 0;
}
