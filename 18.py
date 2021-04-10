def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count ==0:
            return 1

    # i dont get this funct
def check_proper(p):
    count = 0
    for i in p:
        if i =='(':
            count +=1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    