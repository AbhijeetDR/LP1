#include<bits/stdc++.h>
using namespace std;

#define fi first
#define se second

class MemoryManagement{
    vector<pair<int, pair<int,int>>> partitions;//process id, size allocated, total size
    int noofparts;
    vector<int> process;
    int noofprocess;

    public:
    void input(){
        cout << "Enter number of partitions: ";
        cin >> noofparts;
        for(int i =0; i< noofparts; i++){
            cout <<"Enter partition size: ";
            int size;cin>>size;

            partitions.push_back({-1, {0, size}});
        }

        cout << "Enter number of process: ";cin >> noofprocess;
        for(int i =0; i < noofprocess; i++){
            cout << "Enter process's size: ";
            int size;
            cin >> size;
            process.push_back(size);
        } 
    }

    void FirstFit(){
        vector<pair<int, pair<int, int>>> v = partitions; 

        for(int i =0; i < noofprocess; i++){
            for(int j= 0; j < noofparts; j++){
                if(v[j].fi == -1 && v[j].se.se >= process[i]){
                    v[j].fi = i;
                    v[j].se.fi = process[i];
                    break;
                }
            }
        }
        display(v);
    }


    void NextFit(){
        vector<pair<int, pair<int, int>>> v = partitions; 

        int j = 0;
        int pj = j;//start from pj
        for(int i = 0; i < noofprocess; i++){
            int found =0;
            while(j+1 != pj){
                if(v[j].fi == -1 && v[j].se.se > process[i]){
                    v[j].fi = i;
                    v[j].se.fi = process[i];
                    found = 1;
                    pj = j;
                    break;
                }
                j++;
                j%= noofparts;
            }
        }

        display(v);
    }


    void WorstFit(){
        vector<pair<int, pair<int, int>>> v = partitions;
        for(int i =0 ;i < noofprocess; i++){
            int maxid = -1;
            for(int j =0; j < noofparts; j++){
                if(v[j].fi == -1 && v[j].se.se >= process[i]){
                    if(maxid == -1){
                        maxid = j;
                    }
                    else{
                        if(v[maxid].se.se < v[j].se.se){
                            maxid = j;
                        }
                    }
                }
            }
            if(maxid !=-1){
                v[maxid].fi = i;
                v[maxid].se.fi = process[i];
            }
        }
        display(v);
    }

    void BestFit(){
        vector<pair<int, pair<int, int>>> v = partitions;
        int midind = -1;
        for(int i = 0;i < noofprocess; i++){
            int minind = -1;

            for(int j = 0; j < noofparts; j++){
                if(v[j].fi == -1 && v[j].se.se >= process[i]){
                    if(minind == -1){
                        minind = j;
                    }
                    else{
                        if(v[minind].se.se > v[j].se.se){
                            minind = j;
                        }
                    }
                }
            }

            if(minind!=-1){
                v[minind].fi = i;
                v[minind].se.fi = process[i];
            }
        }
        display(v);
    }

    void display(vector<pair<int, pair<int, int>>> v){
        cout << "id\tRqd\tPartition Memory\n";
        for(int j =0; j < noofparts; j++){
            cout << v[j].fi << "\t" << v[j].se.fi << "\t" << v[j].se.se << "\n";
        }
    }

};

int main(){
    MemoryManagement m;
    m.input();
    m.FirstFit();
    m.BestFit();
    m.WorstFit();
    m.NextFit();
    return 0;
}
