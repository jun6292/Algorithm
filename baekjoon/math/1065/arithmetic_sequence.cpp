#include <iostream>
using namespace std;

int arithmetic_seq(int n)
{
	if (n < 100)
		return (1);

	int n1, n2, n3;
	n1 = n % 10;
	n2 = (n % 100) / 10; 
	n3 = n / 100;
	if ((n3 - n2) == (n2 - n1))
		return (1);
	return (0);
}

int main(void)
{
	int cnt = 0;
	int N;
	cin >> N;
	for(int i = 1; i <= N; i++){
		if(arithmetic_seq(i))
			cnt++;
	}
	cout << cnt << '\n';
	return 0;
}
