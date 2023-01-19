#include <iostream>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int f_arr[40];
int N;
int re_cnt = 0, dp_cnt = 0; // 재귀호출 카운트, 동적 프로그래밍 카운트

int fib_re(int n) {
    if (n == 1  || n == 2) {
        re_cnt++;
        return 1;
    }
    else {
        // re_cnt++;
        return fib_re(n - 2) + fib_re(n - 1);
    }
}

void fib_dp(int n) {
    f_arr[0] = 1; f_arr[1] = 1;
    for (int i = 2; i < n; i++) {
        f_arr[i] = f_arr[i - 1] + f_arr[i - 2];
        dp_cnt++;
    }
}

int main()
{
    // 피보나치 수 1
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    fib_re(N);
    fib_dp(N);
    cout << re_cnt << ' ' << dp_cnt << '\n';
}