class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        for i in address:
            if i == ".":
                result += "[.]"
            else:
                result+=i
        return result