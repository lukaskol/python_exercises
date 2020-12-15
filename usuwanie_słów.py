file = open("tekst.txt", 'r')

if file.mode == 'r':
    text = file.read()
    file.close()
    delete_words = ['się', 'i', 'oraz', 'nigdy', 'dlaczego']
    string_words = text.split()
    result_words = [word for word in string_words if word.lower() not in delete_words]
    result_string = ' '.join(result_words)
    file = open('usuwanie_result.txt', 'w+')
    file.write(result_string)
    file.close()

else:
    print("Cannot read file!")
    exit(-1)



