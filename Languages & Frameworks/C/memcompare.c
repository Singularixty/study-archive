#include <stdio.h>
#include <string.h>

int main(){
    char string1[] = "FirstString";
    char string2[] = "SecondString";
    int result = memcmp(string1, string2, 3);
    printf("%d", result);
    system("pause");
    return 0;
}