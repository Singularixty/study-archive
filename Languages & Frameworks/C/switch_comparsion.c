#include <stdio.h>

int main(){
    char grade;
    printf("What is your grade?: ");
    scanf("%c", &grade);
    switch (grade){
        case 'A' | 'a':
            printf("Excellent");
            break;
        case 'B' | 'b':
            printf("Good!");
            break;
        case 'C' | 'c':
            printf("Nice try!");
            break;
        case 'D' | 'dgrade':
            printf("Almost!");
            break;
        default:
            printf("Please enter your grade!");
            break;
    }
}