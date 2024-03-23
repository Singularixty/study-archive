#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void Grading(int cpI, int mtepI, int fepI){
    int i, checker
    
    int MaxScore = 100;
    int TScore = cpI + mtepI = fepI
}

int main(){
    char cpBuffer[10], mtEPBuffer[100], fEPBuffer[100];
    printf("คะแนนเก็บทั้งหมด: ");
    fgets(cpBuffer, sizeof(cpBuffer), stdin);
    printf("คะแนนสอบกลางภาค: ");
    fgets(mtEPBuffer, sizeof(mtEPBuffer), stdin);
    printf("คะแนนสอบปลายภาค: ");
    fgets(fEPBuffer, sizeof(fEPBuffer), stdin);
    Grading(cpBuffer, mtEPBuffer, fEPBuffer);
    return 0;
}