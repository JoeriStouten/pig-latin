print("This game is called PigLatin...")
userWord = input("Type a word...")
klinkers = ['a','e','u','i','o','y','A','E','U','I','O','Y']
medeklinkers = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','R','T','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
length = len(userWord)

if userWord[0] in klinkers:
    print(userWord + "-hay")
else:
    i = 0
    aantal_medeklinkers = 0
    while userWord[i] in medeklinkers:
        i += 1
        aantal_medeklinkers += 1
print(userWord[i:length] + '-' + userWord[0:i] + 'ay')
