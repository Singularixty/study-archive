#include <stdio.h>
#include <stdbool.h>

int main() {
    // 1 Bytes: Store only a single character
    char my_grade = 'A';
    printf("This type stores only a single character: %c\n", my_grade);
    
    // 1 Bytes/Character: Store multiple characters called "string"
    char my_array[] = "Singularixty";
    printf("My name is %s\n", my_array); 

    // 4 Bytes: Store a number with decimals 6-7 digits; if > 7, cause a precision loss
    float gpa = 3.6759294;
    // 8 Bytes: Store a number with decimals 15-16 digits; if > 16, cause a precision loss
    double pi = 3.1415926535897932;
    // 8 Bytes: Store a number with decimals beyond data type limit
    float precision_loss = 3.1415926535897932;

    printf("This type store 6-7 digits: %0.7f\n", gpa);
    printf("This type store 15-16 digits: %0.15lf\n", pi);
    printf("If float store more than 7 digits: %0.15lf\n", precision_loss);

    // 1 Byte: Store a boolean True/False 1=True, 0=False
    bool ishuman = true;
    printf("Is that creature human?:%i\n", ishuman);

    // unsigned syntax mean the value will not store negative number, default is signed.
    // If the value is beyond its range, it will overflow and goes to minimum value
    // 1 Byte: Store 0 to +255 (display using ASCII CHAR)
    unsigned char ascii_char = 100;
    printf("ASCII Character number 100 is %c\n", ascii_char);
    // 1 Byte: Store -128 to +127
    char number = 100;
    printf("Lucky number is %d\n", number);

    // 2 Bytes: Store -32,768 to +32,767 
    short h = 32767;
    printf("This small country has the total citizen of %i\n", h);
    // 2 Bytes: Store 0 to +65,535
    unsigned short i = 65535;
    printf("This price of this item is %i\n", i);

    // 4 Bytes: Store large integers from -2,147,483,648 to +2,147,483,647
    int population = 7654321;
    printf("Population of the city: %d\n", population);

    // 4 Bytes: Store 0 to +4,294,967,295
    unsigned long int largePositiveNumber = 987654321;
    printf("Large positive number: %lu\n", largePositiveNumber);

    // 8 Bytes: Store very large integers from -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807
    long long int hugeNumber = -9223372036854775807LL;
    printf("Huge number: %lld\n", hugeNumber);

    // 8 Bytes: Store 0 to +18,446,744,073,709,551,615
    unsigned long long int veryLargeNumber = 18446744073709551615ULL;
    printf("Very large positive number: %llu\n", veryLargeNumber);

    return 0;
}
