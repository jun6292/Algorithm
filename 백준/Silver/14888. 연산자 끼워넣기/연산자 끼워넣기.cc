#include <iostream>

using namespace std;

int N;
int op[4];  // +, -, *, /
int num[11];
int res_max = -1000000001;
int res_min = 1000000001;

// 깊이는 입력 받는 num 순서
void dfs(int depth, int result) {
    if (depth == N - 1) {
        if (result > res_max)
            res_max = result;
        if (result < res_min)
            res_min = result;
    }
    else {
        for (int i = 0; i < 4; i++) {
            if (op[i] > 0) {
                op[i]--;
                if (i == 0)
                    dfs(depth + 1, result + num[depth + 1]);
                else if (i == 1)
                    dfs(depth + 1, result - num[depth + 1]);
                else if (i == 2)
                    dfs(depth + 1, result * num[depth + 1]);
                else
                    dfs(depth + 1, result / num[depth + 1]);
                op[i]++;
            }
        }
    }
}

int main()
{
    // 연산자 끼워넣기
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> num[i];
    for (int i = 0; i < 4; i++)
        cin >> op[i];   

    dfs(0, num[0]);
    cout << res_max << '\n' << res_min;

    return 0;
}