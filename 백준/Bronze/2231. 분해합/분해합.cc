#include <iostream>
using namespace std;

int main(void)
{
    int N;
    int result = 0;
    int partition;
    cin >> N;
    for(int i = 1; i < N; i++){
        result = i;
        partition = i;
        while (partition){  // partition 각 자리수를 더함
            result += partition % 10;   
            partition /= 10;
        }
        if (result == N){
            cout << i;
            return 0;   // 가장 작은 생성자만 출력하고 프로그램 종료
        }
    }
    cout << "0\n";  // 생성자가 없을 시 0 출력
    return 0;
}