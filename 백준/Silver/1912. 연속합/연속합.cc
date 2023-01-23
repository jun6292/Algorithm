#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
    // 연속합
    ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    int n;  // input
    int dp[100000], arr[100000];

    cin >> n;
    for (int i = 0; i < n; i++) {  
        cin >> arr[i];  // 입력 받은 숫자들을 arr에 저장
    }
    int max_num = arr[0];
    dp[0] = arr[0]; 
    for (int i = 1; i < n; i++) {   // dp는 i번째에서 끝나는 제일 큰 연속합
        dp[i] = max(dp[i - 1] + arr[i], arr[i]);    // i번째에서 끝나는 제일 큰 연속합과 arr[i] 중 큰 값
        max_num = max(dp[i], max_num);  // 누적합의 최댓값과 dp[i]의 값 중 더 큰 값
    }
    cout << max_num << '\n';
}