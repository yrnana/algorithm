import collections

def check(word, chars):
	container = collections.Counter(word)
	for k, v in container.items():
		if not chars.get(k) or chars.get(k) < v:
			return False
	return True

if __name__ == "__main__":
	words = ["cat", "bt", "hat", "tree"]
	chars = "atach"
	tmp = collections.Counter(chars)

	for x in words:
		print(x, check(x, tmp))


