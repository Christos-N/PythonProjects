#Δεν ήξερα αν πρέπει να τυπώνει τις λ΄έξεις στην οθόνη ή να δημιουργεί νέο άρχειο με αυτές οπότε έκανα και τα δύο
import re
g = open("test2.txt","w+")
with open('test.txt','r') as f:
    for line in f:
        for word in line.split():
           z = list(re.sub(r'[^\w]', '', word)) #[^\w] will match anything that's not alphanumeric or underscore
           x = [re.sub('[0-9]', '', word) for word in z] #φτιάχνω μία λίστα που αντικαθιστά τους αριθμούς με το ''
           if len(z)>3 and not('' in x): #ελέγχω το μήκος & να μην έχει αριθμούς
                   z.append(word[0])
                   z.pop(0)
                   z.append("ay")
                   var = ""
                   for i in z:
                       var += i
                   print (var)
                   g.write("%s\n" % (var))
           else:
              print (word)
              g.write("%s\n" % (word))
f.close()
g.close()
