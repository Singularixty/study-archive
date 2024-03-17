#include <stdio.h>

struct Player{
    int Health;
    char *Name;
};

int main(){
    struct Player Player1;
    Player1.Name = "Singularixty";
    Player1.Health = 100;
    printf("Welcome to the town, %s!, Your health has been set to %dHP", Player1.Name, Player1.Health);
    return 0;
}