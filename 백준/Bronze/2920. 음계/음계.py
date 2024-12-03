syllable = list(map(int, input().split()))
new = sorted(syllable)
reverse = sorted(syllable, reverse=True)

if syllable == new:
    print('ascending')
elif syllable == reverse:
    print('descending')
else:
    print('mixed')