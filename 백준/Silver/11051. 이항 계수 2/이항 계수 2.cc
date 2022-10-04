#include <iostream>

using namespace std;

int main()
{
    // 이항 계수 2
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // 파스칼의 삼각형, 동적 계획법으로 풀이
    long long dp[1001][1001] = { 0, };
    int N, K;
    cin >> N >> K;
    for (int i = 1; i <= N; i++) {
        for (int j = 0; j <= N; j++) {
            if (j == 0 || j == i)
                dp[i][j] = 1;
            else
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 10007;
        }
    }
    cout << dp[N][K] << '\n';
    return 0;
}