#include <stdio.h>

int main(){
    FILE *pFile = fopen("test.txt", "w");
    fprintf(pFile, "Hello World");
    fclose(pFile);
    getchar();
    return 0;
}