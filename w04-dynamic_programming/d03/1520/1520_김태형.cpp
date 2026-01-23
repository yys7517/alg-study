#include <bits/stdc++.h>
using namespace std;
//경로의 개수를 구하니 dfs
//dp는 점화식,메모이제이션...어떻게하지?
//일단 dfs하면서 y-1,x-1에 도달하면되는데
//dfs하는 과정은 나보다 작은애들을 담으면서 가기
//담으면서 가는데 들렀던데는 continue;
//아니다 담을 필요없이 visited라는 2차원 배열을 만들고
//방문했을 경우 값을 변경해주고 값을 매번 초기화?

// C++은 전역변수와 로컬변수의 초기값이 다릅니다.
// 전역변수에 선언할 경우 초기값이 0으로 잡히는데
// 로컬변수로 선언할 경우 초기값에 주소값이 껴서 0이 아니게 됩니다.


int dy[4] = {1,0,-1,0};
int dx[4] = {0,1,0,-1};
int n,m;
//n,m의 최대값
int a[501][501];


//각 칸마다 dfs를 실행해서 n-1,m-1이 되는 값을 
//저장할 수 있는(그래야 내리막길이니까)
//dp 배열
//dp 배열요소들의 값이 전부 0
int dp[501][501];


int dfs(int y, int x){
    //기저사례
    //기저사례에서 뭔가 액션이 필요한거같은데
    //이러면 어디다가 계속 더해줘야지 -> 새로운 2차원배열을 만들자
    if(y == n-1 && x == m-1) return 1;
    //값이 존재하면 dp 그대로 반환
    if(dp[y][x]) return dp[y][x];
    
    for(int i=0; i<4;i++){
        int ny = y+dy[i];
        int nx = x+dx[i];
        if(ny >= n || nx >= m || ny < 0 || nx < 0) continue;
        
        if(a[ny][nx] < a[y][x]){
            //dfs시작하는 곳에서 내리막길의 조건을 포함하는애들을 더해보자.
            dp[y][x] += dfs(ny,nx);
        }
    }
    return dp[y][x];
    
}

int main(){
    cin >> n >> m;
    for(int i=0; i<n;i++){
        for(int j=0;j<m;j++){
            cin >> a[i][j];
        }
    }
    cout << dfs(0,0);
    return 0;
}

