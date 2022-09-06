#include <iostream>
#include <cmath>

using namespace std;

// 두 점 사이의 거리
double dist(double x1, double y1, double x2, double y2) {
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main(void)
{
    // 터렛
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    int x1, y1, r1, x2, y2, r2;

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        double distance = dist(x1, y1, x2, y2);
        // 두 원이 겹치는 경우
        if (distance == 0 && r1 == r2)
            cout << "-1\n";
        // 원이 외접하는 경우, 원이 내접하는 경우
        else if (r1 + r2 == distance || abs(r1 - r2) == distance)
            cout << "1\n";
        else if (distance < abs(r1 - r2))  // 작은 원이 큰 원 안에서 만나지 않는 경우
            cout << "0\n";
        else if (distance < r1 + r2)  // 두 원이 두 점에서 만나는 경우
            cout << "2\n";
        else if (distance > r1 + r2)
            cout << "0\n";  // 작은 원이 큰 원 밖에서 만나지 않는 경우
    }

    return 0;
}