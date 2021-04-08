def rotate_matrix_90(a):
    
    n=len(a)
    m=len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check(new_lock):
    lock_length= len(new_lock) //3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j]!=1:
                return False
        return True

def solution(key,lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range (n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):

