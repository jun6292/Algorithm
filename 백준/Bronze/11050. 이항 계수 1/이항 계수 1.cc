#include <iostream>

using namespace std;

int main()
{
    // 이항계수 1
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, K;
    int a = 1, b = 1;
    cin >> N >> K;
    for (int i = 1; i <= K; i++)
        b *= i;
    for (int i = N; i > N - K; i--)
        a *= i;
	cout << a / b << '\n';
}