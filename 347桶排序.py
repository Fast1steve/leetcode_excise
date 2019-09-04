class Solution:
	def topKFrequent(self, nums, k):
		frequent_of_number = {}
		for num in nums:
			frequent_of_number[num] = frequent_of_number.get(num, 0) + 1
		# 建桶
		buckets = [[] for i in range(len(nums) + 1)]
		for key, value in frequent_of_number.items():
			buckets[value].append(key)
		print(buckets)
		result = []
		for x in range(len(nums), -1, -1):
			if k > 0 and buckets[]:
				result += buckets[x]
				k -= len(buckets[x])
			if k==0:
				return result