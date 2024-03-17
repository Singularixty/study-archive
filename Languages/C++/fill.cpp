#include <iostream>

int main(){
    const int ARRAY_SIZE = 100;
    int Dupe_Count = 0;
    std::string usernames[ARRAY_SIZE];
    fill(usernames, usernames + ARRAY_SIZE, "Singularixty");
    for (std::string username : usernames){
        std::cout << usernames << '\n';
    }
    system("pause");
    return 0;
}