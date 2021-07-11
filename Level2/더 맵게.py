import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 리스트를 최소 힙으로 만들어줌 (O(N))
    while scoville[0] < K: # 첫번째 원소가 최소 원소
        if len(scoville) >= 2:
            food1 = heapq.heappop(scoville)
            food2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (food1 + food2 * 2))
            answer += 1
        else: # 아직 K보다 작은 원소가 있는데 원소의 개수가 2개 이하이면 -1
            return -1
    return answer