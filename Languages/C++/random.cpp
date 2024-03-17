#include <iostream>
#include <ctime>

int main(){
    srand(time(0));
    int randomNum = rand() % 5 + 1;
    switch(randomNum){
        case 1:
            std::cout << "You won a lottery\nNum is " << randomNum << '\n';
            break;
        case 2:
        case 3:
        case 4:
        case 5:
            std::cout << "You lost!\nNum is " << randomNum << '\n';
            break;
    }
    system("pause");
    return 0;
}