#include <stdio.h>
#include <string.h>

int main(){
    int age;
    char name[20];
    printf("What is your name?: ");
    fgets(name, 20, stdin);
    name[strlen(name)-1] = '\0';
    printf("What's your age?: ");
    scanf("%d", &age);
    printf("Hello!, %s\n", name);
    printf("You are %d years old.", age);
    return 0;
}