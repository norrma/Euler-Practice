#Combined solutions for Project Euler Questions 1-10

########## Global Functions ##########

import math, sys, time

def isPrime(num):
	#Sanitize input
	if type(num)==float and num%1==0: #If a float value is passed to function but is divisible by 1, convert it to an int and continue 
		num=abs(int(num))
	elif type(num)!=int: #For all other non-int values, return False
		return False	
	else: #For all remaining types (int), get the absolute value of num, as rest of the function assumes only positive integers are passed through
		num=abs(num)
	
	if num<=1: #num=0 and num=1 are not prime, no need to spend time calculating it -> immediately return False
		return False
	elif num<=3: #Covers num=2 and num=3, both are known primes, no need to spend time calculating -> immediately return True
		return True
	
	if num%2==0: #num=2 has already returned True, all future even numbers cannot be prime -> immediately return False
		return False
	else: #Covers all odd numbers after 3
		for i in range(3,int(math.sqrt(num)+1),2): #For loop between 3 and the square root of num (largest factor), jumping by 2 so it will only try to divive by odd numbers
			if num%i==0: #Check if value of num is evenly divisible by any value of i and return False if statement is ever true
				return False
	return True #Failing all other conditions, num must be a prime number -> return True

########## Problem 1 ##########

def euler1(rangeLimit=1000):
	print("Multiples of 3 and 5\nProblem 1\n\nIf we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.\nFind the sum of all the multiples of 3 or 5 below 1000.\n\nhttps://projecteuler.net/problem=1\n\n---------------\n")
	print("Looking at all numbers below "+str(rangeLimit)+" (1000 default)\n")
	
	sum=0

	for i in range(1,rangeLimit+1): #Iterate over all natural numbers between 1 and rangeLimit
		if i%3==0 or i%5==0: #Check if number is evenly divisible by 3 or 5
			sum+=i #Add value of i to a running count
	return sum

########## Problem 2 ##########

def euler2(rangeLimit=4000000):
	print("Even Fibonacci numbers\nProblem 2\n\nEach new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:\n1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...\nBy considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.\n\nhttps://projecteuler.net/problem=2\n\n---------------\n")
	print("Looking at all numbers below "+str(rangeLimit)+" (4000000 default)\n")
	
	fib=[2,1,2,0] #Storing all int values in a list as a different method of storing values
		#fib[0] - Running total of the sum of all even Fibonacci numbers, starts at 2
		#fib[1] - Second last Fibonacci number calculated, starts at 1
		#fib[2] - Previous Fibonacci number calculated, starts at 2
		#fib[3] - Most recent Fibonacci number calculated
	
	while fib[3]<rangeLimit: #Continuously check if the last calculated Fibonaci number is still below rangeLimit
		if fib[3]%2==0: #Check if the last Fibonaci number is even
			fib[0]+=fib[3] #Add even Fibonaci number to the running total
		fib[3]=fib[1]+fib[2] #Calculate next Fibonaci number, done at the end of the loop to ensure while statement works properly
		fib[1]=fib[2] #Push last Fibonaci number to the 'second last' position
		fib[2]=fib[3] #Push most recent Fibonaci number to the 'previous' position
	return fib[0]

########## Problem 3 ##########

def euler3(number=600851475143):
	print("Largest prime factor\nProblem 3\n\nThe prime factors of 13195 are 5, 7, 13 and 29.\nWhat is the largest prime factor of the number 600851475143?\n\nhttps://projecteuler.net/problem=3\n\n---------------\n")
	print("Looking at the largest prime factor of "+str(number)+" (600851475143 default)\n")
	
	largestPrime=1

	if number%2==0: #Check if the provided number is even
		largestPrime=2 #If number is even, we can start with 2 as the largest prime since there are no other possible prime factors
	for i in range(3,int(math.sqrt(number)+1),2): #Since we know 2 is the largest even prime, we can iterate over numbers starting from 3 and jumping by 2 each time, stopping once we reach the square root of the number (largest possible factor)
		if number%i==0: #Check if number is evenly divisible by i
			if isPrime(i): #Check if the value for i is a prime number
				largestPrime=i #Update largest value
	return largestPrime

