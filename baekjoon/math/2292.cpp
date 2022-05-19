#include <iostream>
using namespace std;

int main(void) {
    int N;
    int i = 0, j = 1, n = 2, cnt = 1;
    cin >> N;
    while (1){
        if (N == 1){
            cout << "1\n";
            break;
        }
        cnt++;
        if (1 + 6 * i < N && N <= 1 + 6 * j){
            cout << cnt;
            break ;
        }
        i = j;
        j += n++;        
    }
    return 0;
}
