#include <iostream>
using namespace std;

int main(void) {
    int fixed, flexible, price;
    cin >> fixed >> flexible >> price;
    if (flexible >= price)
        cout << "-1\n";
    else
        cout << (fixed / (price - flexible)) + 1;
    return 0;
}