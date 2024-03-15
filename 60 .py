#!/usr/bin/env python
# coding: utf-8

# **1-Write a Python program to calculate the length of a string using 2 ways

# In[4]:


myname = "Ranim Elgohary"
print(len(myname))
## another way len("Ranim")


# In[3]:


def mytxt(str):
    return len(str)

Text = mytxt("Ranim Elgohary")
print(Text)


# **2-Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead ("##Sample String : 'w3resource'
# Expected Result : 'w3ce'
# ##Sample String : 'w3'
# Expected Result : 'w3w3'
# ##Sample String : ' w'
# Expected Result : Empty String)

# In[7]:


sample_String = ['w3resource', 'w3', 'w']
for S in sample_String:
    if len(S)< 2 :
        print("empty string")
    else:
        print(S[:2]+S[-2:])


# **3-Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. (Sample String : 'abc'
# Expected Result : 'abcing')

# In[19]:


String = "abc" 
if len(String) >=3:
    if String.endswith("ing"):
        Result = String + "ly" 
    else:
        Result = String + "ing"
else:
    Result = String
print(Result)


# **4-Write a Python function that takes a list of words and return the longest word and the length of the longest one
# (Longest word: Exercises
# Length of the longest word: 9)

# In[20]:


def find_longest_word(words):
    if not words:
        return None 
    longest_word = max(words , key = len)
    len_of_the_longest_word = len(longest_word)
    
    return longest_word , len_of_the_longest_word 

wordList = ["Happy" , "More" , "Word" , "Hallo"]
longest_word , len_of_the_longest_word = find_longest_word(wordList)
print(longest_word)
print(len_of_the_longest_word)


# **5-Write a Python program to change a given string to a newly string where the first and last chars have been exchanged using 2 ways (Sample String:abca  Expected Result:ebce)

# In[7]:


def exchange_chars_method1(text):
    if len(text) < 2:
        return text
    else:
        return text[-1] + text[1:-1] + text[0]

sample_string = "abca"
result = exchange_chars_method1(sample_string)
print("Result using Method 1:", result)


# In[6]:


def exchange_chars_method2(text):
    if len(text) < 2:
        return text
    else:
        return text[-1] + text[1:len(text)-1] + text[0]

sample_string = "abca"
result = exchange_chars_method2(sample_string)
print("Result using Method 2:", result)


# **6-Write a Python program to remove characters that have odd index values in a given string (Sample String:abca Expected Result:ac)

# In[1]:


sample_string = "abca"
result_string = sample_string[::2]
print("Sample String:", sample_string)
print("Expected Result:", result_string)


# **7-Write a Python program to count the occurrences of each word in a given sentence (Sample String:amr and ahmed are frindes but amr is the tallest Expected Result:2)

# In[7]:


def count_word(sentence):
    words = sentence.split()
    return {word: words.count(word) for word in set(words)}
sentence = "amr and ahmed are friends but amr is the tallest"
result = count_word_occurrences(sentence)

for word, count in result.items():
    print(f"{word}: {count}")


# **8-Write a Python script that takes input from the user and displays that input back in upper and lower cases

# In[8]:


S = input("Enter a string: ")
print(S.upper())
print(S.lower())


# **9-Write a Python function to reverse a string if its length is a multiple of 4

# In[9]:


def reverse_if_multiple_of_four(input_str):
    if len(input_str) % 4 == 0:
        return input_str[::-1]
    else:
        return input_str

sample_string = "abcdefg"
result = reverse_if_multiple_of_four(sample_string)
print("Result:", result)


# **10- Write a Python program to remove a newline in Python

# In[10]:


def remove_newline(input_str):
    return input_str.replace("\n", "")
sample_string = "This is a string with a newline.\n"
result = remove_newline(sample_string)

print("Original String:")
print(sample_string)


# **11-Write a Python program to check whether a string starts with specified characters

# In[5]:


def starts_with(text, prefix):
    return text.startswith(prefix)

text = "Hello, world!"
prefix = "Hello"
if starts_with(text, prefix):
    print(f'The string "{text}" starts with "{prefix}"')
else:
    print(f'The string "{text}" does not start with "{prefix}"')


# **12- Write a Python program to add prefix text to all of the lines in a string

# In[4]:


def add_prefix_to_lines(text, prefix):
    lines = text.split('\n') 
    prefixed_lines = [prefix + line for line in lines] 
    return '\n'.join(prefixed_lines)  

