import java.util.LinkedList

fun main() {

    val (n, m, v) = readln().split(" ").map { it.toInt() }
    val graph = Array(n+1) { IntArray(n+1) }
    var visited = ArrayList<Int>(n+1)

    repeat(m) {
        val (x,y) = readln().split(" ").map { it.toInt() }

        graph[x][y] = 1
        graph[y][x] = 1
    }

    fun dfs(start: Int) {
        visited.add(start)
        print("$start ")

        for(i in 1..n) {
            if(i !in visited && graph[start][i] == 1) {
                dfs(i)
            }
        }
    }

    // 첫 번째 줄에 DFS 결과를
    dfs(v)

    println()

    // 방문 배열 초기화
    visited = ArrayList()

    fun bfs(start: Int) {
        val queue = LinkedList<Int>()
        queue.add(start)
        visited.add(start)    // 출발 정점 번호를 다시 큐에 담지 않기 위해서

        while(queue.isNotEmpty()) {
            val tmp = queue.poll()
            print("$tmp ")

            for(i in 1..n) {
                if( i !in visited && graph[tmp][i] == 1) {
                    queue.add(i)
                    visited.add(i)  // 큐에 담은 정점의 번호들을 다시 큐에 삽입하지 않기 위해서
                }
            }
        }
    }

    // 마지막 줄에는 BFS 결과를 출력
    bfs(v)
}