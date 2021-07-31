wrd = input("Enter the wrd: ")

   # returns first occurrence of Substring
a = wrd.find('acy')
# print(a)
b = wrd.find('dom')
# print(b)
c = wrd.find('er')
# print(c)
d = wrd.find('ism')
# print(d)
e = wrd.find('ment')
# print(e)
if d != -1:
        print("Root=", wrd.replace('ism', 'ist'), "Affix= -ism")        # communism, narcissism, skepticism
        quit()
elif b != -1:
        print("Root= ", wrd.replace('dom', ''), "Affix= -dom")       # kingdom
        quit()
elif e != -1:
        print("Root= ", wrd.replace('ment', '', 1), "Affix= -ment")  # endorsement
        quit()
elif a != -1:
        print("Root= ", wrd.replace('acy', 'ate'), "Affix= -acy")    # privacy
        quit()  

a1 = wrd.find('ship')
b1 = wrd.find('ied')
c1 = wrd.find('ing')
d1 = wrd.find('en')
e1 = wrd.find('ung')
f = wrd.find('al')
g = wrd.find('ate')
h = wrd.find('anti')
i = wrd.find('hyper')


if a1 != -1:
        print("Root= ", wrd.replace('ship', '', 1), "Affix= -ship")  # fellowship
        quit()
elif h != -1:
        print("Root= ", wrd.replace('anti', '', 1), "Affix= anti-") # anticlimax, antoseptic, antibody
        quit()
elif i != -1:
        print("Root= ", wrd.replace('hyper', '', 1), "Affix= hyper-") # hyperactive, hypersensitivity, hypercritical
        quit()
elif b1 != -1:
        print("Root= ", wrd.replace('ied', 'y', 1), "Affix= -ied")   # unified, verified
        quit()
elif g != -1:
        print("Root= ", wrd.replace('ate', 'ation'), "Affix= -ate")  # regulate, eradicate, enunciate
        quit()
elif c != -1:
        print("Root= ", wrd.replace('er', ''), "Affix= -er")         # trainer
        quit()
elif c1 != -1:
        print("Root= ", wrd.replace('ing', '', 1), "Affix= -ing")
        quit()
elif d1 != -1:
        print("Root= ", wrd.replace('en', '', 2), "Affix= -en")      # enlighten
        quit()
elif e1 != -1:
        print("Root= ", wrd.replace('ung', '', 1), "Affix= -ung")
        quit()
elif f != -1:
        print("Root= ", wrd.replace('al', 'e'), "Affix= -al")        # refusal
        quit()