text = """Line 1
Line 2
Line 3"""
prefix = "Prefix: "
prefixed_text = add_prefix_to_lines(text, prefix)
print(prefixed_text)


# **13-Write a Python program to print the following numbers up to 2 decimal places

# In[3]:


numbers = [3.14159, 42.567, 987.654321]

for number in numbers:
    print(f"{number:.2f}")


# **14-Write a Python program to print the following numbers up to 2 decimal places with a sign

# In[2]:


numbers = [3.14159, -42.567, 987.654321]

for number in numbers:
    print(f"{number:+.2f}")


# **15-Write a Python program to display a number with a comma separator

# In[1]:


number = 1000000
formatted_number = "{:,}".format(number)
print(formatted_number)


# **16-Write a Python program to reverse a string using 2 ways

# In[11]:


def reverse_string(input_string):
    return input_string[::-1]
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print("Reversed String:", reversed_string)


#  **17-Write a Python program to count repeated characters in a string (hint:use dictionary)

# In[12]:


def count_repeated_characters(input_string):
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            print(f"Character '{char}' is repeated {count} times.")
input_string = "programming is fun"
count_repeated_characters(input_string)


# **18-Write a Python program to find the first non-repeating character in a given string

# In[13]:


def first_non_repeating_character(input_string):
    char_count = {}
    
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in input_string:
        if char_count[char] == 1:
            return char
    
    return None

input_string = "programming"
result = first_non_repeating_character(input_string)

if result is not None:
    print(f"The first non-repeating character is: {result}")
else:
    print("No non-repeating character found in the given string.")


# **19-Write a Python program to remove spaces from a given string

# In[14]:


def remove_spaces(input_string):
    return input_string.replace(" ", "")

original_string = "This is a test string."
string_without_spaces = remove_spaces(original_string)

print("Original String:", original_string)
print("String without Spaces:", string_without_spaces)


# **20-Write a Python program to count the number of non-empty substrings of a given string

# In[15]:


def count_substrings(input_string):
    n = len(input_string)
    count = n * (n + 1) // 2
    return count

original_string = "abcdefg"
number_of_substrings = count_substrings(original_string)

print(f"The number of non-empty substrings for '{original_string}' is: {number_of_substrings}")


# **21-write a Python program to swap first and last element of any list.

# In[16]:


def swap_first_and_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]

original_list = [1, 2, 3, 4, 5]
print("Original List:", original_list)

swap_first_and_last(original_list)
print("List after swapping first and last elements:", original_list)


# **22-Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. (Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90])

# In[17]:


def swap_elements_by_positions(lst, pos1, pos2):
    if 0 <= pos1 < len(lst) and 0 <= pos2 < len(lst):
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

original_list = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

print("Original List:", original_list)
print(f"Swap elements at positions {pos1} and {pos2}")
swap_elements_by_positions(original_list, pos1, pos2)
print("List after swapping:", original_list)


# **23- search for the all ways to know the length of the list

# In[ ]:


**24-write a Python code to find the Maximum number of list of numbers.


# In[18]:


def find_maximum_number(lst):
    if not lst:
        return None  
    return max(lst)

number_list = [23, 65, 19, 90, 42, 8, 56]

max_number = find_maximum_number(number_list)

if max_number is not None:
    print(f"The maximum number in the list is: {max_number}")
else:
    print("The list is empty.")


# In[ ]:


**25-write a Python code to find the Minimum number of list of numbers.


# In[19]:


def find_minimum_number(lst):
    if not lst:
        return None  
    return min(lst)

# Example usage
number_list = [23, 65, 19, 90, 42, 8, 56]

min_number = find_minimum_number(number_list)

if min_number is not None:
    print(f"The minimum number in the list is: {min_number}")
else:
    print("The list is empty.")


# **26-search for if an elem is existing in list

# In[20]:


def is_element_in_list(lst, element):
    return element in lst

number_list = [23, 65, 19, 90, 42, 8, 56]
search_element = 42

if is_element_in_list(number_list, search_element):
    print(f"The element {search_element} is present in the list.")
else:
    print(f"The element {search_element} is not present in the list.")


# **27- clear python list using different ways

# In[21]:


my_list = [1, 2, 3, 4, 5]
my_list.clear()
print("List after clearing using clear():", my_list)


# **28-remove duplicated elements from a list

# In[22]:


def remove_duplicates(lst):
    return list(set(lst))

original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
list_without_duplicates = remove_duplicates(original_list)

print("Original List:", original_list)
print("List without Duplicates:", list_without_duplicates)


