#include <stdio.h>

void SingHappyBirthday(char *name, int age){
    for (int i=0; i < 3; i++){
        printf("Happy birthday to %s!\n", name);
    }
    printf("Congratulations!, You are %d years old.", age);
}

int main(){
    SingHappyBirthday("Singularixty", 12);
    return 0;
}