# 31. Next Permutation

## Description

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

## Reference

This problem is from [LeetCode Problem #31: Next Permutation](https://leetcode.com/problems/next-permutation/)

## Hints

1. Try to identify patterns in how the next permutation is formed.
2. Focus on finding the first pair of adjacent elements from the right where the left element is smaller than the right element.
3. Consider what happens when you need to form the next permutation for arrays like [1,2,3] vs [3,2,1].
4. Remember that you need to find the next lexicographically greater permutation, not just any greater permutation.
5. The key is to make the smallest possible change to create the next greater permutation.

## Solution

The algorithm to find the next permutation can be broken down into these steps:

1. Start from the end of the array and move left to find the first pair of adjacent elements where the left element is smaller than the right element. Let's call the left element's index `i`. This means `nums[i] < nums[i+1]`.

2. If no such index exists (i.e., the array is in descending order), then the array is already at its highest permutation. In this case, reverse the entire array to get the lowest permutation.

3. If `i` is found, look for the smallest element to the right of `i` that is greater than `nums[i]`. Let's call this element's index `j`.

4. Swap `nums[i]` and `nums[j]`.

5. Reverse the subarray starting from index `i+1` to the end of the array.

This algorithm ensures that we find the next lexicographically greater permutation with the smallest possible change to the current permutation.

## Time and Space Complexity

- **Time Complexity**: O(n), where n is the length of the input array. We need to traverse the array at most twice in the worst case.

- **Space Complexity**: O(1), as the problem requires us to use only constant extra memory. The algorithm performs all operations in-place.
