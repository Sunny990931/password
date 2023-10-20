password = 'a123'
i = 3
while i > 0:
	mima = input ('請輸入密碼: ')
	if mima == password:
		print('輸入正確')
		break
	else :
		i = i - 1
		print('輸入錯誤! ')
		if i > 0 :
			print ('剩下', str(i) , '次機會')
		else :
			print('你沒機會了')
	