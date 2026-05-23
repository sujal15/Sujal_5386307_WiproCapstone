import  re
# bigning ending program
# txt = input('Enter a text ') #india is my country
# bpat = input('Enter beginning pattern ') # India
# epat = input('Enter ending pattern ') #country
# bpat = '^' + bpat #India
#
# if re.search(pattern=bpat , string=txt):
#     print(' Beginning pattern available')
# else:
#     print('Beginning pattern not available')
# epat =  epat  + '$' #try$
# if re.search(pattern=epat , string=txt):
#     print(' ending pattern available')
# else:
#     print('ending pattern not available')

# mbno = input('Enter a text ')
# pat =  r'\d' #'[0-9]'
# if  re.fullmatch(pattern=pat , string=mbno):
#     print(' Only digit')
# else:
#     print('Char not digit available')

# un = input('Enter a UN ')
# pat = r'^[a-z_]{8,}$'
# if re.match(pattern=pat , string=un):
#     print('Valid')
# else:
#     print('Invalid')

emailadd = input('Email ')
pat = r'^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
if re.match(pattern=pat , string=emailadd):
    print('Valid')
else:
    print('Invalid')


# txt = input('Text: ')
# pat = r'\s+'
# print(re.split(pattern=pat, string=txt))
