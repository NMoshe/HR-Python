import re
vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'
m = re.findall('(?<=['+consonants+'])(['+vowels+']{2,})['+consonants+']', input(), re.IGNORECASE)
print('\n'.join(m or ['-1']))

