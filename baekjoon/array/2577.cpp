#include <iostream>
using namespace std;

int main(void)
{
	int a, b, c;
	int print_num[10] = { 0 };

	cin >> a >> b >> c;
	int result = (a*b*c);

	while (result)
	{
		print_num[result % 10] += 1;
		result /= 10;
	}
	for (int i = 0; i < 10; i++)
		cout << print_num[i] << '\n';
}
