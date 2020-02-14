import re


patterns = ['term1', 'term2']

text = 'term1'
split_term = '@'

email = 'user@gmail.com'


print(re.split(split_term, email))
#print(match.start())


print(re.findall('match','test phrase match in middle match'))

#META CHARACTER SYNTAX


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'
test_phrase_three = 'This is a string with number 12312 and a symbol #hashtag'
test_pattern = ['[A-Z]+'] #['sd*'] * means zero or more d's + = one or more {#} is number of characters followed by
newtest_pattern = [r'\W+']
new_testphrase = 'This is a string! But it has punctuation. How can we remove it?'

multi_re_find(newtest_pattern, test_phrase_three)
