#include <string>
#include <vector>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int sum = 0;    // 자릿수의 합
    int result = x; // x값 변경 방지
    
    // add all digits of x
    while (result > 0){ 
        sum += result % 10;
        result /= 10;
    }
    if ((x % sum) != 0)
        answer = false;
    return answer;
}