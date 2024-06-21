package 실패율;

import java.util.*;
import java.util.stream.Collectors;

public class Solution {

    public static void main(String[] args) {
//        int[][] arr1 =  {{1, 4}, {3, 2}, {4, 1}};
//        int[][] arr2 = {{3, 3}, {3, 3}};

        int[] stages = {2,1,2,6,2,4,3,3};
        int[] result = solution(5,stages);
//        System.out.println("result = " + result);

    }

    public static int[] solution(int N, int[] stages) {
        int[] answer = {};


        Deque<Integer> deque = Arrays.stream(stages)
                .boxed()
                .sorted()
                .collect(Collectors.toCollection(ArrayDeque::new));



        Arrays.sort(stages);



        int count = 0;
        int num = stages[0];
        ArrayList<Double> arrayList = new ArrayList<>();
        //get이라 좀 느릴지도?
        for (int i = 0; i < stages.length ; i++) {
            if(num == stages[i]){
                deque.removeFirst();
            }
            else if(num!=stages[i]){
                double rate = (count / (double) Integer.sum(deque.size(), count)) * 100;

                //키 값으로 hashMap
                System.out.println("\n");
                arrayList.add(rate);
                count=0;
                num = stages[i];
                deque.removeFirst();

                if(deque.size()==0){
                    arrayList.add(0.0);
                }
            }
            count++;
        }
        System.out.println(arrayList);


        return answer;
    }

}
