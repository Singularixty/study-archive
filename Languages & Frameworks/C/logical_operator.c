#include <stdio.h>
#include <stdbool.h>

int main(){
    int age = 19;
    char name[12] = "Singularixty";

    if (age >= 19 && name == "Singularixty"){
        printf("You are allowed");
    }
    else{
        printf("You are not allowed in here!");
    }
    printf("\n");

    if (age >= 19 || name == "Singularixty"){
        printf("You are allowed");
    }
    else{
        printf("You are not allowed in here!");
    }

    printf("\n");

    if (!age >= 19 || name == "Singularixty"){
        printf("You are allowed but underage");
    }
    else{
        printf("You are not allowed in here!");
    }

    return 0;
}