#include <iostream>

using namespace std;

int main()
{
    // 다리 놓기
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T, N, M;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N >> M;
        long long a = 1, b = 1;
        // C(M, N)
        for (int k = M; k > M - N; k--) {
            a *= k;
            a /= b;
            b++;
        }
        cout << a << '\n';
    }
    return 0;
}