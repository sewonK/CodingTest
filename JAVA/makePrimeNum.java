package JAVA;

/*
* 코딩테스트 연습>Summer/Winter Coding(~2018)>소수 만들기
* https://programmers.co.kr/learn/courses/30/lessons/12977
*/
public class makePrimeNum {
    public static void main(String[] args) {
        int[] nums = {1,2,7,6,4};
        Solution1 test = new Solution1();
        System.out.println(test.solution(nums));
    }
}

class Solution1 {
    public boolean isPrime(int num){
        for(int i=2; i*i<num; i++){
            if(num % i == 0) return false;
        }
        return true;
    }

    public int solution(int[] nums) {
        int answer = 0;
        int len = nums.length;
        for(int i=0; i<len; i++){
            for(int j=i+1; j<len; j++){
                for(int k=j+1; k<len; k++){
                    if(isPrime(nums[i]+nums[j]+nums[k])) {
                        answer += 1;
                    }
                }
            }
        }
        return answer;
    }
}