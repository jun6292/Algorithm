#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int pcnt = 0, ycnt = 0;
    for (int i = 0; i < s.length(); i++){
        if (s[i] == 'p' || s[i] == 'P')
            pcnt++;
        else if (s[i] == 'y' || s[i] == 'Y')
            ycnt++;
    }
    if (pcnt == ycnt)
        answer = true;
    else
        answer = false;
    return answer;
}