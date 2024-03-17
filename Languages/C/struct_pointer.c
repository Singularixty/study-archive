#include <stdio.h>
typedef struct Player{
    char *name;
    float hp;
} player;

int main(){
    player NewPlayer = {.name = "Singularixty", .hp = 40};
    player *PlayerPointer = &NewPlayer;
    printf("%s has %.1lfHP", PlayerPointer->name, PlayerPointer->hp);
    return 0;
}