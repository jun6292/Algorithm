#include <iostream>
#include <algorithm>

using namespace std;
int arr[300], dp[300];    // 300: 계단의 최대 개수, arr: 입력 받을 배열, dp: 최댓값 저장

int main()
{
    // 계단 오기
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    int n;  // 계단의 수

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    dp[0] = arr[0]; 
    dp[1] = max(arr[1], arr[0] + arr[1]);
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2]);
    for (int i = 3; i < n; i++) {
        // 전전전 계단을 밟았을 때 최댓값 + 전 계단 + 현재 계단 vs 전전 계단 밟았을 때 최댓값 + 현재 계단
        dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i]);
    }
    cout << dp[n - 1] << '\n';
}