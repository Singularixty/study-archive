#include <stdio.h>

int main(){
    char buffer[100];
    FILE *fp;
    fp = fopen(".temp/temp.txt", "r");
    fgets(buffer, sizeof(buffer), fp);
    printf("%s", buffer);
    fclose(fp);
    return 0;
}