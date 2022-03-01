class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "".join("[.]" if i=="." else i for i in address)