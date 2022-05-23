#include <iostream>
using namespace std;

void hanoi(int n, int from, int via, int to){
    if (n == 1)
        cout << from << " " << to << '\n';
    else{
        hanoi(n - 1, from, to, via);
        cout << from << " " << to << '\n';
        hanoi(n - 1, via, from, to);
    }
}

int main(void)
{
    int N;
    int result = 1;
    cin >> N;
    for(int i = 0; i < N; i++)
        result *= 2;
    cout << result - 1 << "\n";
    hanoi(N, 1, 2, 3);
    return 0;
}