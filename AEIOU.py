ch = input('Enter an alphabet : ')
if ch.isalpha():
    x = ch.lower()
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        print(ch, 'is a vowel.')
    else:
        print(ch, 'is a consonant.')
else:
    print(ch, 'is not an alphabet.')