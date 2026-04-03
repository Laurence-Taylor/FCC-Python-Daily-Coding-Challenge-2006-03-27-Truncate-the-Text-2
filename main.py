def truncate_text(s):
    values_dic = {'i':1,'l':1,'I':1,'.':1,'f':2,'j':2,'r':2,'t':2,' ':2,'a':3,'b':3,'c':3,'d':3,'e':3,'g':3,'h':3,'k':3,'m':3,'n':3,'o':3,'p':3,'q':3,'s':3,'u':3,'v':3,'w':3,'x':3,'y':3,'z':3,'J':3,'L':3,'A':4,'B':4,'C':4,'D':4,'E':4,'F':4,'G':4,'H':4,'K':4,'M':4,'N':4,'O':4,'P':4,'Q':4,'R':4,'S':4,'T':4,'U':4,'V':4,'W':4,'X':4,'Y':4,'Z':4}
    total = 0
    for pos in range(len(s)):
        total += values_dic[s[pos]]
        if total > 50:
            if (total-values_dic[s[pos]]) <= 47:
                return s[:pos]+'...'
            elif (total-values_dic[s[pos]]-values_dic[s[pos-1]]) <= 47:
                return s[:pos-1]+'...'
            elif (total-values_dic[s[pos]]-values_dic[s[pos-1]]-values_dic[s[pos-2]]) <= 47:
                return s[:pos-2]+'...'
    return s

if __name__ == '__main__':
    print(truncate_text("The quick brown fox"))
    print('----')
    print(truncate_text("The silky smooth sloth"))
    print('----')
    print(truncate_text("THE LOUD BRIGHT BIRD"))
    print('----')
    print(truncate_text("The fast striped zebra"))
    print('----')
    print(truncate_text("The big black bear"))
    print('----')
    print(truncate_text("The fast striped z.."))