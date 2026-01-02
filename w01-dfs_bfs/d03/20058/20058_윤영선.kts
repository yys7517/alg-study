#!/usr/bin/env kotlin

import java.io.*
import java.util.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (N, Q) = br.readLine()!!.split(" ").map { it.toInt() }

    // 2^n값 구하기
    fun getLength(n : Int): Int{
        var len = 1
        for (i in 0 until n) {
            len *= 2
        }

        return len
    }

    var len = getLength(N)

    val A = Array(len) { IntArray(len) }

    for(i in 0 until len) {
        val st = StringTokenizer(br.readLine()!!, " ")

        for(j in 0 until len) {
            A[i][j] = st.nextToken().toInt()
        }
    }


    // 마법사가 시전하는 파이어스톰 단계
    val operList = br.readLine()!!.split(" ").map { it.toInt() }

    for( n in 0 until Q ) {
        val t = operList[n]

        // 시계방향 90도 배열 회전
        // 4x4 배열에서
        // [0, 0] -> [0, 3]
        // [0, 1] -> [1, 3]
        // [0, 2] -> [2, 3]
        // [0, 3] -> [3, 3]

        // [1, 0] -> [0, 2]
        // [1, 1] -> [1, 2]
        // [1, 2] -> [2, 2]

        // [i, j] -> [j, size - 1 - i]
        val l = getLength(t)

        val newBoard = Array(len) { IntArray(len) }
        for(i in 0 until l) {
            for(j in 0 until l) {
                newBoard[j][l - 1 - i] = A[i][j]
            }
        }

        for(i in 0 until l) {
            for(j in 0 until l) {
                print(newBoard[i][j].toString() + " ")
            }
            println()
        }
    }
}