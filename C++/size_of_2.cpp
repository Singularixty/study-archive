#include <iostream>

int main(){
    std::string students[] = {"Singularity", "Singularixty"};
    std::cout << "Total Elements:" << sizeof(students)/sizeof(std::string);
    system("pause");
    return 0;
}