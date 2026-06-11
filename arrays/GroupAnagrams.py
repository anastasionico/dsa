from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            sort = [0] * 26
            # sort = [0,0,0,0,0,0,0,0,0,0,0]
            for ch in word:
                # print(ch)
                # sort = [0,0,0,0,1,0,0,0,0,0,0]
                sort[ord(ch) - ord('a')] +=1

            # print(word)
            # print(tuple(sort))

            res[tuple(sort)].append(word)

        return list(res.values())

if __name__ == "__main__":
    solution = Solution()
    result = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(result)