#include <stdio.h>
#include <string.h>

int main() {
    char string1[10] = "Hello"; 
    int action;

    printf("String Modifier:\n");
    printf("1. Change your text to uppercase\n");
    printf("2. Change your text to lowercase\n");
    printf("3. Reverse your text\n");
    printf("Type number to select an action: ");
    if (scanf("%d", &action) != 1) {
        printf("Invalid input!\n");
        return 1;
    }

    getchar();

    if (action == 1){
        strupr(string1);
    } 
    else if (action == 2){
        strlwr(string1);
    } 
    else if (action == 3){
        strrev(string1);
    }
    else {
        printf("Invalid number!\n");
        return 1;
    }

    printf("%s\n", string1); 
    int string_length = strlen(string1);
    printf("String length is %d characters", string_length);
    getchar();
    return 0;
}