########## Problem 4 ##########

def euler4(digits=3):
	print("Largest palindrome product\nProblem 4\n\nA palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.\nFind the largest palindrome made from the product of two 3-digit numbers.\n\nhttps://projecteuler.net/problem=4\n\n---------------\n")
	print("Looking at the largest palindrome product of two "+str(digits)+" digit numbers (3 default)\n")
	
	minRange=10**(digits-1) #Figure out the smallest possible value with X digits by calculating 10^(X-1)
	maxRange=10**digits #Figure out the largest possible value with X digits, plus one, by calculating 10^X - for loops will effectively reduce this value by 1
	maxVal=0

	for x in range(minRange,maxRange): #Loop between all possible values with X digits
		for y in range(minRange,maxRange): #Loop again to come up with all possible combinations
			z=x*y #Calculate number
			if str(z)==str(z)[::-1]: #Convert Z to a string and check if reading it forwards and backwards yields the same result (palindrome)
				if z > maxVal: #Check if palindromic number is larger than our previous largest palindrome
					maxVal=z #Update largest value found
	return(maxVal)

########## Problem 5 ##########

def factorGen(num,primeList):
	
	factors=[]
	
	if num in primeList: #If num is prime, append to factors list and return that value
		factors.append(num)
		return factors
	else:
		while not num in primeList: #Continually check if num is prime, if not, then continue calculating prime factors
			for i in primeList: #Loop through primes starting from smallest to largest
				if num%i==0: #Find smallest prime factor for num, then append value to list
					factors.append(i)
					num/=i #Update num value by dividing it by its smallest prime factor
					break #Break from for loop to re-evaluate while loop condition
		factors.append(int(num)) #Once num is prime, append to list
		return factors #Return list of prime factors that comprise num

def euler5(rangeLimit=20):
	print("Smallest multiple\nProblem 5\n\n2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.\nWhat is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?\n\nhttps://projecteuler.net/problem=5\n\n---------------\n")
	print("Looking for the smallest positive number evenly divisible from 1 to "+str(rangeLimit)+" (20 default)\n")
	
	result=1
	primeList=[] #List of prime numbers between 2 and rangeLimit
	primeFactors=[] #Running list of prime factors for all numbers between 2 and rangeLimit
	
	#Approach here is to calculate prime factorization of all numbers between 1 and rangeLimit, then multiply all prime factors for 1-rangeLimit to get the smallest possible sum divisible by all numbers in rangeLimit

	for i in range(2,rangeLimit+1): #For loop starting at 2 and ending at rangeLimit to check for all prime numbers in that range
		if isPrime(i):
			primeList.append(i)
	for i in range(2,rangeLimit+1): #For loop starting at 2 and ending at rangeLimit
		tempList=factorGen(i,primeList) #Get all prime factors of i from the factorGen function, named tempList since it will be overwritten each time it loops
		for x in tempList: #Loop through list of prime factors of i
			if not x in primeFactors: #Check if a factor does not exist in the primeFactors list
				for y in range(tempList.count(x)): #Check how many instances the given factor shows up in tempList
					primeFactors.append(x) #Add that many instances of the factor to the primeFactors list
			else: #If a factor already exists in the primeFactors list
				difference=tempList.count(x) - primeFactors.count(x) #Compare number of occurrences of the factor in tempList with primeFactors
				if difference > 0: #Check if there are more instances of the factor in tempList than in primeFactors
					for y in range(difference): #Add a number of entries of the factor to primeFactors equal to the difference
						primeFactors.append(x)
	for i in primeFactors:
		result*=i #Multiply all values in primeFactors
	return result #Return smallest possible number divisible by all numbers in rangeList

########## Problem 6 ##########

