#include <iostream>
using namespace std;

int fibonacci(int N){
    if (N == 0)
        return 0;
    if (N == 1)
        return 1;
    if (N == 2)
        return 1;
    return fibonacci(N - 2) + fibonacci(N - 1);
}

int main(void)
{
    int n;
    int result = 0;
    cin >> n;
    result = fibonacci(n);
    cout << result;
    return 0;
}