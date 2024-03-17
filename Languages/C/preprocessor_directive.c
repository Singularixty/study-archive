#include <stdio.h>

#define DEFAULT_NAME_SIZE 200
#define DEBUGGING_MODE 1

int main(){
    #ifdef DEBUGGING_MODE
        printf("[CURRENTLY IN DEBUGGING MODE]");
    #else
        char name[DEFAULT_NAME_SIZE];
        printf("Your name: \n");
    #endif
    
    return 0;
}