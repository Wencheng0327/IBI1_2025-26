#7
#initialize virables, input data and convert them into suitable types
#chenk whether the variables are in their right range
#if not: print to point out which is in wrong range, and assign a boolean false
#else: going on
#check the boolean: if true, calculate CrCl
#define the formular of CrCl using age, weight, gender and Cr
#print the result

def CrCl (age, weight, gender, Cr):
    if gender == "male":
        CrCl = (140 - age ) * weight / ( 72 * Cr )
    else:
        CrCl = (140 - age ) * weight / ( 72 * Cr ) * 0.85
    print ( "CrCl is:" , CrCl )

age = int ( input ( "age: " ) )
weight = float ( input ( "weight: " ) )
gender = input ( "male or female: " )
Cr = float ( input ( "creatine	concentration: " ) )
corrected_range = True
if age <=0 or age > 100: 
    print ( "age needs to be smaller than 100." )
    corrected_range = False
if weight <= 20 or weight >= 80:
    print ( "weight needs to be between 20 and 80." )
    corrected_range = False
if Cr <= 0 or Cr >= 100:
    print ( "Cr needs to be between 0 and 100." )
    corrected_range = False
if not ( gender == "male" or gender == "female" ) :
    print ( "gender needs to be male or female." )
    corrected_range = False

if corrected_range: CrCl (age, weight, gender, Cr)