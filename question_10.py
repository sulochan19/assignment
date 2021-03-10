# 10. Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well


def convert_case(word,separator):
    if separator=='_':
        list=[word[0].lower()]
        for character in word[1:]:
            if character in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                list.append('_')
                list.append(character.lower())
            else:
                list.append(character)
        return ''.join(list)
    elif separator=="-":
        list = [word[0].lower()]
        for character in word[1:]:
            if character in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                list.append('-')
                list.append(character.lower())
            else:
                list.append(character)
        return ''.join(list)



word="ThisIsCamelCase"
print(convert_case(word,'_'))