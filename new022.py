def main():
	f1=1
	n=int(input())
	for i in range(1,n):
		f1=f1*i
	print(f1)
try:
	main()
except:
	print('invalid')
