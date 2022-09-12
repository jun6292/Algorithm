#include <iostream>
#include <algorithm>

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

int main()
{
    // 최대공약수와 최소공배수
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int x, y;

    cin >> x >> y;
    cout << gcd(x, y) << "\n" << lcm(x, y);

    return 0;
}