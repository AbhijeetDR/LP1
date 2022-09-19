
#include <bits/stdc++.h>
using namespace std;
int strtoint(string s)
{
    int num = 0;
    for (int i = 0; i < s.size(); ++i)
    {
        num *= 10;
        num += (s[i] - '0');
    }
    return num;
}
class Pass2
{
    vector<pair<string, int>> systb;
    vector<pair<int, int>> littb;
    vector<string> word;
    int lc;
    bool flag;
    int sudoLC;

public:
    Pass2()
    {
        lc = 0;
        flag = false;
        sudoLC = 0;
        fstream file;
        string s;
        file.open("systab.txt", ios::in);
        while (getline(file, s))
            systb.push_back({input2(s)[0], strtoint(input2(s)[1])});
        file.close();
        file.open("littab.txt", ios::in);
        while (getline(file, s))
            littb.push_back({strtoint(input2(s)[0]), strtoint(input2(s)[1])});
        file.close();
    }
    vector<string> input2(string read)
    {
        vector<string> word;
        string s1 = "";
        for (int i = 0; i < read.size(); ++i)
        {
            if (read[i] == ' ')
            {
                word.push_back(s1);
                s1 = "";
                continue;
            }
            s1 += read[i];
        }
        word.push_back(s1);
        return word;
    }
    void printTAB()
    {
        cout << "Literal Table \n"
             << endl;
        for (int i = 0; i < littb.size(); ++i)
            cout << i + 1 << " ) " << littb[i].first << " " << littb[i].second << endl;
        cout << endl;
        cout << "SYSTEM Table \n"
             << endl;
        for (int i = 0; i < systb.size(); ++i)
            cout << i + 1 << " ) " << systb[i].first << " " << systb[i].second << endl;
    }
    void MachineCode()
    {
        fstream file;
        string s;
        file.open("pass1.txt", ios::in);
        while (getline(file, s))
        {
            word = input2(s);
            for (int i = 0; i < word.size(); ++i)
                cout << word[i] << " ";
            cout << " ";
            if (word.size() == 0)
                return;
            if (word[0] == "(AD,01)")
            {
                lc = strtoint(word[1].substr(3, 3)); // '(c,200)'
                cout << endl;
                continue;
            }
            if (word[0] == "(AD,02)")
            {
                cout << "           NO MACHINE CODE FOR (AD,02) ";
                cout << endl;
                continue;
            }
            if (word[0] == "(AD,03)")
            {
                flag = true;
                if (word[1][1] == 'L')
                    sudoLC = littb[strtoint(word[1].substr(3, 2)) - 1].second;
                else
                    sudoLC = systb[strtoint(word[1].substr(3, 2)) - 1].second;
                sudoLC += (int)(word[1][word[1].size() - 1] - '0');
                lc = sudoLC;
                cout << "  NO MACHINE CODE FOR (AD,03) ";
                cout << endl;
                continue;
            }
            if (word[0] == "(IS,00)")
            {
                cout << "           " << lc << " " << 00 << " " << 0 << " " << 000;
            }
            if (word[0] == "(DL,01)")
            {
                cout << "     " << lc << "  " << 00 << " " << 0 << " " << 00 << word[1][3]; // (c,2)
            }
            if (word[0] == "(DL,02)")
            {
                cout << "     " << lc;
            }
            if (word[0].substr(1, 2) == "IS" && word[0].substr(4, 2) != "00")
            {
                cout << lc << "  " << word[0].substr(4, 2) << " " << word[1][1] << " ";
                if (word[2][1] == 'L')
                    cout << littb[strtoint(word[2].substr(3, 2)) - 1].second;
                else
                    cout << systb[strtoint(word[2].substr(3, 2)) - 1].second;
            }
            lc++;
            cout << endl;
        }
    }
};
int main()
{

    Pass2 p2;
    cout << "\n\n";
    p2.printTAB();
    cout << "\n\n";
    cout << "        MACHINE CODE \n\n";
    p2.MachineCode();
    cout << "\n\n\n\n";
    return 0;
}
