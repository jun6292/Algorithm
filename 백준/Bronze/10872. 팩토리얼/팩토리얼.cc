#include <iostream>
using namespace std;

int factorial(int N){
    if (N == 0)
        return 1;
    if (N == 1)
        return 1;
    return N * factorial(N - 1);
}

int main(void)
{
    int N;
    int result = 0;
    cin >> N;
    result = factorial(N);
    cout << result;
    return 0;
}