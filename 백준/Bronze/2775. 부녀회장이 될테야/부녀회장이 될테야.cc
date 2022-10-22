#include <iostream>
using namespace std;

int neighbor(int k, int n){ // 거주민 수의 합
    int sum = 0;
    if (k == 0)
        return n;
    for (int i = 1; i <= n; i++)
        sum += neighbor(k - 1, i);
    return sum;
}

int main(void) {
    int test;   // test case
    int k, n;   // k층, n호: k는 0층부터, n은 1호부터
    int sum = 0;
    cin >> test;
    for(int i = 0; i < test; i++){
        cin >> k >> n;
        sum = neighbor(k, n);
        cout << sum << "\n";
    }
    return 0;
}