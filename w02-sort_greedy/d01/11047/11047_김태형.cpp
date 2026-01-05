#include<bits/stdc++.h>
using namespace std;
int n,k;
int cnt;
bool compare1(pair<int, int> a, pair<int, int> b) {

	return a.first > b.first;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> k;
    pair<int,int> arr[n];
    for(int i=0; i<n;i++){
        cin >> arr[i].first;
    }
    sort(arr,arr+n,compare1);
    for(int i=0; i<n;i++){
        if(arr[i].first >k){
            continue;
        }
        arr[i].second = k/arr[i].first;
        k = k % arr[i].first;
        if(k == 0){
            break;
        }
    }
    for(int i=0; i<n;i++){
        cnt+=arr[i].second;
    }
    cout << cnt;
    return 0;
}