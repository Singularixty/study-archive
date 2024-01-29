#include <stdio.h>
#include <time.h>

int main(int argc, char *agrv[]){
    time_t t = time(NULL);
    printf("Current Time is %ld\n", t);
    struct tm date = *localtime(&t);
    printf("Year: %d\n", date.tm_year + 1900);
    system("pause");
    return 0;
}