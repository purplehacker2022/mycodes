from sys import prefix


inputed_list = ['mix', 'xyz', 'apple']
print("the inputed list=",str(inputed_list))
prefix_word= "PREFIX_"
pres = [prefix_word + sub for sub in inputed_list]
print( "the output list= ", pres)