#include <iostream>
#include <cmath>

using namespace std;

int ans = -1, N;
int arr[21][21] = { 0, };
bool visited[21];

void dfs(int depth, int num) {
    if (depth == N / 2) {
        int start = 0, link = 0;
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i] && visited[j])
                    start += arr[i][j];
                if (visited[i] == false && visited[j] == false)
                    link += arr[i][j];
            }
        }

        int min = abs(start - link);
        if (ans > min || ans == -1)
            ans = min;
    } else {
        for (int i = num; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(depth + 1, i + 1);
                visited[i] = false;
            }
        }
    }
}

int main(void)
{
    // 스타트와 링크
    ios_base :: sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> arr[i][j];
        }
    }
    dfs(0, 0);
    cout << ans << '\n';
}