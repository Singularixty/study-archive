#include <stdio.h>

void deposit();
void withdraw();
void check_balance();
void exit_bank();

int main() {
    int action;
    do {
        printf("\nBank Account Manager\n");
        printf("1). Deposit Money\n");
        printf("2). Withdraw Money\n");
        printf("3). Check Balance\n");
        printf("4). Exit Bank\n");
        printf("Your Action: ");
        scanf("%d", &action);

        switch (action) {
            case 1:
                deposit();
                break;
            case 2:
                withdraw();
                break;
            case 3:
                check_balance();
                break;
            case 4:
                exit_bank();
                break;
            default:
                printf("Please select between (1-4)!\n");
        }
    } while (action != 4);

    return 0;
}

void check_balance() {
    FILE *CheckBalance;
    CheckBalance = fopen("balance.acc", "r");
    if (CheckBalance == NULL) {
        perror("Error couldn't find bank account");
        return;
    }
    double balance;
    fscanf(CheckBalance, "%lf", &balance);
    printf("Current Balance: %lf\n", balance);
    fclose(CheckBalance);
}

void withdraw() {
    FILE *CheckBalance;
    CheckBalance = fopen("balance.acc", "r+");
    if (CheckBalance == NULL) {
        perror("Error couldn't find bank account");
        return;
    }

    double balance;
    fscanf(CheckBalance, "%lf", &balance);

    double amount;
    printf("Enter the amount to withdraw: ");
    scanf("%lf", &amount);

    if (amount > balance) {
        printf("Insufficient funds!\n");
    } else {
        balance -= amount;
        fseek(CheckBalance, 0, SEEK_SET);
        fprintf(CheckBalance, "%lf", balance);
        printf("Withdrawal successful! \nRemaining balance: %lf\n", balance);
    }

    fclose(CheckBalance);
}

void deposit() {
    FILE *CheckBalance;
    CheckBalance = fopen("balance.acc", "r+");
    if (CheckBalance == NULL) {
        perror("Error couldn't find bank account");
        return;
    }

    double balance;
    fscanf(CheckBalance, "%lf", &balance);

    double amount;
    printf("Enter the amount to deposit: ");
    scanf("%lf", &amount);

    balance += amount;
    fseek(CheckBalance, 0, SEEK_SET); 
    fprintf(CheckBalance, "%lf", balance);
    printf("Deposit successful! \nNew balance: %lf\n", balance);

    fclose(CheckBalance);
}

void exit_bank() {
    printf("Thank you so much for using the bank account manager <3\n");
}
