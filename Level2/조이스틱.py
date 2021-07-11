def solution(name):
	answer = 0
	count = 0 # A가 아닌 문자의 개수
	for c in name: # 각 문자별로 위아래 움직임 더해줌
		if c == 'A':
			continue
		if c > 'A' and c <= 'N':
			answer += ord(c) - ord('A')
			count += 1
		elif c >= 'O' and c <= 'Z':
			answer += ord('Z') - ord(c) + 1
			count += 1
	if count == 0: # 전부다 A일 때 0 반환
		return 0

	name = list(name)
	if name[0] != 'A': # 첫번째 문자는 좌우로 움직이지 않아도 바꿔줄 수 있음
		count -= 1
		name[0] = 'A'

	idx = 0

	for _ in range(count):
		for i in range(1, len(name)):
			left = (idx - i) % len(name)
			right = (idx + i) % len(name)

			if name[right] != 'A':
				answer += i
				name[right] = 'A'
				idx = right
				break
			if name[left] != 'A':
				answer += i
				name[left] = 'A'
				idx = left
				break
	return answer