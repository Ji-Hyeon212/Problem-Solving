#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int count_divisor(double n){
    int cnt = 0;
    if(fmod(n,sqrt(n))==0) cnt = 1;
    else cnt = 0;
    
    return cnt;
} 

int solution(int left, int right) {
    int num = left;
    int answer = 0;
    while(1){
        if(count_divisor(num)==0) answer+=num;
        else answer-=num;
        num++;
        if(num>right) break;
    }
    return answer;
}