#include <stdio.h>
#include <string.h>
#include <stdbool.h>

struct Player
{
    char name[20];
    bool is_admin;
    int health;
    int max_health;
    int mana;
    int max_mana;
};

void heal(struct Player *player, int amount)
{
    if (player->is_admin) {
        player->health += amount;
    } else {
        player->health += amount;
        if (player->health > player->max_health) {
            player->health = player->max_health;
        }
    }
}

int main()
{
    struct Player player_1;
    struct Player player_2;

    // Player: Singularixty
    strcpy(player_1.name, "Singularixty");
    player_1.is_admin = true;
    player_1.health = 60;
    player_1.max_health = 100;
    player_1.mana = 50;
    player_1.max_mana = 100;

    // Player: RobloxMasterProXX
    strcpy(player_2.name, "RobloxMasterProXX");
    player_2.is_admin = false;
    player_2.health = 47;
    player_2.max_health = 100;
    player_2.mana = 51;
    player_2.max_mana = 100;

    printf("Player 1: %s, HP: %d/%d, Mana %d/%d\n", player_1.name, player_1.health, player_1.max_health, player_1.mana, player_1.max_mana);
    printf("Player 2: %s, HP: %d/%d, Mana %d/%d\n", player_2.name, player_2.health, player_2.max_health, player_2.mana, player_2.max_mana);

    heal(&player_1, 10);

    printf("Player 1 after healing: %s, HP: %d/%d, Mana %d/%d\n", player_1.name, player_1.health, player_1.max_health, player_1.mana, player_1.max_mana);

    getchar();
    return 0;
}