# **29-Given list values and keys list, convert these values to key value pairs in form of list of dictionaries. (Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}])

# In[24]:


def convert_to_key_value_pairs(value_list, key_list):
    result_list = []
    
    if len(value_list) == len(key_list):
        # Using zip to iterate over both lists simultaneously
        for values in zip(value_list, key_list):
            result_list.append({key_list[0]: values[0], key_list[1]: values[1]})
    
    return result_list

# Example usage
test_list = ["Gfg", 3, "is", 8]
key_list = ["name", "id"]

result = convert_to_key_value_pairs(test_list, key_list)
print("Output:", result)


# **30-write a python program to count unique values inside a list using different ways

# In[25]:


def count_unique_values_set(lst):
    unique_values = set(lst)
    count = len(unique_values)
    return count

my_list = [1, 2, 3, 2, 4, 5, 1, 6]
unique_count = count_unique_values_set(my_list)
print("Method 1: Count of unique values using set:", unique_count)


# **31-write a python program Extract all elements with Frequency greater than K (Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
# Output : [4, 3] )

# In[26]:


def extract_elements_with_frequency(lst, k):
    element_frequency = {}
    
    for element in lst:
        element_frequency[element] = element_frequency.get(element, 0) + 1
    
    result_list = [element for element, frequency in element_frequency.items() if frequency > k]
    
    return result_list

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k_value = 3

result = extract_elements_with_frequency(test_list, k_value)
print("Output:", result)


# **32-write a python program to find the Strongest Neighbour (Input: 1 2 2 3 4 5
# Output: 2 2 3 4 5)

# In[27]:


def find_strongest_neighbor(lst):
    n = len(lst)
    result_list = []

    if n == 1:
        return lst

    for i in range(n - 1):
        result_list.append(max(lst[i], lst[i + 1]))

    return result_list

input_list = [1, 2, 2, 3, 4, 5]

output_list = find_strongest_neighbor(input_list)
print("Input List:", input_list)
print("Strongest Neighbors:", output_list)


# **33-write a Python Program to print all Possible Combinations from the three Digits (Input: [1, 2, 3]
# Output:
# 1 2 3 ##
# 1 3 2 ##
# 2 1 3 ##
# 2 3 1 ##
# 3 1 2 ##
# 3 2 1)

# In[28]:


from itertools import permutations

def print_all_combinations(digits):
    # Generate all permutations of the given digits
    all_permutations = permutations(digits)
    
    for perm in all_permutations:
        print(" ".join(map(str, perm)), "##")

input_digits = [1, 2, 3]
print("Input Digits:", input_digits)
print("Output:")
print_all_combinations(input_digits)


# **34-write a Python program to find all the Combinations in the list with the given condition (Input: test_list = [1,2,3] 
# Output: 
#  [1], [1, 2], [1, 2, 3], [1, 3]
#  [2], [2, 3], [3])

# In[29]:


from itertools import combinations

def find_combinations_with_condition(lst):
    result_list = []
    
    for r in range(1, len(lst) + 1):
        combinations_list = combinations(lst, r)
        result_list.extend(list(combinations_list))
    
    return result_list

test_list = [1, 2, 3]
result = find_combinations_with_condition(test_list)

for combination in result:
    print(list(combination))


# **35-write a Python program to get all unique combinations of two Lists (List_1 = ["a","b"]
# List_2 = [1,2]
# Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] )

# In[30]:


from itertools import product

def get_unique_combinations(list_1, list_2):
    return [list(zip(list_1, perm)) for perm in product(list_2, repeat=len(list_1))]

List_1 = ["a", "b"]
List_2 = [1, 2]

Unique_combination = get_unique_combinations(List_1, List_2)

print("List_1:", List_1)
print("List_2:", List_2)
print("Unique Combinations:", Unique_combination)


# **36-Remove all the occurrences of an element from a list in Python (Input : 1 1 2 3 4 5 1 2 1 
# 
# **Output : 2 3 4 5 2)

# In[31]:


def remove_all_occurrences(lst, element_to_remove):
    return [elem for elem in lst if elem != element_to_remove]

input_list = [1, 1, 2, 3, 4, 5, 1, 2, 1]
element_to_remove = 1

result_list = remove_all_occurrences(input_list, element_to_remove)

print("Input List:", input_list)
print("Element to Remove:", element_to_remove)
print("List after removing all occurrences:", result_list)


