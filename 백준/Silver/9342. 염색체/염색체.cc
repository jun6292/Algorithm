#include <iostream>
#include <string>
#include <regex>

using namespace std;

int main(void)
{
    int T;
    cin >> T;
    regex pat("^[A-F]?A+F+C+[A-F]?$");
    for (int i = 0; i < T; i++) {
        string str;
        cin >> str;
        if (regex_match(str, pat))
            cout << "Infected!" << endl;
        else 
            cout << "Good" << endl;
    }
    return 0;
}