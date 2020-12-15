file = open('tekst.txt', 'r')

if file.mode == 'r':
    input_string = file.read().split()
    file.close()
    words_change = {'i': 'oraz', 'oraz': 'i', 'nigdy': "prawie nigdy", 'dlaczego': 'czemu'}
    result = []
    for word in input_string:
        result.append(words_change.get(word, word))

    output_string = ' '.join(result)
    file = open('podmiana_result.txt', 'w+')
    file.write(output_string)
    file.close()
else:
    print('Cannot read file')
