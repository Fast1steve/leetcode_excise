class Solution:
	def sortColors(self, nums):
		head, now, tail = 0, 0, len(nums) - 1
		while now <= tail:
			if nums[now] == 0:
				nums[now], nums[head] = nums[head], nums[now]
				now, head = now + 1, head + 1
			elif nums[now] == 2:
				nums[now], nums[tail] = nums[tail], nums[now]
				tail -= 1
			else:
				now += 1
