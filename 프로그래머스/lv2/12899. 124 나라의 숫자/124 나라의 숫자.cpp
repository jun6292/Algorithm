#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(int n) {
    string answer = "";
    string country = "124";
    while (n > 0) {
        if (n % 3 == 0) {
            answer += country[2];
            n--;
        }
        else if (n % 3 == 1)
            answer += country[0];
        else if (n % 3 == 2) 
            answer += country[1];
        
        n /= 3;
    }
    reverse(answer.begin(), answer.end());
    return answer;
}