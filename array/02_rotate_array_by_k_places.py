"""
PROBLEM 1: LEFT ROTATE THE ARRAY BY ONE PLACE
---------------------------------------------

input_arr = [1, 2, 3, 4, 5]
output_arr = [2, 3, 4, 5, 1]
"""

def left_rotate_once(arr):
	n = len(arr)
	first_element = arr[0]
	for i in range(1, n):
		arr[i-1] = arr[i]
	arr[-1] = first_element
	return arr

input_arr = [1, 2, 3, 4, 5]
print(f"left_rotate_once: {left_rotate_once(input_arr)}")


"""
PROBLEM 2: LEFT ROTATE THE ARRAY BY D PLACES
---------------------------------------------

input_arr = [1, 2, 3, 4, 5, 6, 7], d = 2
output_arr = [3, 4, 5, 6, 7, 1, 2]
"""

def bruteforce_rotate_left_by_d_places(arr, d):
	n = len(arr)
	if d > n:
		d = d % n

	temp = []
	for i in range(d):
		temp.append(arr[i])

	for i in range(d, n):
		arr[i-d] = arr[i]

	for i in range(d):
		# print(n-d+i)
		arr[n-d+i] = temp[i]

	# arr[n-d:n-1] = temp
	return arr

def bruteforce_striver(arr, d):
	n = len(arr)
	temp = arr[:d]
	# print(f"arr: {arr}")
	# print(f"temp: {temp}")
	# print(f"arr[:d]: {arr[:d]}")

	# shifting
	for i in range(d, n):
		arr[i-d] = arr[i]

	for i in range(n-d, n):
		arr[i] = temp[i-(n-d)]
	return arr

"""
LEFT ROTATE BY D PLACES OPTIMAL

OBSERVATION:
arr = [1, 2, 3, 4, 5, 6, 7], d = 3

rotate first 3 -> 3, 2, 1
rotate last elements -> 7, 6, 5, 4
so resultant arr = [3, 2, 1, 7, 6, 5, 4]

now reverse this entire array: [4, 5, 6, 7, 1, 2, 3] -> RESULTANT ARRAY

------
steps:
------
	reverse(0, d) -> reverse 0 to d
	reverse(d, n) -> reverse d to n
	reverse(0, n) -> reverse 0 to n
"""

def reverse(arr, start, end):
	while start < end:
		arr[start], arr[end] = arr[end], arr[start]
		start += 1
		end -= 1

def optimal_rotate_by_d_places(arr, d):
	n = len(arr)
	if d > n:
		d = d % n
	reverse(arr, 0, d-1)
	reverse(arr, d, n-1)
	reverse(arr, 0, n-1)
	return arr




input_arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
print(f"Rotate input array by d places: {bruteforce_rotate_left_by_d_places(input_arr, d)}")
input_arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
print(f"Rotate left by d places striver: {bruteforce_striver(input_arr, d)}")

input_arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
print(f"Optimal rotate by d places: {optimal_rotate_by_d_places(input_arr, d)}")



"""
PROBLEM 3: MOVE ALL ZEROES TO THE END OF THE ARRAY
---------------------------------------------

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
output = [1, 2, 3, 2, 4, 5, 1, 0, 0, 0]


--------------
BRUTE APPROACH
--------------
store non zeroes somewhere
temp -> [1, 2, 3, 2, 4, 5, 1]

now modify the original array, put temp array at front of original array
arr = [1, 2, 3, 2, 4, 5, 1, 4, 5, 1]

now the remaining positions (last 3 elements need to be zero)
final output arr:
arr = [1, 2, 3, 2, 4, 5, 1, 0, 0, 0]
"""

def brute_zeroes_at_end(arr):
	n = len(arr)
	temp = []
	for i in range(n):
		if arr[i] != 0:
			temp.append(arr[i])

	for i in range(len(temp)):
		arr[i] = temp[i]

	for i in range(len(temp), n):
		arr[i] = 0
	return arr

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
print(f"Brute zeroes at end: {brute_zeroes_at_end(arr)}")



"""
OPTIMAL SOLUTION

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

-> 2 pointer approach
	-> traverse the array with i making sure i uses non-zero numbers
	-> j is updated only when we find a non-zero number
"""

def optimal_move_zeroes_to_end(arr):
	n = len(arr)
	j = -1

	for i in range(n):
		if arr[i] == 0:
			j = i
			break

	for i in range(j+1, n):
		if arr[i] != 0:
			# swap(arr[i], arr[j])
			arr[i], arr[j] = arr[j], arr[i]
			j += 1
	return arr

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
print(f"Optimal zeroes at end: {brute_zeroes_at_end(arr)}")




