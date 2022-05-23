#include <iostream>
using namespace std;

int main(void)
{
    int N, M;   // N: 카드의 개수, M: 카드에 쓰인 수
    cin >> N >> M;
    int *num = new int [N];
    int result = 0;
    for (int i = 0; i < N; i++)
        cin >> num[i];
    for (int i = 0; i < N; i++){
        for (int j = i + 1; j < N; j++){
            for (int k = j + 1; k < N; k++){
                if (num[i] + num[j] + num[k] <= M && num[i] + num[j] + num[k] > result)
                    result = num[i] + num[j] + num[k];
            }
        }
    }
    cout << result << "\n";
    delete [] num;
    return 0;
}