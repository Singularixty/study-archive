#include <stdio.h>

int main() {
    int student_score;

    printf("Student score: ");
    scanf("%d", &student_score);

    if (student_score > 90) {
        printf("Your grade is A+");
    } else if (student_score > 80) {
        printf("Your grade is A");
    } else if (student_score > 70) {
        printf("Your grade is B");
    } else if (student_score > 60) {
        printf("Your grade is C");
    } else if (student_score > 50) {
        printf("Your grade is D");
    } else {
        printf("Your grade is F");
    }

    return 0;
}
