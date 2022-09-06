#include <iostream>
#include <cmath>

using namespace std;

// 두 점 사이의 거리
double dist(double x1, double y1, double x2, double y2) {
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main()
{
    // 하키
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int W, H, X, Y, P;
    int x, y;   // 선수 좌표
    int ans = 0;

    cin >> W >> H >> X >> Y >> P;
    for (int i = 0; i < P; i++) {
        cin >> x >> y;
        if (x >= X && x <= X + W && y >= Y && y <= Y + H) // square 안, 또는 경계에 있으면
            ans++;
        else if (dist(x, y, X, Y + H / 2) <= H / 2 || dist(x, y, X + W, Y + H / 2) <= H / 2)   // 반원 안, 또는 경계에 있으면
            ans++;
    }

    cout << ans << "\n";

    return 0;
}