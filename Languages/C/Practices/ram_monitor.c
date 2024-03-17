#include <windows.h>
#include <stdio.h>

int main() {
    MEMORYSTATUSEX memInfo;
    memInfo.dwLength = sizeof(MEMORYSTATUSEX);
    
    if (GlobalMemoryStatusEx(&memInfo)) {
        printf("Total Physical Memory: %llu MB\n", memInfo.ullTotalPhys / (1024 * 1024));
        printf("Used Physical Memory: %llu MB\n", (memInfo.ullTotalPhys - memInfo.ullAvailPhys) / (1024 * 1024));
        printf("Free Physical Memory: %llu MB\n", memInfo.ullAvailPhys / (1024 * 1024));
    } else {
        printf("Error getting memory information.\n");
    }

    system("pause");

    return 0;
}
