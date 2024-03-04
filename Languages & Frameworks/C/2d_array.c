#include <stdio.h>
#include <math.h>

int main(){
    double table_of_data[2][3] = {{1, 2, 3}, {24.3, 15.4, 25.3}};
    int rows = sizeof(table_of_data) / sizeof(table_of_data[0]);
    int columns = sizeof(table_of_data[0]) / sizeof(table_of_data[0][0]);

    for (int row = 0; row < rows; row++){
        for (int column = 0; column < columns; column++){
            double result = pow(table_of_data[row][column], 2);
            printf("%.2lf ", result);
        }
        printf("\n");
    }
    getchar();
    return 0;
}
