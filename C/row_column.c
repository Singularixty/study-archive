#include <stdio.h>

int main() {
    int rows;
    int columns;
    char symbol;

    printf("Enter # of rows: \n");
    scanf("%d", &rows);

    printf("Enter # of columns: \n");
    scanf("%d", &columns);

    getchar();

    printf("Enter symbol to display: \n");
    scanf("%c", &symbol);
    getchar();
    printf("\n");
    for (int row = 1; row <= rows; row++) {
        for (int column = 1; column <= columns; column++) {
            printf("%c", symbol);
        }
        printf("\n");
    }

    getchar();
    return 0;
}
