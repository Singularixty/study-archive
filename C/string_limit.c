#include <stdio.h>
#include <string.h>

int main() {
    char buffer[20];
    printf("Please declare a name of food (up to 20 characters): ");
    fgets(buffer, sizeof(buffer), stdin);
    if (strlen(buffer) >= 19 && buffer[18] != '\n') {
        printf("Buffer exceeded character limit.\n");
    } else {
        printf("Enjoy your %s\n", buffer);
    }
    return 0;
}
