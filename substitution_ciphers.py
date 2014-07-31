alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
balpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
CIPHERLISTS=[[]]
VIGNERESQUARE=[[]]

def shiftalph(tLIST,SHIFTVALUE):
	i=0
	LIST=list(tLIST)
	if(SHIFTVALUE > len(alpha)):
		print str(SHIFTVALUE) + " is to big a shift for the alphabet 1-26"
		return LIST
	else:
		LEFTSIDE=[]
		while (SHIFTVALUE > i):
			LEFTSIDE.insert(0,LIST[-1])
			del LIST[-1]
			i=i+1
		LIST=LEFTSIDE+LIST
		print "Shift of: " + str(SHIFTVALUE) + " - Cipher Length: " + str(len(LIST))
	return LIST

def main():
	i=1
	balpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	shifted=list(balpha)
	while(i<=26):
		tlist=list(shiftalph(shifted, i))
		i=i+1
		CIPHERLISTS.insert(0,list(tlist))
	VIGNERESQUARE=list(CIPHERLISTS)
	print VIGNERESQUARE

if __name__ == '__main__':
	main()
