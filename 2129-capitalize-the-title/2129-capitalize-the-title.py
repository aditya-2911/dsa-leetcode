class Solution:
    def capitalizeTitle(self, title: str) -> str:
        lst=title.split(' ')
        
        for word in range(len(lst)):
            if len(lst[word])==1 or len(lst[word])==2:
                lst[word]=lst[word].lower()
            else:
                lst[word]= lst[word][:1].upper()+lst[word][1:].lower()
        title= " ".join(lst)
        return title