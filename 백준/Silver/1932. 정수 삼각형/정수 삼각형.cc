#include <iostream>
#include <algorithm>

using namespace std;
int dp[500][500];

int main()
{
    // 정수 삼각형
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int n;
    int max_sum = 0;

    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cin >> dp[i][j];
        }
    }
    for (int i = 1; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            if (j == 0)   // 삼각형의 좌측변에 있는 수
                dp[i][j] = dp[i][j] + dp[i - 1][j]; //  같은 변에 있고 한단계 위에 있는 수와 더함
            else if (j == i)    // 삼각형의 우측변에 있는 수 
                dp[i][j] = dp[i][j] + dp[i - 1][j - 1]; //  같은 변에 있고 한단계 위에 있는 수와 더함
            else
                dp[i][j] = max(dp[i][j] + dp[i - 1][j - 1], dp[i][j] + dp[i - 1][j]);   // 왼쪽 대각선 위를 더한 값과 오른쪽 대각선 위를 더한 값중 큰 값
        }
    }
    for (int i = 0; i < n; i++) {   // 정수 삼각형의 밑변에서 가장 큰 수를 찾음
        if (max_sum < dp[n - 1][i])
            max_sum = dp[n - 1][i];
    }
    cout << max_sum << '\n';
}