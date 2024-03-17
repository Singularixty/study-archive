#include <stdio.h>
#include <string.h>

int main(){
    char name[20];
    char buffer[200];
    printf("What's your name?: ");
    fgets(buffer, sizeof(buffer), stdin);
    strcpy(name, buffer);
    printf("%s", name);
    return 0;
}