#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

int main(){
    char Input[10000];
    printf("Input: ");
    scanf("%s", &Input);

    bool has_upperchar = false;
    bool has_lowerchar = false;

    for (int i = 0; Input[i] != '\0'; i++){
        if (isupper(Input[i])){
            has_upperchar = true;
            printf("%d", isupper(Input[i]));
        }
        if (islower(Input[i])){
            has_lowerchar = true;
            printf("%d", islower(Input[i]));
        }
    }
    
    if (has_upperchar & has_lowerchar){
        printf("Input characters are mixed\n");
    }
    else if (has_upperchar){
        printf("Input characters are uppercase\n");
    }
    else{
        printf("Input characters are lowercase\n");
    }

    system("pause");
    return 0;
}