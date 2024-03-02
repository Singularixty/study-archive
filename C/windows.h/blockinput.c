#include <windows.h>
#include <stdio.h>

int main(){
    BOOL result = BlockInput(TRUE);
    Sleep(5000); 
    BOOL result2 = BlockInput(FALSE);
    system("pause");
    return 0;
}
