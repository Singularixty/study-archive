#include <stdio.h>

void PrintOut(char *text);

int main() {
    PrintOut("Hello");
    return 0;
}

void PrintOut(char *text) {
    printf("%s", text);
}
