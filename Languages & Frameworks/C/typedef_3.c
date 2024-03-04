#include <stdio.h>

typedef struct{
    int x;
    int y;
} Point;

int main(){
    Point pos1;
    pos1.x = 50;
    pos1.y = 100;

    printf("Pos 1: %d\nPos 2: %d\n", pos1.x, pos1.y);

    system("pause");
    return 0;
}