#include <iostream>
using namespace std;

// greedy algorithm
int main(void) {
    int kg;
    int a, b;   // a는 5kg봉지 수, b는 3kg봉지 수
    cin >> kg;
    a = kg / 5;
    while (a >= 0){
        if ((kg - 5 * a) % 3 == 0){
            b = (kg - 5 * a) / 3;
            cout << a + b;
            break;
        }
        a--;
    }
    if (kg != 5 * a + 3 * b)
        cout << "-1\n";
    return 0;
}
