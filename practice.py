def reverse_words(s):
    return " ".join(s.split()[::-1])


def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for char in s:                        # 1. Loop through each character
        if char.isalpha():                # 2. Filter: is it a letter?
            if char.lower() in "aeiou":   # 3. Classify: vowel or consonant?
                vowels += 1               # 4. Count it
            else:
                consonants += 1
    return {"vowels": vowels, "consonants": consonants}



# ===== STRING MANIPULATION (Most common in IBM assessments) =====

# --- Reversing a string ---
s = "hello"
print(s[::-1])  # "olleh"

# --- Check if palindrome ---
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False

# --- Count character frequency ---
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("banana"))  # {'b': 1, 'a': 3, 'n': 2}

# --- Find first non-repeating character ---
def first_unique_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

print(first_unique_char("aabbcdd"))  # "c"

# --- Check if two strings are anagrams ---
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("listen", "silent"))  # True

# --- Common string methods to know ---
s = "  Hello, World!  "
print(s.strip())        # "Hello, World!"
print(s.lower())        # "  hello, world!  "
print(s.upper())        # "  HELLO, WORLD!  "
print(s.split(","))     # ['  Hello', ' World!  ']
print(s.replace("World", "IBM"))  # "  Hello, IBM!  "
print(s.find("World"))  # 9
print(s.count("l"))     # 3





# ===== LISTS & ARRAYS =====

# --- Two Sum Problem (classic!) ---
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]

# --- Find the maximum/minimum ---
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(max(nums))  # 9
print(min(nums))  # 1

# --- Remove duplicates while preserving order ---
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]

# --- List comprehensions (IBM loves these) ---
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# --- Flatten a nested list ---
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, 3], [4, [5, 6]]]))  # [1, 2, 3, 4, 5, 6]

# --- Rotate an array ---
def rotate_array(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

print(rotate_array([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]

# --- Sliding window: max sum of subarray of size k ---
def max_subarray_sum(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

print(max_subarray_sum([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))  # 24





# ===== DICTIONARIES & SETS =====

# --- Word frequency counter ---
def word_count(sentence):
    words = sentence.lower().split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

print(word_count("the cat sat on the mat the cat"))
# {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}

# --- Group anagrams together ---
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# --- Find intersection of two lists ---
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]

# --- Merge two dictionaries ---
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}  # dict2 values override
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# --- Find most common element ---
from collections import Counter

def most_common(lst):
    return Counter(lst).most_common(1)[0]

print(most_common([1, 2, 2, 3, 3, 3, 4]))  # (3, 3) -> element 3, appears 3 times





# ===== SORTING & SEARCHING =====

# --- Binary Search (must know!) ---
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 11], 7))  # 3

# --- Custom sorting ---
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
# Sort by grade descending
students.sort(key=lambda x: x[1], reverse=True)
print(students)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# --- Sort a dictionary by value ---
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(sorted_scores)  # {'Bob': 92, 'Alice': 85, 'Charlie': 78}

# --- Find kth largest element ---
import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

print(kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5




# ===== LOOPS, LOGIC & MATH PATTERNS =====

# --- FizzBuzz (classic interview question) ---
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# --- Fibonacci sequence ---
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print([fibonacci(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# --- Check if a number is prime ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))  # True
print(is_prime(15))  # False

# --- Find GCD (Greatest Common Divisor) ---
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # 6

# --- Factorial (iterative) ---
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))  # 120

# --- Power of two check ---
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(16))  # True
print(is_power_of_two(18))  # False

