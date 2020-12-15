#!/usr/bin/env python3
import csv
from tabulate import tabulate

headers = ["City", "State", "LatD", "LatM", "LatS", "NS", "LonD", "LonM", "LonS", "EW"]
data = []

with open("sample_csv.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        temp = [f'{row["City"]}'.replace("\"", "").replace(" ", ""),
                f'{row["State"]}'.replace("\"", "").replace(" ", ""),
                f'{row["LatD"]}'.replace("\"", "").replace(" ", ""),
                f'{row["LatM"]}'.replace("\"", "").replace(" ", ""),
                f'{row["LatS"]}'.replace("\"", "").replace(" ", ""),
                f'{row["NS"]}'.replace("\"", "").replace(" ", ""),
                f'{row["LonD"]}'.replace("\"", "").replace(" ", ""),
                f'{row["LonM"]}'.replace("\"", "").replace(" ", ""),
                f'{row["LonS"]}'.replace("\"", "").replace(" ", ""),
                f'{row["EW"]}'.replace("\"", "").replace(" ", "")]
        data.append(temp)
    print(tabulate(data, headers=headers))
    f.close()

print("[1]Edycja\n[2]Usuwanie")
option = input("Numer opcji: ")
if option == '1':
    print("Wpisz nazwę miasta, którego wartości chcesz zmienić")
    city = input("Miasto: ")
    for i in data:
        if i[0] == city:
            print("State %s\nLatD %s\nLatM %s\nLatS %s\nNS %s\nLonD %s\nLonM %s\nLonS %s\nEW %s" %
                (i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
            print("Podaj kolejno wartości. Jeśli nie zmieniasz, zostaw puste.")
            for j in range(len(headers)):
                if j == 0:
                    continue
                temp = input("%s: " % headers[j]).replace(" ", "")
                if temp == "":
                    continue
                i[j] = temp
elif option == '2':
    print("Wpisz nazwę miasta, które chcesz usunąć")
    city = input("Miasto: ")
    for i in data:
        if i[0] == city:
            data.remove(i)
            print("Usunięto")
            break


with open('sample_csv.csv', mode='w') as f:
    writer = csv.DictWriter(f, fieldnames=headers)

    writer.writeheader()
    for d in data:
        writer.writerow({headers[2]: d[2],
                         headers[3]: d[3],
                         headers[4]: d[4],
                         headers[5]: d[5],
                         headers[6]: d[6],
                         headers[7]: d[7],
                         headers[8]: d[8],
                         headers[9]: d[9],
                         headers[0]: d[0],
                         headers[1]: d[1]})
