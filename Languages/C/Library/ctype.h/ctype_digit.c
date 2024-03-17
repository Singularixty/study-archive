#include <stdio.h>
#include <ctype.h>

int main() {
    int i, checker;
    char ArrayOfString[] = "Som62eKindOfArrayofString";
    
    for (i = 0; ArrayOfString[i] != '\0'; i++) {
        checker = isdigit(ArrayOfString[i]);
        printf("- Checker rV of %d : %d\n", i+1, checker);
        if (checker != 0) {
            printf("String #%d : %c is a number\n", i + 1, ArrayOfString[i]);
        } else {
            printf("String #%d : %c is NOT a number\n", i + 1, ArrayOfString[i]);
        }
    }
    return 0;
}
