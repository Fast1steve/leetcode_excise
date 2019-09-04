class Solution:
	def findContentChildren(self, g, s):
		g = sorted(g)
		s = sorted(s)
		cnt_g = 0
		cnt_s = 0
		while cnt_g < len(g) and cnt_s <len(s):
			if g[cnt_g] <= s[cnt_s]:
				cnt_g += 1

			cnt_s += 1
		return cnt_g