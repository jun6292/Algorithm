#include <iostream>
using namespace std;

int main(void) {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int height, slip, climb;
    cin >> climb >> slip >> height;
    if (height <= climb)
        cout << "1\n";
    else if ((height - climb) % (climb - slip) == 0)
        cout << ((height - climb) / (climb - slip)) + 1;
    else
        cout << ((height - climb) / (climb - slip)) + 2;
    return 0;
}
