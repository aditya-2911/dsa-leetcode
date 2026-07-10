class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip=''

        for i in address:
            if i!='.':
                ip+=i
            else:
                ip+='[.]'
        return ip
        