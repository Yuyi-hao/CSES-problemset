#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, x;
    cin >> n >> x;
    vector<int> values(n);
    for(int i = 0; i < n; i++){
        cin >> values[i];
    }
    map<int, int> dct;
    for(int i=0; i< n; i++){
        if(dct.count(x-values[i])){
            cout << i+1 << " " << dct[x-values[i]] << endl;
            return 0;
        }
        dct[values[i]] = i+1;
    }
    cout << "IMPOSSIBLE" << endl;
    return 0;
}