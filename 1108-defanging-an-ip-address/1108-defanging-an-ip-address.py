class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result = ""
        for i in address:
            if i.isdigit():
                result += i
            if i == ".":
                result += "[.]"
        return result
        