#include <stdio.h>

int FindMaxNum(int num1, int num2, int num3) {
    if (num1 >= num2 && num1 >= num3) {
        return num1;
    } else if (num2 >= num1 && num2 >= num3) {
        return num2;
    } else {
        return num3;
    }
}

int main() {
    int findnum = FindMaxNum(6621, 125, 66);
    printf("Highest number is %d", findnum);
    return 0;
}
