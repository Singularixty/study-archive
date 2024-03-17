#include <stdio.h>
#include <string.h>

int main(){
    char name[20];
    printf("What's your name?: ");
    scanf("%s", name);
    printf("Hello, %s!", name);
}