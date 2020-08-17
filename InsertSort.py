
'''
Pseudocode
INSERTION-SORT(A)
   for i = 1 to n
   	key ← A [i]
    	j ← i – 1
  	 while j > = 0 and A[j] > key
   		A[j+1] ← A[j]
   		j ← j – 1
   	End while
   	A[j+1] ← key
  End for
'''

def insertionSort(myarr):
    for i in range(1,len(myarr)):
        key = myarr[i]
        #Move the element myarr[0,i-1] that are greater than key to 1 position from their current position.
        j= i-1
        while j >=0 and key < myarr[j]:
            myarr[j+1] = myarr[j]
            j -=1
        #Place the element
        myarr[j+1] = key
if __name__== "__main__":
    # Driver code to test above
    arr = [12, 11, 13, 5, 6, 9]
    print("Input Array is :",end=' ')
    for i in range(len(arr)):
        print(arr[i],end=' ')
    print(" ")
    insertionSort(arr)
    print ("Sorted array is :",end=' ')
    for i in range(len(arr)):
        print (arr[i], end=' ')
      
 '''
 Time Complexity
 Worst Case Time Complexity [ Big-O ]: O(n2)
Best Case Time Complexity [Big-omega]: O(n)
Average Time Complexity [Big-theta]: O(n2)
 '''
