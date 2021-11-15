#https://leetcode.com/discuss/interview-question/690707/Amazon-or-Phone-or-Group-Product-Id-pairs-into-Categories
#union find 

# I recently had a phone interview with Amazon and I was asked the following question:

# Given a list of Product Id pairs, group them according to their categories and return the new list containing categorized Product Ids.

# Input: ((1,2), (2,5), (3,4), (4,6), (6,8), (5,7), (5,2), (5,2))

# Output: ((1,2,5,7), (3,4,6,8))

# Test case I came up with:

# Input: ((1,2), (2,5), (3,4), (4,6), (6,8), (5,7), (5,2), (3,1))

# Output: ((1,2,5,7,3,4,6,8))

# Initially the problem definition had a mistake in it which was quite contradictory to the given input and expected output. and I did point that out during the interview and the interviewer did not seem to acknowledge it. So it seemed better to ignore the error in the problem definition and concentrate on the given input and output, and I decided to come up with more test cases. The problem definition initially stated "return the number of categories and the number of product ids in each category". The interviewer changed their mind while I was reading the problem aloud and asked me to return the list of categorized product ids instead of what is mentioned in the problem definition.

# When I started discussing the solution, initially I thought of solving it using DFS approach and it didn't seem right to me. Suddenly it struck me that it can be solved using Union-Find data structure as it is perfect for merging disjoint sets. The interviewer seemed not aware of that data structure and asked me which data structure from C++ STD library. I told that there is no in-built Union-Find data structure available in C++ STD library and I was going to implement one for solving the problem. And it was all downhill from there.

# I spent most of time explaining how the data structure works and while coding it, I did go through inner workings of FIND and UNION functions and how path compression happens. I was also asked whether the solution would work for random product ids because inputs from test cases had product ids uniformly numbered from 1 to 8. I told the interviewer that we just need to map the random product ids to node ids begining from 0 to number of product ids.

# I got to the partial solution by the end of 30 odd minutes and my solution was only able to return the number of categories.

# After the interview got over, I did complete the problem on my end and the solution using Union-Find data structure did categorize the product ids according to their categories for the initial set of inputs. I did not really try giving random product ids because it simply boiled down to mapping the product ids to node ids starting from 0.

# I did get some feedback from my recruiter (He was great by the way) and the interviewer felt that I could not identify the right data structure to solve the problem that was posed to me.

# I am clearly surprised by the feedback and I felt that interviewer clearly had no knowledge on Union-Find data structure and how the problem can be solved efficiently as U-F data structure gurantees amortized time. I did not really explore other better ways of solving this problem. So any feedback from the community regarding the solution and the process itself would be really helpful.



def productGroups(groups):
	def dfs(group, groups, visited, uniqueKeys):
		for g in groups:
			if g in visited:
				continue
			g1 = group[0]
			g2 = group[1]

			if g2 == g[0] or g1 == g[0] or g1 == g[1] or g2 == g[1]:
				visited.add(g)
				uniqueKeys.add(g[0])
				uniqueKeys.add(g[1])
				dfs(g, groups, visited, uniqueKeys)


	visited = set()

	results = list()

	for g in groups:
		if g in visited:
			continue

		dfsResults = visited
		uniqueKeys = set()
		dfs(g, groups, dfsResults, uniqueKeys)
		results.append(list(uniqueKeys))
		visited.union(dfsResults)

	print(results)


productGroups([(1,2), (2,5), (3,4), (4,6), (6,8), (5,7), (5,2), (5,2)])
productGroups([(1,2), (2,5), (3,4), (4,6), (6,8), (5,7), (5,2), (3,1)])