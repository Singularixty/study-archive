#include "header.h"
#include <iostream>

void swap_var(std::string &FirstVar, std::string &SecondVar) {
    std::string TempVar;
    TempVar = FirstVar;
    FirstVar = SecondVar;
    SecondVar = TempVar;
}