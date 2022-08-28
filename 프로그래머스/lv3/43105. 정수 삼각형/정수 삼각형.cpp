#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    vector<vector<int>> dp = triangle;
    
    int n = triangle.size();
    
    // y = 1 부터 시작: (0, 0)에서의 dp 값은 변경하지 않음 dp(0, 0) = tri(0, 0)
    for (int y = 1; y < n; y++) {
        for (int x = 0; x <= y; x++) {
            if (x == 0) // 직각 삼각형에서 가장 왼쪽 세로 라인
                dp[y][x] = dp[y - 1][x] + triangle[y][x];
            else if (x == y)    // 직각 삼각형의 빗변
                dp[y][x] = dp[y - 1][x - 1] + triangle[y][x];
            else
                dp[y][x] = max(dp[y - 1][x], dp[y - 1][x - 1]) + triangle[y][x];
        }
        // dp 벡터 맨 마지막행에서 최댓값을 찾음
        answer = *max_element(dp[n - 1].begin(), dp[n - 1].end());
    }
    
    return answer;
}