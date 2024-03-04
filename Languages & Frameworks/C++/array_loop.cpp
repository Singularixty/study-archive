#include <iostream>

int main(){
    std::string usernames[] = {"RobloxMaster", "FortnitePro"};
    std::cout << sizeof(usernames[0]) << "\n\n";

    std::string names[] = {"Patrick", "Johnson", "Michael", "NewName", "ZZZZZZ"};
    for (int i = 0; i < sizeof(names)/sizeof(std::string); i++){
        std::cout << "Size ->" << sizeof(names[i]);
        std::cout << " Loop #" << i << " " << names[i] << '\n';
    }
    std::cout << sizeof(names) << '\n';
    std::cout << "DONE" << '\n';
    system("pause");
    return 0;
}