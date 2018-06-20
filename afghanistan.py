
#The following is a list that stores blanks and is also used to store the replaced values of the blanks that are used to fill the blanks. 
blanks = ["__1__", "__2__", "__3__", "__4__"]

#The following is a variable that stores the content of easy_level quiz. The formatters are used insert blanks items into the the variable. 
easy_cont = """
	Afghanistan is a country surrounded by the Central Asian republics of Turkmenistan, Uzbekistan, and Tajikstand to the North, \n
	Pakistan to the East and South, Iran to the West and has a small border with {} in the Northeast. {} is the capital of Afghanistan.\n
	Afghanistan is derived from two words, Afghan and stan, which means the {} of Afghans. There are many ethnic groups living in Afghanistan \n
	such as Pashtun, Tajik, Uzbek, Hazara, Pashai, and amongst many others Baloch. The current president of Afghanistan is {}, who is a former World Bank official.
	""".format(blanks[0], blanks[1], blanks[2], blanks[3])

easy_ans = ["China","Kabul","land","Ashraf Ghani"] #This is a list of easy_ans that are used to evaluate user's answer. 

#The following is a variable that stores the content of medium_level quiz. The formatters are used insert blanks items into the the variable. 
medium_cont = """
	Afghanistan is a country surrounded by the Central Asian republics of Turkmenistan, Uzbekistan, and Tajikstand to the {}, \n
	Pakistan to the East and South, {} to the West and has a small border with China in the Northeast. Kabul is the capital of Afghanistan.\n
	In addition to Kabul, the other major cities of Afghanistan are Jalalabad, Kandahar, {} and Mazar-e-sharif. \n
	Afghanistan is derived from two words, Afghan and stan, which means the land of Afghans. There are many ethnic groups living in Afghanistan \n
	such as Pashtun, Tajik, Uzbek, Hazara, Pashai, and amongst many others Baloch. Afghanistan has been in {} since the Soviet Union invaded Afghanistan in 1979.
		""".format(blanks[0], blanks[1], blanks[2], blanks[3])

medium_ans = ["North", "Iran", "Herat", "war"] #This is a list of medium_ans that are used to evaluate user's answer. 

#The following is a variable that stores the content of hard_level quiz. The formatters are used insert blanks items into the the variable. 
hard_cont = """
	Afghanistan is a {} country surrounded by the Central Asian republics of Turkmenistan, Uzbekistan, and Tajikstand to the North, \n
	Pakistan to the East and South, Iran to the West and has a {} km border with China in the Northeast. Kabul is the capital of Afghanistan.\n
	In addition to Kabul, the other major cities of Afghanistan are Jalalabad, Kandahar, Herat and Mazar-e-sharif. \n
	Afghanistan is derived from two words, Afghan and stan, which means the land of Afghans. There are many ethnic groups living in Afghanistan \n
	such as Pashtun, Tajik, Uzbek, Hazara, Pashai, and amongst many others Baloch. {} is the major religion of Afghanistan but there are other religious \n
	minorities such as Sikhs living side by side in peace. Afghanistan has been in war since the Soviet Union invaded Afghanistan in 1979.\n
	{} are the biggest armed group currently fighting the government of Afghanistan as well as its foreign backers.  
		""".format(blanks[0], blanks[1], blanks[2], blanks[3])
	
hard_ans = ["landlocked", "91", "Islam", "Taliban"] #This is a list of hard_ans that are used to evaluate user's answer. 

#The following is the main function which prints a welcome statement. 
#Then, it prompts the user to choose the difficulty level of the quiz they want to take. When the user inputs their favorite level, he/she is directed to that level. 
#if they do not choose one of the levels, easy, medium, or hard, they are prompted again and again until they do so. 

def main():
	print ("""\n \tWelcome to a short but fun quiz. This quiz is on the material of Intro to Programming Nanodegree. It has three levels of difficulty.\n""")
	difficulty_level = input("Please enter easy, medium or hard to select your favorite level of difficulty: ").lower()
	if difficulty_level == "easy":
		blanks_game(easy_cont, easy_ans)
	elif difficulty_level == "medium":
		blanks_game(medium_cont, medium_ans)
	elif difficulty_level == "hard":
		blanks_game(hard_cont, hard_ans)
	else:
		print ("Please only enter easy, medium or hard to take a quiz or you will be prompted again.")
		return main()

#The following function is takes two inputs, one is a string and the other is a list, the outputs are the content of the quiz, the prompts, and the result of each question.
#First, variables attempts, min_attempts, and index are defined after defining the blanks_game function is defined. 
#Second, the while loop starts with a condition that as long as index variable is larger than the length of answers, and the attempts variable is biggers than the min_attempts variable,
#execute the block of code with three branches. First, if the user_response variable that seeks user's input is equal answer, derived from the answers list, 
#then execute the block of code which is printing a correct statement as well as user's input and then printing the whole quiz, and the index variable also increase by 1 each time this block
#of code is run until the quiz is completed.  Second, if the user's answer is not correct, he is given five attempts, after which he is provided the right answer and the loop moves onto the next question until the end. 
#Third, when the index variable is equal to the len(answers), which means the quiz is completed, the user is brought to another function explained below. 


def blanks_game(quiz, answers):
	attempts = 5
	min_attempts = 0
	index = 0
	while index < len(answers) and attempts > min_attempts:
		print ("\n", quiz)
		user_response = input(("\nWhat should be substituted for %s?\n>> ")%blanks[index])
		if user_response == answers[index]: 
			quiz = quiz.replace(blanks[index], user_response)
			print ("\n %r is the correct answer."%user_response,"This is how the text looks now. \n", quiz)
			index += 1
		else:	 
			attempts -= 1 
			print ("That is incorrect. Please try again.", "You have %d attempts left." %attempts)
			if attempts == min_attempts:
				quiz = quiz.replace(blanks[index], answers[index])
				print ("\n here is the answer in case you want to note it down. \t %r \n"%answers[index], quiz)
				index += 1
				attempts += 5
		if index == len(answers):
			replay()

##The following is called when the user completes the blanks_game function, he or she is given a choice if he/she wants to play the game again or a different
#level of the game. If he inputs yes, the main function gets executed which includes the blanks_game function. If he inputs anything but yes, he is greeted with a Game over message. 
def replay():
	print ("You have reached the end of the quiz. Would you like to try this level again or a different level?", "Say yes if you want.")
	try_again = input("> ")
	if try_again == "yes":
		main()
	else:
		print ("Awesome Job. Game over.")
main()