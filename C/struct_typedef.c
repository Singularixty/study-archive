#include <stdio.h>

typedef struct car_spec{
    char *engine;
    char *fuel_type;
} Car;

int main(){
    Car c1;
    c1.engine = "Some Engine";
    c1.fuel_type = "Diesel";
    printf("%s, %s", c1.engine, c1.fuel_type);
    return 0;
}