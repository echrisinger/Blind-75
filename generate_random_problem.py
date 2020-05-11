import random

with open('generated_problems.txt') as gen_f:
    content = gen_f.readlines()
generated_problems = [x.strip() for x in content] 

problems = """
Two Sum
Best Time to Buy and Sell Stock
Contains Duplicate
Product of Array Except Self
Maximum Subarray
Maximum Product Subarray
Find Minimum in Rotated Sorted Array
Search in Rotated Sorted Array
3 Sum
Container With Most Water
Sum of Two Integers
Number of 1 Bits
Counting Bits
Missing Number
Reverse Bits
Climbing Stairs
Coin Change
Longest Increasing Subsequence
Longest Common Subsequence
Word Break Problem
Combination Sum
House Robber
House Robber II
Decode Ways
Unique Paths
Jump Game
Clone Graph
Course Schedule
Pacific Atlantic Water Flow
Number of Islands
Longest Consecutive Sequence
Alien Dictionary (Leetcode Premium)
Graph Valid Tree (Leetcode Premium)
Number of Connected Components in an Undirected Graph (Leetcode Premium)
Insert Interval
Merge Intervals
Non-overlapping Intervals
Meeting Rooms (Leetcode Premium)
Meeting Rooms II (Leetcode Premium)
Reverse a Linked List
Detect Cycle in a Linked List
Merge Two Sorted Lists
Merge K Sorted Lists
Remove Nth Node From End Of List
Reorder List
Set Matrix Zeroes
Spiral Matrix
Rotate Image
Word Search
Longest Substring Without Repeating Characters
Longest Repeating Character Replacement
Minimum Window Substring
Valid Anagram
Group Anagrams
Valid Parentheses
Valid Palindrome
Longest Palindromic Substring
Palindromic Substrings
Encode and Decode Strings (Leetcode Premium)
Maximum Depth of Binary Tree
Same Tree
Invert/Flip Binary Tree
Binary Tree Maximum Path Sum
Binary Tree Level Order Traversal
Serialize and Deserialize Binary Tree
Subtree of Another Tree
Construct Binary Tree from Preorder and Inorder Traversal
Validate Binary Search Tree
Kth Smallest Element in a BST
Lowest Common Ancestor of BST
Implement Trie (Prefix Tree)
Add and Search Word
Word Search II
Merge K Sorted Lists
Top K Frequent Elements
Find Median from Data Stream
""".split('\n')

problem = random.choice(list(set(problems) - set(generated_problems)))
with open('generated_problems.txt', 'w+') as gen_f:
    for prob in generated_problems+[problem]:
        gen_f.write(prob+"\n")

print(problem)

