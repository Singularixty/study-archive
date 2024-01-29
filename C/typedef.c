#include <stdio.h>
#include <string.h>
#include <stdbool.h>

typedef struct
{
   char name[20];
   int age;
   char department[20];
} Worker;

int main()
{
    Worker workers[2];

    workers[0] = (Worker){"Somchai", 19, "Programmer"};
    workers[1] = (Worker){"Somlak", 20, "Accountant"};

    int numWorkers = sizeof(workers) / sizeof(workers[0]);

    for (int i = 0; i < numWorkers; i++) {
        printf("[%s] %s %dY\n", workers[i].department, workers[i].name, workers[i].age);
    }

    getchar();
    return 0;
}
