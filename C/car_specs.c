#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct car {
    char *car_name;
    int fuel_tank_capacity;
    int seating_cap;
} car;

int main() {
    int i;
    car newcar[2];
    
    for (i = 0; i < sizeof(newcar) / sizeof(car); i++) {
        newcar[i].car_name = (char*)malloc(50 * sizeof(char));
        if (newcar[i].car_name == NULL) {
            printf("Memory allocation failed.\n");
            return 1;
        }
    }

    printf("%d\n", sizeof(newcar) / sizeof(car));
    for (i = 0; i < 2; i++) {
        printf("Please declare car #%d capacity tank: ", i + 1);
        scanf("%d", &newcar[i].fuel_tank_capacity);
        printf("Please declare car #%d seating capacity: ", i + 1);
        scanf("%d", &newcar[i].seating_cap);
        printf("Please declare car #%d's name: ", i + 1);
        scanf("%s", newcar[i].car_name);
    }

    for (i = 0; i < 2; i++) {
        printf("car #%d capacity tank: %d\n", i + 1, newcar[i].fuel_tank_capacity);
        printf("car #%d seating capacity: %d\n", i + 1, newcar[i].seating_cap);
        printf("car #%d's name: %s\n", i + 1, newcar[i].car_name);
        printf("--------------------------------------------\n");
    }
    
    // Free allocated memory
    for (i = 0; i < 2; i++) {
        free(newcar[i].car_name);
    }
    
    return 0;
}
