#include <iostream>
using namespace std;

void counting_star(int i, int j, int N) {
    if ((i / N) % 3 == 1 && (j / N) % 3 == 1){
        cout << " ";
    }
    else
    {
        if (N / 3 == 0)
            cout << "*";
        else
            counting_star(i, j, N/3);
    }
}

int main(void)
{
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++)
            counting_star(i, j, N);
        cout << '\n';
    }
    return 0;
}
