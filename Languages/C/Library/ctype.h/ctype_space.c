#include <stdio.h>
#include <ctype.h>

int main() {
    int i, j;
    char array[] = "S o me ArrayHehe";
    
    for (i = 0, j = 0; array[i] != '\0'; i++) {
        if (!isspace((unsigned char)array[i])) {
            array[j++] = array[i];
        }
    }
    
    array[j] = '\0';
    
    printf("%s\n", array);
    return 0;
}
