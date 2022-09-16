#include <iostream>

using namespace std;

int N, M;
int arr[9] = { 0, };
bool visited[9] = { false, };

void dfs(int depth) {
    if (depth == M) {
        for (int i = 0; i < M; i++)
            cout << arr[i] << ' ';
        cout << "\n";
        return;
    }
    for (int i = 1; i <= N; i++) {
        if (!visited[i]) {
            visited[i] = true;
            arr[depth] = i;
            dfs(depth + 1);
            visited[i] = false;
        }
    }
}

int main(void)
{
    // N과 M (1)
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    dfs(0);

    return 0;
}