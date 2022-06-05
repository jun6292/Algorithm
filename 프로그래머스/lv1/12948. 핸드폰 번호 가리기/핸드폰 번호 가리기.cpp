#include <string>
#include <vector>

using namespace std;

string solution(string phone_number) {
    string answer = phone_number;
    int size = phone_number.length();
    for(int i = 0; i < size - 4; i++)
        answer[i] = '*';
    return answer;
}