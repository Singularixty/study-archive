#include <stdio.h>
#include <ctype.h>

int main(){
    char myString[] = "Are you fine?";
    int i, check;
    for (i = 0; myString[i] != '\0'; i++){
        check = isalpha(myString[i]);
        if (check != 0){
            printf("String #%d : %c is a character\n", i+1, myString[i]);
        }else{
            printf("String #%d : %c is not a character\n", i+1, myString[i]);
        }

    }
    system("pause");
    return 0;
}