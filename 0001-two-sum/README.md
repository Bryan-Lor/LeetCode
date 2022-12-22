<h2><a href="https://leetcode.com/problems/two-sum/">1. Two Sum</a></h2><h3>Easy</h3><hr><div><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than&nbsp;<code>O(n<sup>2</sup>)&nbsp;</code>time complexity?</div>
</br>
  
<details>
<summary><b>SHOW SOLUTIONS</b></summary>
  
## O(n) Optimal Linear Solution
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) solution that iteratively goes through each item and saves its 
        # complimentary number into a dictionary which will then be returned in O(1) time.
        # O(n) * O(1) = O(n)
	
        complimentMap = dict()        
        for i in range(len(nums)):
            complimentaryNumber = target - nums[i]
            if nums[i] in complimentMap:
                return [complimentMap[nums[i]], i]
            else:
                complimentMap[complimentaryNumber] = i
```
  
## O(n<sup>2</sup>) Brute Force Solution
```
def twoSum(self, nums: List[int], target: int) -> List[int]:
         # O(n^2) solution where you iteratively[O(n)] go through each item and search if
         # target - nums[i] exists within the list. If so, simply return the two indexes which .
         # also takes [O(n)] times. O(n) * O(n) = O(n^2)
	 
         for i in range(len(nums)):
             complimentaryNumber = target - nums[i]
             if complimentaryNumber in nums and nums.index(complimentaryNumber) != i:
                 return [i, nums.index(complimentaryNumber)]
```
</details>

Time: 65 ms (92.39%), Space: 15.4 MB (9.61%) - LeetHub
