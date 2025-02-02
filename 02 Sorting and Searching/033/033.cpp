#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll solve(ll N, vector<ll>& cubes)
{
    ll ans = 0;

    multiset<ll> topElements;
    for (int i = 0; i < N; i++) {
        auto it = topElements.upper_bound(cubes[i]);
        if (it == topElements.end()) {
            ans++;
            topElements.insert(cubes[i]);
        }
        else {
            topElements.erase(it);
            topElements.insert(cubes[i]);
        }
    }
    return ans;
}

int main()
{
    int N, k;
    cin >> N;
    vector<ll> tower;
    for(int i=0; i < N; i++){
        cin >> k;
        tower.push_back(k);
    }
    cout << solve(N, tower);
    return 0;
}