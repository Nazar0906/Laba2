u = input("Порахувати кількість букв в тексті - 1\n Посортувати букви в алфавітному порядку - 2\n Ваш вибір: ")

def tx(s):
	d = {}
	for i in s:
		if i.isalpha():
			d[i] = d.get(i,0) + 1
	for i in sorted(d):
		print(i + ":" + str(d[i]))

while u == "1":
	print("Ви вибрали 1 варіант")
	txx = input("Напишіть щось: ")
	tx(txx)
	print("Закінчено")
	print("Для продовження натисніть - N\n Вихід - E")
	u2 = input("Ваш вибір: ")
	if u2 == "N":
		u == "1"
	elif u2 == "2":
		u == "2"
	elif u2 == "E":
		break
	else:
		print("Неправильно")
while u == "2":
	print("Ви обрали 2 варіант")
	ttx = input("Напишіть щось: ").replace('@', '').replace('#', '').replace('$', '').replace('%', '').replace('^', '').replace('&','').replace('*', '').replace('(', '').replace(')', '')
	ttx =ttx
	ttx = sorted(ttx)
	print(ttx)
	print("")
	print("Для продовження натисніть - N\nВихід - E")
	u3 = input("Ваш вибір: ")
	if u3 == "N":
		u == "1"
	if u3 == "E":
		break
	else:
		print("Невірно")