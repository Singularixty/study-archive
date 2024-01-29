#include <stdio.h>

void SendHBD(int age, char name[]) {
    printf("You are %d years old now!\n", age);
    printf("%s, wish you have a good life!\n", name);
}

int main() {
    int age = 21;
    char name[] = "Singularixty";
    SendHBD(age, name);

    return 0;
}
