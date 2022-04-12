package JAVA;

import java.util.Arrays;

/*
 * 프로그래머스 코딩테스트 연습 > 2021 Dev-Matching: 웹 백엔드 개발자(상반기) >로또의 최고 순위와 최저 순위
 *  https://programmers.co.kr/learn/courses/30/lessons/77484?language=java
 */

public class lotto {
    public static void main(String[] args) {
        int[] lottos = {44, 1, 0, 0, 31, 25};
        int[] win_nums = {31, 10, 45, 1, 6, 19};
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.solution(lottos, win_nums)));
    }
}

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0, 0};
        int[] rank = {6, 6, 5, 4, 3, 2, 1};
        int cnt_zero = 0;
        int score = 0;
        for(int lotto: lottos){
            if (lotto == 0) {
                cnt_zero += 1;
                continue;
            }

            for(int num: win_nums){
                if (lotto == num) score += 1;
            }
        }
        
        answer[0] = rank[score + cnt_zero];
        answer[1] = rank[score];
        return answer;
    }
}
