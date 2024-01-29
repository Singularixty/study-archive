#include <stdio.h>
#include <string.h>

int main() {
    char name[20];
    printf("Your Username: ");
    fgets(name, sizeof(name), stdin);

    size_t len = strlen(name);
    if (len > 0 && name[len - 1] == '\n') {
        name[len - 1] = '\0';
    }

    while (strlen(name) == 0) {
        printf("Please enter your username!\n");
        printf("Your Username: ");
        fgets(name, sizeof(name), stdin);

        len = strlen(name);
        if (len > 0 && name[len - 1] == '\n') {
            name[len - 1] = '\0';
        }
    }

    printf("Hello %s\n", name);
    getchar();

    return 0;
}
