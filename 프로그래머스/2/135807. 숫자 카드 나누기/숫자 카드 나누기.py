def solution(arrayA, arrayB):
    answer = 0
    gcd_a = find_gcd_in_arr(arrayA)
    gcd_b = find_gcd_in_arr(arrayB)
    
    if not_div(arrayA, gcd_b):
        answer = max(answer, gcd_b)
        
    if not_div(arrayB, gcd_a):
        answer = max(answer, gcd_a)
        
    return answer

def gcd(a, b):  # 유클리드 호제
    while b:
        a, b = b, a % b
    return a

def find_gcd_in_arr(arr):   # 배열 안에서 최대공약수를 구함
    arr_gcd = arr[0]
    for num in arr[1:]:
        arr_gcd = gcd(arr_gcd, num)
    return arr_gcd

def not_div(arr, p_gcd):   # 하나라도 나누어떨어지는지 확인
    for i in arr:
        if i % p_gcd == 0:
            return False
    return True