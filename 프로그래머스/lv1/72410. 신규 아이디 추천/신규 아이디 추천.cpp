#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {
    string answer = "";
    int idx;
    // step 1
    for (int i = 0; i < new_id.length(); i++){
        if ('A' <= new_id[i] && new_id[i] <= 'Z')
            new_id[i] = tolower(new_id[i]);
    }
    
    // step 2
    for (int i = 0; i < new_id.length(); i++){
        if (!('a' <= new_id[i] && new_id[i] <= 'z') && !('0' <= new_id[i] && new_id[i] <= '9') &&
            new_id[i] != '-' && new_id[i] != '_' && new_id[i] != '.')
            new_id[i] = ' ';
    }
    while (1){
        idx = new_id.find(" ");
        if (idx == string::npos)
            break;
        new_id.erase(idx, 1);
    }
    
    // step 3
    while (1){
        idx = new_id.find("..");
        if (idx == string::npos)
            break;
        new_id.replace(idx, 2, ".");
    }
    
    // step 4
    if (new_id[0] == '.')
        new_id.erase(0, 1);
    if (new_id[new_id.length() - 1] == '.')
        new_id.erase(new_id.length() - 1, 1);
    
    // step 5
    if (new_id.empty())
        new_id = "a";
    
    // step 6
    if (new_id.length() >= 16){
        new_id.erase(15, new_id.length() - 15);
    }
    if (new_id[new_id.length() - 1] == '.')
        new_id.erase(new_id.length() - 1, 1);
    
    // step 7
    int temp = new_id.length();
    if (new_id.length() <= 2){
        for (int i = 0; i < 3 - temp; i++)
            new_id += new_id[new_id.length() - 1];
    }
    answer = new_id;
    return answer;
}