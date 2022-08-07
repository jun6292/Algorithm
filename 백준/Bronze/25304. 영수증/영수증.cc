#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int X, N, a, b;
    int result = 0;
    cin >> X >> N;
    for (int i = 0; i < N; i++) {
        cin >> a >> b;
        result += a * b;
    }
    if (result == X)
        cout << "Yes\n";
    else
        cout << "No\n";
    return 0;
}