# **37-write a python program to Replace index elements with elements in Other List (The original list 1 is : [‘Gfg’, ‘is’, ‘best’] The original list 2 is : [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0] The lists after index elements replacements is : [‘Gfg’, ‘is’, ‘best’, ‘is’, ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘best’, ‘is’, ‘is’, ‘best’, ‘Gfg’])

# In[32]:


def replace_elements_with_other_list(list_1, list_2):
    for index in list_2:
        if index < len(list_1):
            list_1[index] = list_1[index][::-1]  


original_list_1 = ['Gfg', 'is', 'best']
original_list_2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

print("The original list 1 is:", original_list_1)
print("The original list 2 is:", original_list_2)

replace_elements_with_other_list(original_list_1, original_list_2)

print("The lists after index elements replacements is:", original_list_1)


# **38- write python program to Retain records with N occurrences of K(Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 2 
# Output : [(4, 5, 5, 4)]
# Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 3 
# Output : [] )

# In[33]:


def retain_records_with_n_occurrences(test_list, k, n):
    result_list = [record for record in test_list if record.count(k) == n]
    return result_list

test_list_1 = [(4, 5, 5, 4), (5, 4, 3)]
K_1 = 5
N_1 = 2

result_1 = retain_records_with_n_occurrences(test_list_1, K_1, N_1)
print(f"Input: {test_list_1}, K: {K_1}, N: {N_1}")
print(f"Output: {result_1}")

test_list_2 = [(4, 5, 5, 4), (5, 4, 3)]
K_2 = 5
N_2 = 3

result_2 = retain_records_with_n_occurrences(test_list_2, K_2, N_2)
print(f"Input: {test_list_2}, K: {K_2}, N: {N_2}")
print(f"Output: {result_2}")


# **39-write a Python Program to Sort the list according to the column using lambda
# array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# Output :
# Sorted array specific to column 0, [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# Sorted array specific to column 1, [[2, 1, 2], [3, 2, 1], [1, 3, 3]]
# Sorted array specific to column 2, [[3, 2, 1], [2, 1, 2], [1, 3, 3]]

# In[34]:


def sort_array_by_column(input_array, column):
    sorted_array = sorted(input_array, key=lambda x: x[column])
    return sorted_array

input_array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]

for col in range(len(input_array[0])):
    sorted_array = sort_array_by_column(input_array, col)
    print(f"Sorted array specific to column {col}, {sorted_array}")


# In[ ]:


**40- write a program to Sort Python Dictionaries by Key or Value
Input:
{'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

Output: 
{'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}


# In[35]:


def sort_dict_by_key(input_dict):
    sorted_dict = dict(sorted(input_dict.items()))
    return sorted_dict

def sort_dict_by_value(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))
    return sorted_dict

input_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

sorted_dict_by_key = sort_dict_by_key(input_dict)
print("Sorted by key:", sorted_dict_by_key)

sorted_dict_by_value = sort_dict_by_value(input_dict)
print("Sorted by value:", sorted_dict_by_value)


# **41-write python program to Remove keys with Values Greater than K ( Including mixed values )
# nput : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘geeks’ : ‘CS’},
# K = 7 
# Output : {‘Gfg’ : 3, ‘for’ : 6, ‘geeks’ : ‘CS’}

# In[39]:


def remove_keys_greater_than_k(input_dict, k):
    result_dict = {key: value for key, value in input_dict.items() if (isinstance(value, int) and value <= k) or (isinstance(value, str))}
    return result_dict

test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
K = 7

result = remove_keys_greater_than_k(test_dict, K)
print("Input Dictionary:", test_dict)
print(f"Output Dictionary after removing keys with values greater than {K}:", result)


# **42-Write a Python program to concatenate the following dictionaries to create a new one
# 
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# In[41]:


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result_dict = {}
result_dict.update(dic1)
result_dict.update(dic2)
result_dict.update(dic3)

print("Result:", result_dict)


# **43-Write a Python program to iterate over dictionaries using for loops

# In[42]:


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print("Iterating over keys:")
for key in my_dict:
    print(key)

print("\nIterating over values:")
for value in my_dict.values():
    print(value)

print("\nIterating over key-value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")


# **44- Write a Python script to merge two Python dictionaries

# In[43]:


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2}

print("Merged Dictionary:", merged_dict)


# **45-Write a Python program to get the maximum and minimum values of a dictionary values

# In[44]:


my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}

max_value = max(my_dict.values())
min_value = min(my_dict.values())

print("Maximum Value:", max_value)
print("Minimum Value:", min_value)


# **46- Write a Python program to drop empty items from a given dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

