#include<bits/stdc++.h>
using namespace std;
int n;
vector<int> v;
int main(){
    //빠른 입출력
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for(int i=0; i<n;i++){
        int temp;
        cin >> temp;
        v.push_back(temp);
    }
    sort(v.begin(),v.end());
    for(int i=0; i<n;i++){
        cout << v[i] << "\n";
    }
    
    
    return 0;
}