#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int x, y, w, h;
    int a, b;

    cin >> x >> y >> w >> h;
    a = min(w - x, h - y);
    b = min(x, y);
    cout << min(a, b) << "\n";

    return 0;
}