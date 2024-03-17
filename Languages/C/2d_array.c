#include <stdio.h>

int main(){
    char items[5][3][20] = {{"Ruler", "Rubber", "Pencil"},
                        {"Cellphone", "Smartphone", "Television"},
                        {"Bottle", "Cabinet", "Fridge"}};
    printf("%s", items[0][0]);
    for (int i = 0; i < sizeof(items)/sizeof(items[0]); i++){
        for (int j = 0; j < sizeof(items[0])/sizeof(items[0][0]); j++){
            printf("%s\n", items[i][j]);
        }
    }
    return 0;
}