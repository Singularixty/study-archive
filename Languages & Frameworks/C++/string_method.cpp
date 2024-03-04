#include <iostream>

int main(){
    std::string username;
    std::cout << "Your mail address?: ";
    std::cin >> username;
    if (username.empty()){
        std::cout << "Empty string";
    }
    else if (username.length() > 20){
        std::cout << "Too long username";
    }
    else{
        username.append("@gmail.com");
        std::cout << "\nYour email: " << username << '\n';
    }
    system("pause");
    return 0;
}