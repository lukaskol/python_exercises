inserted_data = input('Insert your name, surname and year of birth in one line: ')
name_end = inserted_data.find(' ')
surname_end = inserted_data.find(' ', name_end+1)
name = inserted_data[:name_end]
surname = inserted_data[name_end+1:surname_end]
date = inserted_data[surname_end+1:]
print('Name: ' + name + '\nSurname: ' + surname + '\nDate of birth: ' + date)
