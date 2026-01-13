#include<bits/stdc++.h>
using namespace std;

bool find(const vector<int>& v, int findNumber){
    int l=v[0];
    int r=v.size()-1;

    
    while(l <= r){
        int mid = (l+r)/2;
        if(mid < findNumber){
            l = mid +1;
        }else if(mid > findNumber){
            r = mid - 1;
        }else{
            return true;
        }
    }
    return false;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n,m;
    vector<int> v;
    cin >> n;
    for(int i=0; i<n;i++){
        int temp;
        cin >> temp;
        v.push_back(temp);
    }

    sort(v.begin(),v.end());
    cin >> m;
    for(int i=0;i<m;i++){
        int temp;
        cin >> temp;
        if(find(v,temp)){
            cout << 1 << "\n";
        }else
            cout << 0 << "\n";
    }
    return 0;
}
