#include <stdio.h>
#include <string.h>

struct Student
{
    char name[12];
    int age;
    float gpa;
};

int main(){
    struct Student student_1 = {"Somchai", 12, 3.21};
    struct Student student_2 = {"SomLuk", 13, 3.55};
    struct Student student_3 = {"Sompong", 13, 1.92};

    struct Student students[] = {student_1, student_2, student_3};

    for(int i = 0; i < sizeof(students)/sizeof(students[0]); i++){
        printf("%s is %d years old / GPA: %.2lf\n", students[i].name, students[i].age, students[i].gpa);
    }

    getchar();
    return 0;
}