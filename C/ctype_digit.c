#include <stdio.h>
#include <ctype.h>

int main() {
    char c[] = "hello8 world";
    int i, check;
    for (i = 0; c[i] != '\0'; i++) {
        check = isdigit(c[i]);
        if (check != 0) {
            printf("Character '%c' is a digit.\n", c[i]);
        } else {
            printf("Character '%c' is not a digit.\n", c[i]);
        }
    }
    return 0;
}
