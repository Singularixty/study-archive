#include <stdio.h>
#include <string.h>

enum Day{Sun = 1, Mon = 2, Tue = 3, Wed = 4, Thrs = 5, Fri = 6, Sat = 7};

int main(){
    enum Day today = Sat;
    printf("%d", today);
    getchar();
    return 0;
}