def euler6(natRange=100):
	print("Sum square difference\nProblem 6\n\nThe sum of the squares of the first ten natural numbers is,\n1^2 + 2^2 + ... + 10^2 = 385\nThe square of the sum of the first ten natural numbers is,\n(1+2+...+10)^2 = 55^2 = 3025\nHence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is\n3025-385=2640\n\nFind the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.\n\nhttps://projecteuler.net/problem=6\n\n---------------\n")
	print("Looking for different between sum of squares of the first "+str(natRange)+" natural numbers (100 default) and the square of the sum.\n")
	
	sumSquares=0
	squareSum=0

	for i in range (1,natRange+1): #Iterate between 1 and natRange
		sumSquares+=(i**2) #Add squared value of i to make up the sum of squared numbers between i and natRange
		squareSum+=i #Add value to running total
	squareSum=squareSum**2 #Square running total to get the squared value of all sums between 1 and natRange
	return squareSum - sumSquares #Retrun difference between squared value of all sums and the sum of all squared values between i and natRange

########## Problem 7 ##########

def euler7(endVal=10001):
	print("10001st prime\nProblem 7\n\nBy listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.\nWhat is the 10001st prime number?\n\nhttps://projecteuler.net/problem=7\n\n---------------\n")
	print("Returning prime number at position "+str(endVal)+" (10001 default)\n")
	
	primeNumbers=[2] #Smallest prime number, but also largest even prime
	counter=3 #Second smallest prime number - starting point

	while len(primeNumbers) < endVal: #Continue looping as long as we have fewer than endVal prime numbers
		if isPrime(counter): #Check if the counter value is prime
			primeNumbers.append(counter) #Append value to primeNumber list
		counter+=2 #Increase counter by 2, no need to look at any even numbers after 2
	return primeNumbers[-1] #Return last value in primeNumber list

########## Problem 8 ##########

def euler8():
	print("Largest product in a series\nProblem 8\n\nThe four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.\n\n-Refer to problem page for 1000-digit number-\n\nFind the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?\n\nhttps://projecteuler.net/problem=8\n\n---------------\n")
	print("Problem using default values from Project page, not updated to accept other input\n")
	
	value=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
	strVal=str(value) #Store 1000-digit int as a string to allow for easier manipulation
	lenVal=len(strVal) #Calculate length of string
	slice=13 #Default 'slicing' value for problem
	maxVals={
		"sum": 0, #Dict val for the sum of the largest possible product
		"values": [0] #Dict val for the list of numbers that make up the largest product, used for testing/troubleshooting
	}

	for i in range(lenVal-slice): #For loop that iterates through all possible starting positions that can make up 13 digits
		tally=1 #Running tally for product of 13 digits
		runningList=[] #Running list of numbers making up the product
		for x in range(slice): #For loop iterating a number of times equal to the size of the slice
			tally*=int(strVal[i+x]) #Calculate the product of all values starting at i, and ending at i+slice
			runningList.append(strVal[i+x]) #Store digits used to get that product
		if tally > maxVals.get("sum"): #Check if the current sum is larger than the previous largest sum, and update dictionary with new values if true
			maxVals["sum"]=tally
			maxVals["values"]=runningList
	return maxVals["sum"] #Return largest product

########## Problem 9 ##########

def cCalc(a,b):
	c=math.sqrt((a**2+b**2)) #Calculate value that C has to be given values of A and B
	if c%1 > 0: #Check if C is a proper integer (i.e. properly divisible by 1)
		return 0 #If not a proper integer, return 0
	else:
		return int(c) #If C is a proper integer, return value of C

def tripletCheck(a,b,c,sum): #Function to calculate if the end condition for this problem has been met
	if a < b < c: #Validate that values meet requirement in problem - only time this wouldn't be true is when the cCalc function returns 0 for the value of varC
		if a+b+c == sum: #Verify if the end condition has been met
			return True #Return True only if the end condition has been met
	return False

