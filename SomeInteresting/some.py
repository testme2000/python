import codecs

# unicode string to be converted
u_string = 'This is a test.'

# encoding the unicode string to byte string
b_string = codecs.encode(u_string, 'utf-8')

print(b_string)