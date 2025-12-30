#include<bits/stdc++.h>
using namespace std;
//노드의 최대 수
int arr[101];
//노드랑 연결된 애들을 자식에 넣기 위해 vector
vector<int> v[101];
//방문배열
int visited[101];
//전역변수로 선언(하면 디폴트값 0)
int sum;
//sum을 반환하는 dfs
int dfs(int here){
    visited[here] = 1;
    for(int b : v[here]){
        if(visited[b]!=0) continue;
        sum++;
        visited[b] =1;
        
        dfs(b);
    }
    return sum;

}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    // for(int i=1; i<=n;i++){
    //     arr[i] = i;
    // }
    for(int i=1; i<=n;i++){
        int p,q;
        cin >> p >> q;
        v[p].push_back(q);
        v[q].push_back(p);
    }

    cout << dfs(1);

}