def euler9():
	print("Special Pythagorean triplet\nProblem 9\n\nA Pythagorean triplet is a set of three natural numbers, a < b < c, for which,\na^2 + b^2 = c^2\n\nFor example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.\n\nThere exists exactly one Pythagorean triplet for which a + b + c = 1000.\nFind the product abc.\n\nhttps://projecteuler.net/problem=9\n\n---------------\n")
	print("Problem using default values from Project page, not updated to accept other input\n")
	
	endSum=1000
	varA=1
	varB=2
	varC=5
	
	#Approach here is to bruteforce possible values of A and B, and reverse what the value for C should be before checking if the three values make up the pythagorean triplet for 1000

	while not tripletCheck(varA,varB,varC,endSum): #While loop using the tripletCheck function to determine if the end condition has been met or not before breaking -> risk of looping infinitely if no result can be found
		varB+=1 #Increment value of B
		for a in range(1,varB): #Loop through values from 1 to varB-1 for all possible values for A
			varC=cCalc(a,varB) #Calculate the value for C
			if varC > 0: #cCalc function will return 0 if the value of C was not a proper integer
				varA=a #update value for A
				if tripletCheck(varA,varB,varC,endSum): #Validate if the end condition has already been met, if so, break from the loop, bit of an awkward double-check going on due to how the loops are nested
					break
	return(varA*varB*varC) #Return product of ABC

########## Problem 10 ##########

def euler10(upperLimit=2000000):
	print("Summation of primes\nProblem 10\n\nThe sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.\nFind the sum of all the primes below two million.\n\nhttps://projecteuler.net/problem=10\n\n---------------\n")
	print("Finding the sum of all primes below "+str(upperLimit)+" (2000000 default)\n")
	
	if abs(upperLimit) > 1: #Check if upperLimit is 2 or greater, if true we know that the smallest (and only even) prime number starts at 2
		primes=[2]
	else: #If upperLimit is 1 or lower, it cannot contain any prime numbers --> return 0
		return 0 

	for i in range(3,upperLimit+1,2): #For loop for all odd values between 3 and upperLimit+1
		if isPrime(i): #Calls isPrime function to check if value is a prime number
			primes.append(i) #Appends value to primes list if isPrime returns true
	return sum(primes) #Return sum of all values in the primes list

########## Main ##########

def main():
	functions = { #Using a dictionary to map functions as a way to create a 'switch' statement within python
		1: euler1,
		2: euler2,
		3: euler3,
		4: euler4,
		5: euler5,
		6: euler6,
		7: euler7,
		8: euler8,
		9: euler9,
		10: euler10
	}

	start_time=time.time() #Log start time
	
	arg_names=['script','problem','parameter'] #Accept up to 3 commandline arguments - script argument will always be the filename, ignored in tests below
	args=dict(zip(arg_names, sys.argv)) #Map given arguments to the arg_names above

	if len(args) > 1: #Validate if 2 or more arguments are provided (i.e. 1 more argument after scriptname)
		try:
			problem_to_run=functions.get(int(args['problem'])) #Validate that argument 2 is an int value
		except ValueError:
			print("Error with argument 1; only integers accepted") #If not an int, state error and exit
			sys.exit()
		
		if len(args)==3: #Check if arg3 was provided
			try:
				print(problem_to_run(int(args['parameter']))) #Attempt to run problem with optional parameter, will succeed if arg3 is an int
			except ValueError:
				print("Error with argument 2; only integers accepted") #If arg3 is not an integer, state error and exit
		else: #Otherwise run problem without optional argument
			try: 
				print(problem_to_run()) #Attempt to run problem without optional parameter, will succeed if arg2 is in scope of the function dict
			except TypeError:
				print("Error with argument 1; problem out of scope") #If arg2 is out of scope, state error and exit
				sys.exit()
	else: #If 1 or fewer arguments, state that and exit
		print("Insufficient arguments")
		sys.exit()

	print("Runtime: "+str(round(time.time()-start_time,2)))	#Display time taken for troubleshooting/efficiency purposes

if __name__=="__main__":
	main()