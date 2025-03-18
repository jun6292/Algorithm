# stack 활용
def solution(s):
    st = []
    
    for i in range(len(s)):
        if len(st) >= 2 and st[-1] == st[-2]:
            st.pop()
            st.pop()     
        st.append(s[i])

    if len(st) >= 2 and st[-1] == st[-2]:
        st.pop()
        st.pop()
    
    return 0 if st else 1