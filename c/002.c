#include <stdio.h>

int foo(int a, int b);
void ffo(int* a, int* b);

int main()
{
	int a = 3;
	int b = 5;

	int c = foo(a, b);
	printf("a = %d, b = %d\n", a, b);
	printf("c is %d\n", c);

	ffo(&a, &b);
	printf("a = %d, b = %d\n", a, b);

	return 0;
}

int foo(int a, int b)
{
	return a + b;
}

void ffo(int* a, int* b)
{
	int tmp = 0;
	tmp = *a;
	*a = *b;
	*b = tmp;
}
