#include <iostream>

using namespace std;

int N, M;
int arr[9] = { 0, };

void dfs(int depth, int num) {
    if (depth == M) {
        for (int i = 0; i < M; i++)
            cout << arr[i] << ' ';
        cout << '\n';
    }
    else {
        for (int i = num; i <= N; i++) {
            arr[depth] = i;
            dfs(depth + 1, i);
        }
    }
}

int main()
{
    // N과 M (4)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    dfs(0, 1);

    return 0;
}