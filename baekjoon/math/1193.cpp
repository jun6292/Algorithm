#include <iostream>
using namespace std;

int main(void) {
    int X;
    cin >> X;
    int i = 1;  // 대각선 행
    while (X > i){
        X -= i;
        i++;
    }
    if (i % 2 == 1)
        cout << i + 1 - X << "/" << X << "\n";
    else
        cout << X << "/" << i + 1 - X << "\n";
    return 0;
}
