#!/usr/bin/env kotlin

import java.util.*

fun main() {
    val(M, N) = readLine()!!.split(" ").map { it.toInt() }

    val arr = Array(M) {
        val st = StringTokenizer(readLine()!!, " ")
        IntArray(N) { st.nextToken().toInt() }
    }

    val dp = Array(M) { IntArray(N) }

    val visited = Array(M) { BooleanArray(N) }

    val dx = arrayOf(-1,1,0,0)
    val dy = arrayOf(0,0,-1,1)

    fun dfs(startX: Int, startY: Int) {
        visited[startX][startY] = true
        print("${arr[startX][startY]} ")

        if(arr[startX][startY] == arr[M-1][N-1]) {
            println()
            visited[M-1][N-1] = false

            dp[M-1][N-1]++
        }


        for(i in 0 until 4) {
            val nx = startX + dx[i]
            val ny = startY + dy[i]

            if( nx >= 0 && nx < M && ny >= 0 && ny < N ) {
                if(arr[startX][startY] > arr[nx][ny] ) {
                    if( !visited[nx][ny] ) {
                        dfs(nx, ny)
                    }
                }
            }
        }
    }

    for(i in 0 until M) {
        for(j in 0 until N) {
            dfs(i, j)
        }
    }

    println("count: ${dp[M-1][N-1]}")

}