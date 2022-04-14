package JAVA;

import java.util.Arrays;

public class bubbleSort {
    public static void sort(int[] arr){
        final int len = arr.length;
        for(int i=len-1; i>=0; i--){
            for(int j=0; j<i; j++){
                if(arr[j] > arr[j+1]){
                    int tmp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = tmp;
                    System.out.println(Arrays.toString(arr));
                }
            }
        }
    }
    public static void main(String[] args) {
        int[] arr = {5, 3, 8, 9, 10, 1, 0};
        sort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
