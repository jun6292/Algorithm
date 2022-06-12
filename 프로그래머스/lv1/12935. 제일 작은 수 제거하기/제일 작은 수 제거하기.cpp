#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int>::iterator min_idx = min_element(arr.begin(), arr.end());
    arr.erase(min_idx);
    vector<int> answer = arr;
    if (answer.size() == 0)
        answer.push_back(-1);
    return answer;
}