#include <iostream>

int main(){
    std::string minerals[][3] = {
        {"Coal", "Gold", "Iron"},
        {"Diamond","Emerld", "Sapphire"}
    };

    int rows = sizeof(minerals)/sizeof(minerals[0]);
    int columns = sizeof(minerals[0])/sizeof(minerals[0][0]);

    std::cout << "#Rows: " << rows << '\n';
    std::cout << "#Columns: " << columns << '\n';

    for (int i = 0; i < rows; i++){
        for (int j = 0; j < columns; j++){
            std::cout << minerals[i][j] << ' ';
        }
        std::cout << '\n';
    }
    system("pause");
    return 0;
}