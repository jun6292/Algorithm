#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer = arr;
    auto last = unique(answer.begin(), answer.end());
    answer.erase(last, answer.end());
    return answer;
}