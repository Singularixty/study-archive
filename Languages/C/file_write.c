#include <stdio.h>

int main(){
    FILE *fp;
    fp = fopen(".temp/temp.txt", "w");
    fprintf(fp, "hello world");
    fclose(fp);
    return 0;
}