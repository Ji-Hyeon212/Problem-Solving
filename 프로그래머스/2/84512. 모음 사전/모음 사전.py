def solution(word):
    vowels = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    weights = [781, 156, 31, 6, 1]
    answer = len(word)
    for i, char in enumerate(word):
        vowel = vowels[char]
        answer += vowel * weights[i]
    return answer