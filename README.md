# Sample Codes for LeetBLIND 75 Problems

* [two_sum](https://github.com/Aethels/Leetcode75/blob/main/two_sum.py) -> use hash map to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice

* [valid_parenthesis](https://github.com/Aethels/Leetcode75/blob/main/valid_parenthesis.py) -> push opening brace on stack, pop if matching close brace, at end if stack empty, return true

* [merge_two_sorted_linkedlists](https://github.com/Aethels/Leetcode75/blob/main/merge_two_sorted_linkedlists.py) -> insert each node from one list into the other

* [best_time_for_buy_and_sell](https://github.com/Aethels/Leetcode75/blob/main/best_time_for_buy_and_sell.py) -> find local min and search for local max, sliding window

* [valid_palindrome](https://github.com/Aethels/Leetcode75/blob/main/valid_palindrome.py) -> left, right pointers, update left and right until each points at alphanum, compare left and right, continue until left >= right, don’t distinguish between upper/lowercase

* [inverted_tree](https://github.com/Aethels/Leetcode75/blob/main/inverted_tree.py) -> the root of a binary tree, invert the tree, and return its root.

* [valid_anagram](https://github.com/Aethels/Leetcode75/blob/main/valid_anagram.py) -> hashmap to count each char in str1, decrement for str2

* [binary_search](https://github.com/Aethels/Leetcode75/blob/main/binary_search.py) -> Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1

* [flood_fill](https://github.com/Aethels/Leetcode75/blob/main/flood_fill.py) ->  m x n integer grid image where image[i][j] represents the pixel value of the image, three integers sr, sc, and color. perform a flood fill on the image starting from the pixel image[sr][sc] accourding the directions

* [LCA_of_BST](https://github.com/Aethels/Leetcode75/blob/main/LCA_of_BST.py) -> compare p, q values to curr node, base case: one is in left, other in right subtree, then curr is lca




