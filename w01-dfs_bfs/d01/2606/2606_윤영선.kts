#!/usr/bin/env kotlin

import java.util.LinkedList

fun main() {
    val n = readln().toInt()    // 컴퓨터의 수 n
    val m = readln().toInt()    // 연결된 컴퓨터의 쌍 (간선의 수) m

    val graph = Array(n+1) { IntArray(n+1) }
    val visited = ArrayList<Int>(n+1)

    repeat(m) {
        val (x,y) = readln().split(" ").map { it.toInt() }

        graph[x][y] = 1
        graph[y][x] = 1
    }


    // 바이러스가 퍼진 컴퓨터의 수
    var result = 0

    fun bfs(start: Int) {
        val queue = LinkedList<Int>()
        queue.add(start)
        visited.add(start)

        while(queue.isNotEmpty()) {
            val tmp = queue.poll()

            for(i in 1..n) {
                if(i !in visited && graph[tmp][i] == 1) {
                    queue.add(i)
                    visited.add(i)
                    result++
                }
            }
        }
    }

    // DFS 풀이
    fun dfs(start: Int) {
        visited.add(start)

        for(i in 1..n) {
            if( i !in visited && graph[start][i] == 1) {
                result++
                dfs(i)
            }
        }
    }

    bfs(1)  //  1번으로부터 바이러스가 퍼지기 시작

    println(result)
}