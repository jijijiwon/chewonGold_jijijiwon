def merge_sort(arr, p, r, K):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q, K)
        merge_sort(arr, q + 1, r, K)
        merge(arr, p, q, r, K)

def merge(A, p, q, r, K):
    global count, result  # count는 저장된 횟수, result는 K번째 저장된 값
    left = A[p:q+1]  # 왼쪽 부분 배열 (A[p..q])
    right = A[q+1:r+1]  # 오른쪽 부분 배열 (A[q+1..r])
    
    i = 0  # 왼쪽 배열의 인덱스
    j = 0  # 오른쪽 배열의 인덱스
    k = p  # 원래 배열 A에 병합된 결과를 저장할 인덱스
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        
        count += 1
        if count == K:
            result = A[k]  # K번째 저장된 값을 result에 저장
        k += 1
    
    # 왼쪽 배열에 남은 요소가 있으면 A에 복사
    while i < len(left):
        A[k] = left[i]
        i += 1
        count += 1
        if count == K:
            result = A[k]  # K번째 저장된 값을 result에 저장
        k += 1
    
    # 오른쪽 배열에 남은 요소가 있으면 A에 복사
    while j < len(right):
        A[k] = right[j]
        j += 1
        count += 1
        if count == K:
            result = A[k]  # K번째 저장된 값을 result에 저장
        k += 1

# 입력 및 초기 설정
N, K = map(int, input().split())
arr = list(map(int, input().split()))
count = 0  # 저장 횟수를 추적할 전역 변수
result = -1  # K번째 저장된 값을 저장하는 변수 (-1로 초기화)

# 병합 정렬 실행
merge_sort(arr, 0, N - 1, K)

# 결과 출력
print(result)
