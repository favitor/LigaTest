""" 
Write a function that takes as arguments: an array of distinct integers and an integer (target value). 
You need to check if any two numbers of the array sum up to the target value. 
If that's the case, your function should return those two numbers in array fashion. Otherwise, just return an empty array.
"""


def two_sum(array, target):
        # Write your code here
        for i in range(len(array) - 1):
        	for j in range(i + 1, len(array)):
        		if array[i] + array[j] == target:
        			print("Par que some", target, "é: (", array[i],",", array[j],")")
        pass



if __name__=="__main__":
        array_one = [3, 5, -4, 8, 11, 1, -1, 6]
        target = 10

        two_sum(array_one,target)
