#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    const int MIN_NUM = 1;
    const int MAX_NUM = 50;
    int guess;
    int guesses = 0;
    int answer;

    srand(time(0));
    answer = (rand() % MAX_NUM) + MIN_NUM;

    do{
        printf("Your num guess: ");
        scanf("%d", &guess);
        if (guess > answer){
            printf("Too high!\n");
        }
        else if (guess < answer){
            printf("Too low\n");
        }
        else{
            printf("Correct!\n");
        }
        guesses++;
    }while (guess != answer);
    
    printf("answer: %d\n", answer);
    getchar();
    printf("gueeses until correct: %d\n", guesses);

    getchar();
    return 0;
}