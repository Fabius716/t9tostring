# the dictionary
td={"2":'abc',"3":'def',"4":'ghi',"5":'jkl',"6":'mno',"7":'pqrs',"8":'tuv',"9":'wxyz'}
# counter
dictcounter=0
# counter
letterprocessed=0
# solution string
sol=""
# open doc
with open("bank_heist_message.txt","r") as document:
    for line in document:
        print(line)
        for letter in line:
            print(f'letter is {letter} and lp is {letterprocessed}')
            if letterprocessed+1==len(line):
                break
            # se letterprocessed+1 > len(line) pass
            if letterprocessed+1 > len(line):
                pass
            # se letter == " " pass
            if letter==" " or letter=="." or letter=="," or letter==":" or letter=="!":
                #pass
                sol = sol + letter
            print(letterprocessed+1,len(line))
            if letter==line[letterprocessed+1] and not letterprocessed+1 > len(line) and not (letter==" " or letter=="." or letter=="," or letter==":" or letter=="!"):
                #line[x]==line[x+1] in teoria
                dictcounter+=1
            if letter!=line[letterprocessed+1] and not letterprocessed+1 > len(line) and not (letter==" " or letter=="." or letter=="," or letter==":" or letter=="!"):
                #aggiungi la lettera (processata nel dict) ad una stringa e resetta dictcounter
                #letter index key should be used 
                print(td[letter][dictcounter])
                sol=sol+td[letter][dictcounter]
                dictcounter=0
            letterprocessed+=1
            print(sol)
        letterprocessed=0
# stai attento a creare un eccezione per index out of size -> primo if
#
# 
