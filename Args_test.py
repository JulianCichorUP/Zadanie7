def person_print(name,last_name,age,*others):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name,last_name,age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)

person_print('Julian','Cichor',21,"pesel: 12345678912", "zawod: student")

"""
Nie można, ponieważ argument args/kwargs musi być na końcu deklaracji funkcji. 
"""
