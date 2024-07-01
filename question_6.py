'''Paul is given an array A of length N. He must perform the following Operations on the
array sequentially:
* Choose any two integers from the array and calculate their average.
* If an element is less than the average, update it to 0. However, if the element is
greater than or equal to the average, he need not update it.
Your task is to help Paul find and return an integer value, representing the minimum
possible sum of all the elements in the array by performing the above operations. Note: An exact average should be calculated, even if it results in a decimal.
Input Format:
input1: An integer value N, representing the size of the array A.
input2: An integer array A.
Output Format:
Return an integer value, representing the minimum possible sum of all the elements
in the array by
Sample Input
5
1 2 3 4 5
Sample Output
5'''

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
ele_1=arr[-1]
ele_2=arr[-2]
avg=(ele_1+ele_2)/2
sum=0
for i in range(len(arr)):
    if(arr[i]>=avg):
        sum=sum+arr[i]
print(sum)