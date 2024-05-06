class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        ans = []
        temp = ""
        spacing = 0
        for i in A:
            if i == ',':
                ans.append(temp + i)
                temp = ""
            elif i == '[' or i == '{':
                if temp:
                    ans.append(temp)
                ans.append('\t' * spacing + i)
                spacing += 1
                temp = ""
            elif i == ']' or i == '}':
                spacing -= 1
                if temp:
                    ans.append(temp)
                temp = '\t' * spacing + i
            else:
                if not temp and spacing > 0:
                    temp = '\t' * spacing
                temp += i

        if temp:
            ans.append(temp)

        return ans
