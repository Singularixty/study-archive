#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

void typeText(const char *text, int delay);

int main() {
    char username[30];
    char message[1000];
    int bond_with_brother = 0;
    bool setup_success = false;

    typeText("Welcome to Two Wolves of Horizon\n", 60);

    do {
        typeText("Please specify your username to play: ", 50);
        scanf("%s", username);

        if (strlen(username) > 20 || strlen(username) < 1) {
            setup_success = false;
            typeText("Sorry, your name must be between 1 and 20 characters. Please try again.\n", 50);
        } else {
            setup_success = true;
            sprintf(message, "Hello, %s!\n", username);
            typeText(message, 50);
            break;
        }

    } while (!setup_success);
    system("pause");
    return 0;
}

void typeText(const char *text, int delay) {
    while (*text) {
        putchar(*text);
        fflush(stdout);
        usleep(delay * 1000);
        text++;
    }
}
