def solution(numbers, target):
	global answer

	if not numbers:  # 스택이 가득 찼을 때
		if sum(stack) == target:  # 합이 target과 같으면 카운트
			answer += 1
		return
	number = numbers[0]

	stack.append(number)
	solution(numbers[1:], target)  # 리스트에서 첫 번째 원소를 제외
	stack.pop()

	stack.append(-number)
	solution(numbers[1:], target)
	stack.pop()

	return answer


stack = []
answer = 0
