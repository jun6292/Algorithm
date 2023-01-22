#include <iostream>

using namespace std;
long long dp[101];  // int로 하면 틀림

int main()
{
    // 파도반 수열
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int N, T; // 입력, 테스트 케이스 수

    dp[1] = 1; dp[2] = 1; dp[3] = 1;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        for (int j = 4; j <= N; j++) {
            dp[j] = dp[j - 2] + dp[j - 3];  // P(N) 점화식
        }
        cout << dp[N] << '\n';
    }
}