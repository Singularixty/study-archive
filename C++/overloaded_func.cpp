#include <iostream>

void BakeNewPizza();
void BakeNewPizza(std:: string topping);

int main(){
    std::string topping;
    std::cout << "Declare topping of pizza you want to eat: ";
    std::getline(std::cin, topping);
    if (topping.empty()){
        BakeNewPizza();
    }
    else{
        BakeNewPizza(topping);
    }
    
    system("pause");
    return 0;
}

void BakeNewPizza(){
    std::cout << "Baked pizza!\n";
}

void BakeNewPizza(std::string topping){
    std::cout << "Baked " << topping << " pizza!\n";
}