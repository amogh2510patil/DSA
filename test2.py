def validity(string,i):
    if i-1>=0 and string[i]==string[i-1]:
        if i-2>=0 and string[i-1]==string[i-2]:
            return False
        if i+1<len(string) and string[i+1]==string[i]:
            return False
    if i+1<len(string) and string[i]==string[i+1]:
        if i+2<len(string) and string[i+2]==string[i+1]:
            return False
        if i+1<len(string) and string[i+1]==string[i]:
            return False
    return True
def solution(S):
    # write your code in Python 3.6
       
    string=[char for char in S]
    i=0
    backtrack=False
    while i<len(string) and i>=0:
        if S[i]=='a' or S[i]=='b':
            if backtrack:
                i=i-1
                continue
            i=i+1
            continue
        if string[i]=='?':
            string[i]='a'
            flag=validity(string,i)
            if flag:
                i+=1
                continue
            string[i]='b'
            flag=validity(string,i)
            if flag:
                i+=1
                continue
            i=i-1
            backtrack=True
            continue
    
        elif string[i]=='a':
            string[i]='b'
            flag=validity(string,i)
            if flag:
                backtrack=False
                i=i+1
                continue
            
        string[i]='?'
        i=i-1
        backtrack=True
    return string if i>0 else "Not possible"
print(validity("aaabaa",2))
print(solution("aa??aa"))


        
        

