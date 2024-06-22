class Solution:
    def numberOfSubarrays(self, nums, k):
        prefix_sum = 0
        count_map = {0: 1}  # Initialize with 0:1 to handle the case when the subarray starts from index 0
        result = 0

        for num in nums:
            # Update prefix sum (considering 1 for odd and 0 for even)
            prefix_sum += num % 2

            # If there exists a prefix sum that is (current prefix_sum - k), 
            # it means there is a subarray ending at the current index with k odd numbers.
            if prefix_sum - k in count_map:
                result += count_map[prefix_sum - k]

            # Update the count of current prefix_sum in the map
            if prefix_sum in count_map:
                count_map[prefix_sum] += 1
            else:
                count_map[prefix_sum] = 1

        return result

# Example Usage
solution = Solution()
print(solution.numberOfSubarrays([1,1,2,1,1], 3))  # Output: 2
print(solution.numberOfSubarrays([2,4,6], 1))       # Output: 0
print(solution.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))  # Output: 16
