# imie = 'Ala'
# if imie == "Ania":
#     print('czesc Ania')
# elif imie == "Ola":
#     print ('czesc Ola')
# else: 
#     print ('czesc nieznajoma')

# odleglosc = 3
# if odleglosc<5: 
#     print ('wow, ale blisko')
# elif 5<= odleglosc <10:
#     print("dosyc blisko")
# elif 10<= odleglosc< 20:
#     print ('zaczyna sie robic daleko')
# else:
#     print('o matko jak daleko')

# def hej(imie):
#     print('HELLO ' + imie)

# imiona = ['Kasia','Basia','Zosia']

# for imie in imiona:
#     hej (imie)
# hej('Ania')
def jak_daleko (odleglosc):
    if odleglosc<5: 
        print ('wow, ale blisko')
    elif 5<= odleglosc <10:
        print("dosyc blisko")
    elif 10<= odleglosc< 20:
        print ('zaczyna sie robic daleko')
    else:
        print('o matko jak daleko') 


odleglosc = [10, 15, 4 ]
for o in odleglosc:
    jak_daleko (o)

for i in range(1,10):
    print(i)
# jak_daleko(15)
# jak_daleko(17)
# jak_daleko(3) 
