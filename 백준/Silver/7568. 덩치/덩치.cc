#include <iostream>
using namespace std;

int main(void) {
    int N;  // 2 <= N <= 50
    int arr[50][2];     // ([0]: 몸무게, [1]: 키)를 저장할 배열
    int rank[50];
    fill_n(rank, 50, 1);    // 덩치 등수를 나타내기 위해 1로 초기화
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> arr[i][0] >> arr[i][1];
    for (int i = 0; i < N; i++){    // 브루트 포스, 전부 비교
        for (int j = 0; j < N; j++){
            if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1])
                rank[i]++;
        }
        cout << rank[i] << " ";
    }
    return 0;
}  