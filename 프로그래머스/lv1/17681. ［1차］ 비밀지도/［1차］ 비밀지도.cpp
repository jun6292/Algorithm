#include <string>
#include <vector>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    for (int i = 0; i < arr1.size(); i++) {
        int reps = n;
        vector<int> tmp1, tmp2;
        while (reps > 0) {
            if (arr1[i] == 0)
                tmp1.push_back(0);
            else {
                tmp1.push_back(arr1[i] % 2);
                arr1[i] /= 2;
            }
            if (arr2[i] == 0) 
                tmp2.push_back(0);
            else {
                tmp2.push_back(arr2[i] % 2);
                arr2[i] /= 2;
            }
            reps--;
        }
        int idx = tmp1.size() - 1;
        string map = "";
        while (idx > -1) {
            if (tmp1[idx] == 1 && tmp2[idx] == 1)
                map += "#";
            else if (tmp1[idx] == 0 && tmp2[idx] == 0)
                map += " ";
            else
                map += "#";
            idx--;
        }
        answer.push_back(map);
    }
    return answer;
}