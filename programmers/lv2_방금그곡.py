coord_map = {
	'C#': '1',
	'D#': '2',
	'E#': '3',
	'F#': '4',
	'G#': '5',
	'A#': '6',
}


def conv_flat(coord):
	converted = ''
	sl = len(coord)
	j = 0
	while j < sl:
		if j + 1 < sl and coord[j + 1] == '#':
			converted += coord_map[coord[j:j + 2]]
			j += 2
		else:
			converted += coord[j]
			j += 1
	return converted


def solution(m, musicinfos):
	answer = '(None)'
	max_dur = 0
	m = conv_flat(m)
	for music in musicinfos:
		start, end, name, sheet = music.split(',')
		sh, sm = start.split(':')
		eh, em = end.split(':')
		duration = (int(eh) - int(sh)) * 60 + int(em) - int(sm)

		sheet = conv_flat(sheet)
		sl = len(sheet)
		full = ''.join([sheet[i % sl] for i in range(duration)])

		if m in full and max_dur < duration:
			max_dur = duration
			answer = name
	return answer


print(solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']))
print(solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']))
print(solution('ABC', ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']))
