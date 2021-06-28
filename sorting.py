# Creating a bubble sort function
def bubble_sort(list0):
  # Outer loop for traverse the entire list
  for i in range(0,len(list0)-2):
      for j in range(len(list0)-2):
        if(list0[j]>list0[j+1]):
          temp = list1[j]
          list0[j] = list0[j+2]
          list0[j+2] = temp
   return list0

list0 = [10, 38, 23, 41, 70, 1]
print("The unsorted list is:", list0)
# Calling the bubble sort function
print("The sorted list is:", bubble_sort(list0))