# In[45]:


original_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}

new_dict = {key: value for key, value in original_dict.items() if value is not None}

print("Original Dictionary:", original_dict)
print("New Dictionary after dropping empty items:", new_dict)


# **47-Write a Python program to create a tuple of numbers and print one item

# In[46]:


numbers_tuple = (1, 2, 3, 4, 5)
print("One item from the tuple:", numbers_tuple[0])


# **48-Write a Python program to unpack a tuple into several variables

# In[47]:


my_tuple = (1, 'apple', 3.14)

number, fruit, pi_value = my_tuple
print("Unpacked Variables:")
print("Number:", number)
print("Fruit:", fruit)
print("Pi Value:", pi_value)


# **49-Write a Python program to add an item to a tuple

# In[49]:


original_tuple = (1, 2, 3)
new_item = 4
new_tuple = original_tuple + (new_item,)
print("Original Tuple:", original_tuple)
print("New Tuple after adding an item:", new_tuple)


# **50-Write a Python program to convert a tuple to a string

# In[50]:


my_tuple = ('Hello', ' ', 'World', '!')

result_string = ''.join(map(str, my_tuple))
print("Tuple:", my_tuple)
print("Converted String:", result_string)


# **51-Write a Python program to convert a list to a tuple

# In[51]:


my_list = [1, 2, 3, 4, 5]

result_tuple = tuple(my_list)

print("List:", my_list)
print("Converted Tuple:", result_tuple)


# **52-Write a Python program to reverse a tuple

# In[52]:


my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = tuple(reversed(my_tuple))
print("Original Tuple:", my_tuple)
print("Reversed Tuple:", reversed_tuple)


# **53-Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# In[53]:


original_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100
modified_list = [tuple(t[:-1] + (new_value,)) for t in original_list]
print("Original List:", original_list)
print("Modified List:", modified_list)


# **54-Write a Python program to convert a given string list to a tuple
# Original string: python 3.0
# <class 'str'>
# Convert the said string to a tuple:
# ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')

# In[54]:


original_string = "python 3.0"
tuple_result = tuple(original_string)
print("Original String:", original_string)
print("Converted Tuple:", tuple_result)


# **55-Write a Python program to calculate the average value of the numbers in a given tuple of tuples

# In[55]:


numbers_tuple = ((10, 20, 30), (40, 50, 60), (70, 80, 90))
flattened_numbers = [num for tup in numbers_tuple for num in tup]
average_value = sum(flattened_numbers) / len(flattened_numbers)
print("Original Tuple of Tuples:", numbers_tuple)
print("Flattened List of Numbers:", flattened_numbers)
print("Average Value:", average_value)


# **56-Write a Python program to add member(s) to a set.

# In[56]:


original_set = {1, 2, 3, 4, 5}
original_set.add(6)
original_set.update({7, 8, 9})
print("Original Set:", original_set)


# **57-Write a Python program to remove an item from a set if it is present in the set.

# In[57]:


original_set = {1, 2, 3, 4, 5}
item_to_remove = 3
if item_to_remove in original_set:
    original_set.remove(item_to_remove)
    print(f"{item_to_remove} removed from the set.")
else:
    print(f"{item_to_remove} not present in the set.")
print("Updated Set:", original_set)


# **58-Write a Python program to create an intersection,union,difference and symmetric difference of sets

# In[58]:


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
intersection_result = set1.intersection(set2)
union_result = set1.union(set2)
difference_result = set1.difference(set2)
symmetric_difference_result = set1.symmetric_difference(set2)
print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection:", intersection_result)
print("Union:", union_result)
print("Difference (set1 - set2):", difference_result)
print("Symmetric Difference:", symmetric_difference_result)


# **59-Write a Python program to find the maximum and minimum values in a set

# In[59]:


my_set = {10, 5, 30, 15, 20}
max_value = max(my_set)
min_value = min(my_set)
print("Original Set:", my_set)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)


# **60- Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

# In[60]:


def find_pairs_with_sum(lst, target_sum):
    pairs = []
    seen_numbers = set()
    for num in lst:
        complement = target_sum - num
        if complement in seen_numbers:
            pairs.append((num, complement))
        seen_numbers.add(num)
    return pairs
input_list = [1, 2, 3, 4, 5, 6]
given_sum = 7
result_pairs = find_pairs_with_sum(input_list, given_sum)
print(f"List: {input_list}")
print(f"Pairs with sum {given_sum}: {result_pairs}")


# In[ ]:




