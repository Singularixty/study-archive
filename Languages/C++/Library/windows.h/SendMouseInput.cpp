#include <iostream>
#include <windows.h>

int main(){
    INPUT input;
    input.type = INPUT_MOUSE;
    input.mi.dx = 100;
    input.mi.dy = 100;
    input.mi.mouseData = 0;
    input.mi.dwFlags = MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_MOVE;
    input.mi.time = 0;
    input.mi.dwExtraInfo = 0;

    SendInput(1, &input, sizeof(INPUT));
    return 0;
}