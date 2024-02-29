#include <stdio.h>

typedef struct Player{
    char *name;
    float hp;
} player;

int main(){
    player new_player = {.name = "Singularixty", .hp = 100.00};
    player *ptr = &new_player;
    printf("Name: %s\nHP: %.2f", ptr->name, ptr->hp);
    return 0;
}