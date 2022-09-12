#include <iostream>

using namespace std;

int gcd(int a, int b) {
    int r = 0;
    int large = max(a, b);
    int small = min(a, b);
    // 유클리드 호제
    while (small) {
        r = large % small;
        large = small;
        small = r;
    }
    return large;
}

int lcm(int a, int b) {
    return a * b / gcd(a, b);
}

int main(void)
{
    // 최소 공배수
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    int a, b;

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> a >> b;
        cout << lcm(a, b) << "\n";
    }

    return 0;
}