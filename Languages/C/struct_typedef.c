#include <stdio.h>

typedef struct{
    char *name;
    long long int money;
} Player;

int main(){
    Player Player1;
    Player1.name = "Singularixty";
    Player1.money = 20002523249;
    printf("%s has $%lld\n", Player1.name, Player1.money);
    return 0;
}