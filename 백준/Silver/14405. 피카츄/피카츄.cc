#include <iostream>
#include <string>
#include <regex>

using namespace std;

int main(void)
{
    string S;
    cin >> S;
    regex pat("(pi|ka|chu)+");
    if (regex_match(S, pat))
        cout << "YES" << endl;
    else 
        cout << "NO" << endl;
    return 0;
}