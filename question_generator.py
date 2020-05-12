#########################################################################################################
cons = ['','k','g','s','z','t','d','m','h','p','b','n','r','y','w'] # consonant prefixes
vow = ['a','i','u','e','o',''] # vowel suffixes

# Generates a list of romaji characters
hiragana_list=[]
for consonant in (cons):
    for vowel in (vow):
        if consonant+vowel == 'si':# special case shi
             hiragana_list.append('shi')
        elif consonant+vowel == 'zi':# special case ji
             hiragana_list.append('zi')
        elif consonant+vowel == 'di':# special case dji
             hiragana_list.append('dji, '+' di, ' + ' or ji')
        elif consonant+vowel == 'tu':# special case tsu
             hiragana_list.append('tsu')
        elif consonant+vowel == 'hu':# special case fu
             hiragana_list.append('fu')
        elif consonant+vowel == 'zu':# special case tsu
             hiragana_list.append('dzu')
        elif consonant == 'y' and vowel != 'a' and vowel != 'u' and vowel != 'o':# special case ya yu yo
            pass
        elif consonant == 'w' and vowel != 'a' and vowel != 'o': # special case wa wo
            pass
        elif consonant != 'n' and vowel == '': # special case n
            pass
        else:
            hiragana_list.append(consonant+vowel)# appends to hiragana_list
            #print (consonant+vowel)
#########################################################################################################            
# Generates the quiz questions: #########################################################################
#########################################################################################################
n = range(71)
for i in n:
    print("Question %d" %(i+1)+" what is the following character in hiragana",hiragana_list[i]+"?"+ romkan.to_hiragana('%d')%hiragana_list[i]) 
#type(question)
