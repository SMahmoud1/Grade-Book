#------------------------------------------------------------------------------
#Student Name: Salma Mahmoud / Assignment: P#3 / Date: 10/05/2012
#------------------------------------------------------------------------------
#Honor Code Statemant: I receivied no assistance on this assignment that 
#violates the ethical guidelines set fourth by professor and class syllabus
#------------------------------------------------------------------------------
#References: Class powerpoints, Python textbook, tutoring
#------------------------------------------------------------------------------
#Comments: I am attempting the extra credit
#------------------------------------------------------------------------------
#Pseudocode: 
#BEGIN
#from math, import the square-root funtion
#set 'scores' equal to an empty set
#set options equal to string '0 - Clear out scores
#1 - Input more scores
#2 - Display all scores
#3 - Get average score
#4 - Get standard deviation of scores
#5 - Get high score
#6 - Get low score
#7 - Quit
#8 - Get mode score
#Input choice :'
#set variable 'choose_again' is set to equal 'true'
#while choose_again is true
#   option variable is set equal to input(options)
#   if option is equal to string '0'
#       'scores' equals an empty set
#	elif option is equal to string '1'
#		set varible num_scores equal to integer input asking 'how many new scores?'
#		for every x in the range of num_scores
#			scores append the float input of the numbers '#: '
#	elif option is equal to string '2'
#		print string 'there are ' plus the string of the length of the scores list
#		plus string 'scores.'
#		for every x in scores
#			print string '	' plus string x
#	elif option is equal to string '3'
#		set the varaible 'total' equal to 0
#		for every x in scores
#			total  equals total plus x
#		avg_number equals 'total' divided by length of scores list
#	elif option is equal to string '4'
#		set total_1 equals 0
#		for every x in scores
#			total_1 equals total_1 plus x
#		avg equals 'total_1' divided by length of scores
#
#		set total_2 equals 0
#		for every x in scores
#			total_2 equals 'total_2' plus 'x' minus 'avg' squared
#		std (standard devition) equals square root of 'total_2' divided by 
#		'length of scores'
#		print string 'Standard Deviation: ' plus string 'std'
#	elif option is equal to string '5'
#		set max_number equals 0
#		for every x in scores
#			if x is larger than max_number
#				max_number will equal x
#		set count equal to 0
#		for every x in scores
#			if x equals max_number
#				count equals count plus 1
#		print string 'High score: " plus string 'max_number'
#		print string 'count' plus string 'people got this score.'
#	elif option is equal to string '6'
#		set min_number equal to 100
#		for every x in scores
#			if x is less than min_number
#				min_number wil equal x
#		set count equal to 0
#		for every x in scores
#			if x equal min_number
#				count equals count plus 1
#		print sring 'Low scores: ' plus string 'min_number'
#		print string 'count' plus string 'people go this score'
#	elif option is equal to string '7'
#		print string 'Good-bye!'
#		choose_again equals False
#	elif option is equal to string '8'
#		set flip to equal True
#		while flip is True
#			flip equals False
#			for every x in range of length of scores minus 1
#				if scores set 'x' is more than scores set 'x plus 1'
#					tempor will equal scores x
#					scores set 'x' equals scores set 'x plus 1'
#					scores x plus 1 equals tempor
#					flip equals true
#			mode_score will equal empty set
#			occurance will equal set of '0'
#			current_score will eqaul score set '0'
#			mode_score append current set
#			number equals 0
#			for every x in scores
#				if x equals current
#					set occurence set to set number equal to occurence set set number plus 1
#				else
#					occurance append 1 to set
#					mode_score append x to set
#					current_score will equal x
#					number equals number plus 1
#				max_number equal 0
#				for every x in occurance
#					if x is more than max_number
#						max_number will equal x
#				count will equal 0
#				for every x in occerance
#					if x equals max_number
#						count equals count plus 1
# 				print string '# of Modes: " plus string count
#				print string 'Score occured " plus string max_number plus string 'times'
#				for every x in the range of the length of 'occurance'
#					if occurance set x equals max_number
#						print string '#: ' plus string mode_score set x
#				for every x in range of the length of occerence
#					if occurance set x equals max_number
#						print string '#: ' plus string mode_score set x
#	else
#		print string 'Invalid inputs, please try again.'
#END
#------------------------------------------------------------------------------

from math import sqrt

scores=[]

options="""
0 - Clear out scores
1 - Input more scores
2 - Display all scores
3 - Get average score
4 - Get standard deviation of scores
5 - Get high score
6 - Get low score
7 - Quit
8 - Get mode score
Input choice :"""

choose_again = True
while(choose_again):
    option = input(options)

    if(option == "0"):
        scores = []
        
    elif(option=="1"):
        num_scores = int(input("How many new scores? "))
        for x in range(num_scores):
            scores.append(float(input("#: ")))

    elif(option=="2"):
        print("There are "+str(len(scores))+" scores.")
        for x in scores:
            print("\t"+str(x))

    elif(option=="3"):
        total = 0
        for x in scores:
            total += x
        avg_number = total / len(scores)
        print("Average score: " + str(avg_number))

    elif(option=="4"):
        total = 0
        for x in scores:
            total += x
        avg = total / len(scores)

        total2 = 0
        for x in scores:
            total2 += (x - avg)**2
        std = sqrt(total2 / len(scores))
        print("Standard Deviation: " + str(std))
        
    elif(option=="5"):
        max_number = 0
        for x in scores:
            if(x > max_number):
                max_number = x

        count = 0
        for x in scores:
            if(x == max_number):
                count += 1
                
        print("High score: " + str(max_number))
        print(str(count) + " people got this score")

    elif(option=="6"):
        min_number = 100
        for x in scores:
            if(x < min_number):
                min_number = x

        count = 0
        for x in scores:
            if(x == min_number):
                count += 1

        print("Low score: " + str(min_number))
        print(str(count) + " people got this score")
        
    elif (option=="7"):
        print("Goodbye!")
        break
		
    elif (option=="8"):
        flip = True
        while(flip):
            flip = False
            for x in range(len(scores) - 1):
                if(scores[x] > scores[x+1]):
                    temp = scores[x]
                    scores[x] = scores[x+1]
                    scores[x+1] = temp
                    flip = True
					
        mode_score = []
        occurance = [0]
        current_score = scores[0]
        mode_score.append(current)
        num = 0
        for x in scores:
            if(x == current_score):
                occurance[num] += 1
            else:
                occurance.append(1)
                mode_score.append(x)
                current_score = x
                num += 1
				
        max_number = 0
        for x in occurance:
            if(x > max_number):
                max_number = x        
        count = 0
        for x in occurance:
            if(x == max_number):
                count += 1
        print("# of Modes: " + str(count))
        print("Score occured " + str(max_number) + " times")
        for i in range(len(occurance)):
            if(occurance[i] == max_number):
                print("#: " + str(mode_score[i]))
    else:
        print("Invalid inputs, please try again. ")