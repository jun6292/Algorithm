#include <iostream>

using namespace std;

int main()
{
    // 직각삼각형
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while (true) {
        int a, b, c;
        cin >> a >> b >> c;

        if (a == 0 && b == 0 && c == 0)
            break;

        if (a > b && a > c) {
            if (b * b + c * c == a * a)
                cout << "right\n";
            else
                cout << "wrong\n";
        }
        else if (b > a && b > c) {
            if (a * a + c * c == b * b)
                cout << "right\n";
            else
                cout << "wrong\n";
        }
        else if (c > a && c > b) {
            if (a * a + b * b == c * c)
                cout << "right\n";
            else
                cout << "wrong\n";
        }
    }

	return 0;
}