#include <bits/stdc++.h>

using namespace std;

long long N, k, start, ans;
map<long long,long long> mp;

int main(){
    cin >> N;

    start = 0;
    ans = 0;
    for(long long end = 0; end < N; end++){
        cin >> k;
        if (mp.find(k) == mp.end())
            mp.insert({k, end});
        else {
            if(mp[k] >= start)
                start = mp[k] + 1;
            mp[k] = end;
        }
        ans = max(ans, end - start + 1);
    }

    cout << ans << "\n";
    return 0;
}