#include <stdio.h>
#include <string.h>

int main() {
    char grade[3];
    int MAX_SCORE = 100;
    int CSBuffer, MTESBuffer, FESBuffer;
    int FinalScore;

    printf("Collected Score: ");
    scanf("%d", &CSBuffer);
    printf("Mid Term Score: ");
    scanf("%d", &MTESBuffer);
    printf("Final Exam Score: ");
    scanf("%d", &FESBuffer);

    if (CSBuffer < 0 || CSBuffer > 30) {
        printf("Collected Point is lesser than zero or greater than 30\n");
        return 1;
    }
    if (MTESBuffer < 0 || MTESBuffer > 30) {
        printf("Midterm Exam Point is lesser than zero or greater than 30\n");
        return 1;
    }
    if (FESBuffer < 0 || FESBuffer > 40) {
        printf("Final Exam Point is lesser than zero or greater than 40\n");
        return 1;
    }

    FinalScore = CSBuffer + MTESBuffer + FESBuffer;

    if (FinalScore > MAX_SCORE) {
        printf("Summation of scores is greater than maximum score\n");
        return 1;
    }

    // Grading
    if (FinalScore >= 80 && FinalScore <= 100){
        strcpy(grade, "A");
    }
    else if (FinalScore >= 75 && FinalScore <= 79){
        strcpy(grade, "B+");
    }
    else if (FinalScore >= 70 && FinalScore <= 74){
        strcpy(grade, "B");
    }
    else if (FinalScore >= 65 && FinalScore <= 69){
        strcpy(grade, "C+");
    }
    else if (FinalScore >= 60 && FinalScore <= 64){
        strcpy(grade, "C");
    }
    else if (FinalScore >= 55 && FinalScore <= 59){
        strcpy(grade, "D+");
    }
    else if (FinalScore >= 50 && FinalScore <= 54){
        strcpy(grade, "D");
    }
    else{
        strcpy(grade, "F");
    }
    
    printf("Final Student Grade: %s\n", grade);
    system("pause");
    return 0;
}
