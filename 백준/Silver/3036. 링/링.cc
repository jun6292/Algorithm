#include <iostream>
#include <vector>

using namespace std;

int gcd(int x, int y) { // 최대 공약수 구하기, 유클리드 호제 알고리즘
    int r;
    while (y) {
        r = x % y;
        x = y;
        y = r;
    }
    return x;
}

int main()
{
    // 링
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    int radius;
    vector<int> ring;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> radius;
        ring.push_back(radius);
    }
    for (int i = 1; i < N; i++) {   // 기약분수로 나타내기 위해서 최대 공약수로 두 수를 나눠줌
        int gcd_r = gcd(ring[0], ring[i]);
        int ring1 = ring[0] / gcd_r;
        int ring2 = ring[i] / gcd_r;
        cout << ring1 << '/' << ring2 << '\n'; 
    }
}