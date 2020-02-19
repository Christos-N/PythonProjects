def function():
    s = input("Enter text:")
    y = [ord(c) for c in s] #εκχωρώ στο y(array) τον ASCII code της λέξης που μου δόθηκε
    x = ''.join(str(j) for j in y) #εκχωρώ στο x(string) τους αριθμούς του πίνακα y τον έναν δίπλα στον άλλο
    x = int(x) #μετατρέπω το x από string σε int
    for i in range (2,x):       #ελέχγω αν ο αριθμός είναι πρώτος
        if x%i == 0:
            y = 0
            print("The number", x, "is not prime!")
            break
        else:
            y = 1
    if y == 1:
        print("The number", x, "is prime!")
function()
