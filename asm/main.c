#include <stdio.h>
#include "Add100.h"

int main()
{
    int result;
    result = Add100(20);
    printf("result: %i\n", result);
    return 0;
}

// compile through 'gcc -m32 Add100.o main.c -o [FILENAME]
