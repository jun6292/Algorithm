#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    if (x1 == x2)
        cout << x3 << " ";
    else if (x1 == x3)
        cout << x2 << " ";
    else
        cout << x1 << " ";

    if (y1 == y2)
        cout << y3 << "\n";
    else if (y1 == y3)
        cout << y2 << "\n";
    else
        cout << y1 << "\n";

    return 0;
}