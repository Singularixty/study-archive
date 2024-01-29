#include <stdio.h>

struct Player {
    char name[20];
    int score;
    int health;
    int level;
};

void PlayerInfo(struct Player player) {
    printf("Player Information:\n");
    printf("Name: %s\n", player.name);
    printf("Score: %d\n", player.score);
    printf("Health: %d\n", player.health);
    printf("Level: %d\n", player.level);
    printf("\n");
}

int main() {
    struct Player player1 = {"Singularixty", 100, 90, 1};
    struct Player player2 = {"ProMasterGG", 150, 80, 2};
    PlayerInfo(player1);
    PlayerInfo(player2);
    getchar();
    return 0;
}
