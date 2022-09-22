#include<iostream>
#include<fstream>
#include<vector>
// #include<map>
#include<map>
using namespace std;

class PNTAB{
    public:
    int pcnt;//parameter count
    map<int, string[4]> pntabM;

    void display(){
        for(auto i: pntabM){
            cout << i.first << " ";
            for(int j = 0; j < 4;j++){
                cout << i.second[j] << " ";
            }
            cout << "\n";
        }
        // cout << "\n";
    }



};


class MNT{
    friend class PNTAB;
    
    public:
    // string tab[5];
    int mcnt;//macro count;
    map<int, string[5]> mntM;
    MNT(){
        mcnt = 0;
    }

    void fillMNT(string line, PNTAB& pntab){
        mcnt++;
        //ABC &A, &B=, &C=AREG
        int n = line.size();
        string name = "";
        int pp = 0, kp= 0;
        string curstr = "";
        string paraname = "";
        string paraval = "";
        int paranum = 0;
        cout << line << "\n";


        for(int i = 0; i < n; i++){
            if(line[i] == ' '){
                if(name == ""){
                    name = curstr;
                    mntM[mcnt][0] = name;
                    // cout << "name : " << mntM[mcnt][0] << "\n";
                    // curstr = "";
                    // cout << "name1: " << name << "\n";
                }
                else{
                    paranum++;
                    if(curstr.find("=")!=string::npos){
                        //found
                        string tmp = "";
                        kp++;
                        for(int i = 1; curstr[i] != '\0';i++){
                            if(curstr[i] == '='){
                                paraname = tmp;
                                tmp= "";
                            }
                            else{
                                tmp += curstr[i];
                            }
                        }
                        pntab.pntabM[mcnt][3] = tmp;
                        pntab.pntabM[mcnt][2] = paraname;
                        paraname = "";
                    }
                    else{
                        pp++;
                        paraname = curstr.substr(1);
                        pntab.pntabM[mcnt][2] = paraname;
                        paraname = "";
                    }                    
                }
            }
        }
    }

    void display(){
        for(auto i: mntM){
            cout << i.first << " ";
            for(int j = 0; j < 5; j++){
                cout << i.second[j] << " ";
            }
           cout << "\n"; 
        }

    }

};




class pass1{
    public:
    friend class MNT;
    friend class MDT;
    friend class PNTAB;
    MNT mntab;
    // MDT mdtab;
    // PNTAB pntab;
    fstream asmfile;
    // fstream mntfile;
    // fstream mdtfile;
    int mc;//macro cnt
    
    pass1(){
        asmfile.open("code.asm");
        // mntfile.open("mnt.txt");
        // mdtfile.open("mdt.txt");
        mc = 0;
    }

    void run(){
        string line;
        bool mcro = 0;
        while(asmfile){
            getline(asmfile, line);
            if(line == "MACRO"){
                PNTAB pntb;
                int instcnt = 0;
                getline(asmfile, line);
                do{
                    instcnt++;
                    if(instcnt==1){
                        mntab.fillMNT(line, pntb);
                    }
                    getline(asmfile, line);
                }while(line != "MEND");

                pntb.display();

            }
            else if(line == "MEND"){
                mcro = 0;
            }
        }

        mntab.display();
    }



};

int main(){
    // pass1 p;
    // p.run();
    PNTAB p;
    MNT m;
    m.fillMNT("ABC &A, &B=, &C=AREG", p);
    m.display();
    return 0;
}
