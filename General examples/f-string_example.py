
#f-string example
for align, text in zip('<^>', ['left', 'center', 'right']):
    print(f'{text:{align}{align}16} \n')

i = 0
print(f' {i:>16} \n')