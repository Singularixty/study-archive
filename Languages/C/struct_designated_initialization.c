#include <stdio.h>

struct abc
{
    int x;
    int y;
    int z;
};


int main(){
    struct abc example = {.y = 20, .x= 10};
    printf("x=%d, y=%d", example.x, example.y);
    return 0;
}