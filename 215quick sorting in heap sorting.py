class Solution1:
	def findKthLargest(self, nums, k):
		return self.quick_sort(nums, k)

	def quick_sort(self, nums, k):
		# 这个位置的元素是我们想要的结果元素
		k = len (nums) - k
		left = 0
		right = len(nums) - 1
		while left < right:
			j = self.partition(nums, left, right)
			if j == k:
				break
			elif j < k:
				left = j + 1
			else:
				right = j - 1
		return nums[k]

	def partiton(self, nums, left, right):
		while True:
			while nums[left] < nums[right]:
				right -= 1
			else:
				nums[left], nums[right] = nums[right], nums[left]
				if left >= right:
					break
				left += 1

			while nums[left] < nums[right]:
				left += 1
			else:
				nums[left], nums[right] = nums[right], nums[left]
				if left >= right:
					break
				right -= 1

		return left
class Solution2:
	def findKthLargest(self, nums, k):
		return self.heap_sort(nums, k)
	def heap_sort(self, nums, k):
		# 构建大顶堆
		for i in range(len(nums)//2 - 1, -1, -1):
			self.heap_adjust(nums, i, len(nums))
		cnt = 0
		#交换堆顶元素。然后重新调整堆结构
		for i in range(len(nums) - 1, 0, -1):
			self.heap_swap(nums, 0, i)
			cnt += 1
			if cnt == k:
				return nums[i]
			self.heap_adjust(nums, 0, i)
		# 说明 k==len(nums)
		return nums[0]

	def heap_adjust(self, nums, start, length):
		tmp = nums[start]
		k = start * 2 + 1
		while k < length: #对于完全二叉树来讲，没有左节点就没有右节点
		# 当前节点左节点序号
			left = start * 2 + 1
		# 当前节点右节点序号
			right = left + 1

			if right < length and nums[right] > nums[left]:
			# 如果右节点比较大
				k = right
			if nums[k] > tmp:
			# 如果子节点比父节点大，则将子节点赋值给父节点
			nums[start] = nums[k]
			start = k
			else:
				break
			k = k*2 + 1
		nums[start] = tmp
	def heap_swap(self, nums, i, j):
		nums[i], nums[j] = nums[j], nums[i]
		return nums

