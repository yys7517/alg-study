#include<bits/stdc++.h>
using namespace std;
//v는 정점의 개수(최대 1000개)
vector<int> v[1000];
int n,m,a;
//방문배열로 해당 노드를 방문했는지 확인 (dfs)
int visited_dfs[1001];
//방문배열로 해당 노드를 방문했는지 확인 (dfs)
int visited_bfs[1001];

void dfs(int here){
    visited_dfs[here] = 1;
    cout << here << " ";
    //자식들 정렬을 해서 
    sort(v[here].begin(),v[here].end());
    for(int b : v[here]){
        if(visited_dfs[b] == 1) continue;
        dfs(b);
    }
    return;
}

void bfs(int here){
    queue<int> q;
    //우선 시작점에서 방문을 해두기
    //안할경우 시작점으로 돌아올 수 있음
    visited_bfs[here] = 1;
    //시작점을 먼저 큐에 집어넣기
    q.push(here);
    //아래 반복문은 시작점과 연결되어 있는 애들 전부 들릴 수 있음
    while(q.size()){
        //bfs는 너비우선탐색이기에 처음 들어온 녀석이 q.front()에 존재
        int here = q.front();
        cout << here << " ";
        //첫번째 큐에 넣은 가장 최상위 부모는 이제 빼고 그 부모와 연결되어있는 자식들을 q에집어넣어야됨.
        q.pop();
        //자식들을 q에 집어넣기 전에 sort(문제 조건이 같은 레이어에서는 숫자가 작은 노드부터 들러야 하기 때문에)
        sort(v[here].begin(),v[here].end());
        //vector안에 들어있는 자식들을 q에 집어넣음
        for(int b : v[here]){
            //내 자식들끼리 연결되어 있어 방문했던 노드를 방문하면 안되기에 continue
            if(visited_bfs[b]!=0)continue;
            visited_bfs[b]=1;
            q.push(b);
        }
    }

}
int main(){
    //C++ 빠른 입력 위한 메모리 비우기
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    //C++ 입력
    cin >> n >> m >> a;
    for(int i=0; i<m;i++){
        //양방향이기에 각 노드에 푸쉬
        int p,q;
        cin >> p >> q;
        v[p].push_back(q);
        v[q].push_back(p);
    }


    
    dfs(a);
    cout << "\n";
    bfs(a);
    return 0;
}