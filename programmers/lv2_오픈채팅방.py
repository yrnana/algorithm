def solution(record):
	answer = []

	rec = []
	nick = dict()

	for r in record:
		r = r.split(' ')
		if r[0] == 'Change':
			nick[r[1]] = r[2]
		elif r[0] == 'Enter':
			nick[r[1]] = r[2]
			rec.append([r[0], r[1]])
		else:
			rec.append([r[0], r[1]])

	for x in rec:
		case, uid = x
		s = nick[uid] + '님이 '
		s += '들어왔습니다.' if case == 'Enter' else '나갔습니다.'
		answer.append(s)

	return answer


print(solution(
	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
