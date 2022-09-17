#include <iostream>

using namespace std;

int arr[8] = { 0, };
int N, M;

void dfs(int depth) {
    if (depth == M) {
        for (int i = 0; i < M; i++)
            cout << arr[i] << ' ';
        cout << "\n";
    }
    else {
        for (int i = 1; i <= N; i++) {
            arr[depth] = i;
            dfs(depth + 1);
        }
    }
}

int main()
{
    // N과 M (3)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    dfs(0);

    return 0;
}