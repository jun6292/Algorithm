#include <iostream>
#include <vector>

using namespace std;

int main()
{
    // 2960번: 에라토스테네스의 체
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, K;
    int cnt = 0;

    cin >> N >> K;
    vector<bool> v(N + 1);
    for (int i = 2; i <= N; i++)
        v[i] = true;
    for (int i = 2; i <= N; i++) {
        for (int j = i; j <= N; j += i) {
            if (v[j]) {
                v[j] = false;
                cnt++;
                if (cnt == K) {
                    cout << j << "\n";
                    return 0;
                }
            }
        }
    }
}