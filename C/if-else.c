#include <stdio.h>

int main() {
    int age;
    printf("Your age: ");

    if (scanf("%d", &age) != 1) {
        printf("Error: Invalid input. Please enter a valid age.\n");
        return 1;
    }

    if (age >= 18) {
        printf("You are allowed to drink.\n");
    } else {
        printf("You are not allowed to drink.\n");
    }

    return 0;
}