"""
PROBLEM 4: LINEAR SEARCH
------------------------

arr = [6, 7, 8, 4, 1], num = 4
return index at which element is present, here answer = 3
"""




"""
PROBLEM 5: UNION OF TWO SORTED ARRAYS
------------------------

give me a union array, add all the elements, but you don't repeat any element

example 1:
----------
arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5]

union = [1, 2, 3, 4, 5]


example 2:
----------
arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]

union = [1, 2, 3, 4, 5, 6]


----------------
brute approach:
----------------
unique -> map or set
	- add elements into the set from arr1
	- add elements into the set from arr2
	- return the final set
"""

def brute(arr1, arr2):
	res = set()
	for num in arr1:
		res.add(num)
	for num in arr2:
		res.add(num)
	return list(res)


"""
OPTIMAL: 2 POINTER APPROACH

        i
arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]
        j


"""
def optimal_self(arr1, arr2):
	res = []
	i, j = 0, 0
	n = len(arr1)
	m = len(arr2)

	while i < n and j < m:
		if arr1[i] <= arr2[j]:
			if i > 0 and arr[i] != res[-1]:
				res.append(arr1[i])
			else:
				res.append(arr1[i])
			i += 1
		else:
			if j > 0 and arr[j] != res[-1]:
				res.append(arr2[j])
			else:
				res.append(arr2[j])
			j += 1

	if i < n:
		while i < n:
			res.append(arr1[i])
			i += 1
	if j < m:
		while j < m:
			res.append(arr2[j])
			j += 1
	return res


def optimal2(nums1, nums2):
    res = []
    n, m = len(nums1), len(nums2)
    i, j = 0, 0

    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            if len(res) == 0 or res[-1] != nums1[i]:
                res.append(nums1[i])
            i += 1
        else:
            if len(res) == 0 or res[-1] != nums2[j]:
                res.append(nums2[j])
            j += 1
    # if i is exhausted
    while j < m:
        if len(res) == 0 or res[-1] != nums2[j]:
            res.append(nums2[j])
        j += 1
    
    # if j is exhausted
    while i < n:
        if len(res) == 0 or res[-1] != nums1[i]:
            res.append(nums1[i])
        i += 1
    return res

arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]
print(f"Brute union 2 array: {brute(arr1, arr2)}")
print(f"[NOT WORKING] Optimal union 2 array: {optimal_self(arr1, arr2)}")
print(f"[STRIVER WORKING] Optimal union 2 array: {optimal2(arr1, arr2)}")




"""
PROBLEM 6: INTERSECTION OF TWO SORTED ARRAYS
-------------------------------------
-> give me the elements that are present in both the array

a = [1, 2, 2, 3, 3, 4, 5, 6]
b = [2, 3, 3, 5, 6, 6, 7]

intersection = [2, 3, 3, 5, 6]


BRUTE FORCE SOLUTION
--------------------
- for every element in first array, search for same corresponding element in second array
	- keep track if someone has been used previously or not
	- keep a visited array to track numbers used in the second array
		- zero (0) -> means that element has not been visited/used yet
		- one  (1) -> means that element has been visited/used

"""

def intersection_brute(a, b):
	n, m = len(a), len(b)
	res = []
	visited = [0 for i in range(m)]

	for i in range(n):
		for j in range(m):
			if a[i] == b[j] and visited[j] == 0:
				res.append(b[j])
				visited[j] = 1
				break
			if b[j] > a[i]:
				break
	return res


"""
OPTIMAL APPROACH -> TWO POINTER APPROACH
----------------
-> i at beginning of a
-> j at beginning of b

-> if equal, add to res
-> if a[i] < b[j] -> increment i to increase a[i] (because it's sorted), so that it can match b[j]
-> if a[i] > b[j] -> increment j to increase b[j] (because it's sorted), so that it can match a[i]
"""

def intersection_optimal(a, b):
	n, m = len(a), len(b)
	i, j = 0, 0
	res = []

	while i < n and j < m:
		if a[i] == b[j]:
			res.append(a[i])
			i += 1
			j += 1
		elif a[i] < b[j]:
			i += 1
		elif a[i] > b[j]:
			j += 1
	return res

a = [1, 2, 2, 3, 3, 4, 5, 6]
b = [2, 3, 3, 5, 6, 6, 7]

print(f"intersection brute: {intersection_brute(a, b)}")
print(f"intersection optimal: {intersection_optimal(a, b)}")