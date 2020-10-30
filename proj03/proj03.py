###############################################################################
# Project 03
# Algorithm
#   Prompts for residency, then level
#   Depending on level: 
#       prompts for college then specific major (CMSE)
#       prompts for admittance to Engineering college or if in James Madison 
#   Prompts for credits 
#   Calculates the Fall 2019 semester tuition cost
#   Reprompts if user wants to do another calculation
#       If yes, cycle beings again because processes explained in lines 12-17 
#       exist within loops
#       If no, program ends
#
###############################################################################

# Following lines show the per-credit costs as well as flat-rate costs for
# differing levels, denoted by: residency_level_type-of-cost
# RES = resident | FR = freshman | SO = sophomore | JU = junior | SE = senior
# INTR = international | PER = per-credit | FLT = flat-rate
RES_FR_PER = 482
RES_FR_FLT = 7230
RES_SO_PER = 494
RES_SO_FLT = 7410
RES_JU_SE_PER = 555
RES_JU_SE_FLT = 8325
INTR_FR_SO_PER = 1325.5
INTR_FR_SO_FLT = 19883
INTR_JU_SE_PER = 1366.75
INTR_JU_SE_FLT = 20501
SPE_RES_JU_SE_PER = 573
SPE_RES_JU_SE_FLT = 8595
SPE_INTR_JU_SE_PER = 1385.75
SPE_INTR_JU_SE_FLT = 20786
# Following lines show fees (denoted by FEE), followed by college and time
# BUS = Business college fee | ENG_CMSE = Engineering and/or CMSE fee
# HLTH_SCI = Health/Science college fees | INTR = international fees
# PT = part-time | FT = full-time
FEE_BUS_PT = 113
FEE_BUS_FT = 226
FEE_ENG_CMSE_PT = 402
FEE_ENG_CMSE_FT = 670
FEE_HLTH_SCI_PT = 50
FEE_HLTH_SCI_FT = 100
FEE_INTR_PT = 375
FEE_INTR_FT = 750
# Taxes and their reasons; these are straightforward denotations
TAX_ASMSU = 21
TAX_RADIO = 3
TAX_NEWS = 5
TAX_JMC = 7.5

# Code actually starts here
print("2019 MSU Undergraduate Tuition Calculator.\n")
resident = input("Resident (yes/no): ")
resident = resident.lower()
# Testing out how to use a function, only used once / is specific because of so 
# many different situations and stipulations
def cost_0_credit_4_ju_se(credit_int):
    cost = SPE_RES_JU_SE_PER * credit_int
    fees = FEE_BUS_PT + TAX_ASMSU + TAX_RADIO
    total_cost = cost + fees
    if major_cmse == "yes":
        total_cost = total_cost + FEE_ENG_CMSE_PT
    print("Tuition is ${:,.2f}.".format(total_cost))

# The format of the rest of the code is very similar in structure, repeated for
# way too long. Comments made on the first general structure will therefore
# be representative of the following structures, though specific variables will
# change in order to create different scenarios and different tuition amounts.

while resident == 'yes':
    level = input("Level—freshman, sophomore, junior, senior: ")
    level = level.lower()
    # Following line is at an indent that indicates level
    if level == "junior" or level == "senior":
        #asks for college at junior / senior level as well as CMSE major
        college = input("Enter college as business, engineering, health, " \
                        "sciences, or none: ")
        college = college.lower() #ensures answers like yEs & YES can work 
        major_cmse = input("Is your major CMSE (“Computational Mathematics " \
                           "and Engineering”) (yes/no): ")
        major_cmse = major_cmse.lower() #again ensures end answer is "yes"
        # Following if structures (elif,else) at this indent ask for college
        if college == "business":
            credit = input("Credits: ")
            # following indent level if for this try-except function used to
            # test input for if it can be made an integer
            try:
                credit_int = int(credit)
            except: #if not, exception code runs, which is in a while loop to
                    # guarantee an integer eventually is entered
                while credit == credit:
                    print("Invalid input. Try again.") #error message
                    credit = input("Credits: ") #reprompting, moving on to try
                    try: 
                        credit_int = int(credit) #try to make input an integer
                        if type(credit_int) is int: #if possible, breaks while
                            break 
                    except: #if not, reruns while loop until integer is entered
                        continue 
                else: 
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0: #Ensures that input is positive
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            while credit_int % 1 != 0: #ensures input is an integer, not float
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            if 0 < credit_int <= 4: #scenario when credits are between 1 and 4
                cost_0_credit_4_ju_se(credit_int) #function made in line 66
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") #reprompts
                another_calc = another_calc.lower() #makes answer interpretable
                if another_calc == "yes": 
                    resident = input("Resident (yes/no): ") 
                    #gets input needed to perpetuate the while loop (line 79)
                    resident = resident.lower() 
                    continue
                else:
                    break
            elif credit_int == 5: #for 5 credits (different fees from 4 & 6)
                #134 is per-credit cost (for engineering/business) * credits
                cost = SPE_RES_JU_SE_PER * credit_int 
                fees = FEE_BUS_FT + TAX_ASMSU + TAX_RADIO #Fees for 5 credits
                total_cost = cost + fees
                if major_cmse == "yes": #if that adds CMSE fee if needed
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) #prints cost
                #following lines follow comments in lines 122-131
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ")
                another_calc = another_calc.lower() 
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            #Structure repeats itself, follows same comments as prior
            elif 6 <= credit_int < 12:
                cost = SPE_RES_JU_SE_PER * credit_int
                fees = FEE_BUS_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost))                 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ")
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 12 <= credit_int <= 18:
                cost = SPE_RES_JU_SE_FLT #different here is variable(flat rate)
                fees = FEE_BUS_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ")
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            #calculates with flat-rate & per-credit variables.   
            elif credit_int >= 19:
                SRJSF = SPE_RES_JU_SE_FLT # only here to shorten next line
                cost = SRJSF + ((credit_int - 18) * SPE_RES_JU_SE_PER)
                fees = FEE_BUS_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
        #from here on out the code is the same structure for every possible 
        #possible scenario, with general comments made above applicable.        
        elif college == "engineering":
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            while credit_int % 1 != 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            if 0 < credit_int <= 4:
                cost = SPE_RES_JU_SE_PER * credit_int
                fees = FEE_ENG_CMSE_PT + TAX_ASMSU + TAX_RADIO
                total_cost = cost + fees
                if major_cmse == "yes":
                    total_cost = total_cost
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int == 5:
                cost = SPE_RES_JU_SE_PER * credit_int
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 6 < credit_int < 12:
                cost = SPE_RES_JU_SE_PER * credit_int
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 12 <= credit_int <= 18:
                cost = SPE_RES_JU_SE_FLT
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int >= 19:
                SRJSF = SPE_RES_JU_SE_FLT #to shorten next line to under 80 ch.
                cost = SRJSF + (SPE_RES_JU_SE_PER * (credit_int - 18))
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
        elif college == "health" or college == "sciences":
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            while credit_int % 1 != 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            if 0 < credit_int <= 4:
                cost = RES_JU_SE_PER * credit_int
                fees = FEE_HLTH_SCI_PT + TAX_ASMSU + TAX_RADIO
                total_cost = cost + fees
                if major_cmse == "yes":
                    total_cost = total_cost + FEE_ENG_CMSE_PT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int == 5:
                cost = RES_JU_SE_PER * credit_int
                fees = FEE_HLTH_SCI_FT + TAX_ASMSU + TAX_RADIO
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 6 <= credit_int < 12:
                cost = RES_JU_SE_PER * credit_int
                fees = FEE_HLTH_SCI_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ")
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 12 <= credit_int <= 18:
                cost = RES_JU_SE_FLT
                fees = FEE_HLTH_SCI_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ")
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int >= 19:
                cost = RES_JU_SE_FLT + (RES_JU_SE_PER * (credit_int - 18))
                fees = FEE_HLTH_SCI_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
        else:
            jmc = input("Are you in the James Madison College (yes/no): ")
            jmc = jmc.lower()
            
            if jmc == "yes":
                credit = input("Credits: ")
                credit = credit
                try:
                    credit_int = int(credit)
                except:
                    while credit == credit:
                        print("Invalid input. Try again.")
                        credit = input("Credits: ")
                        try: 
                            credit_int = int(credit)
                            if type(credit_int) is not int:
                                continue
                            
                            
                        except:
                            credit_int = (int(credit))
            
                while credit_int <= 0:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    credit_int = float(credit_int)
                while credit_int % 1 != 0:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    credit_int = float(credit)
                if 0 < credit_int <= 4:
                    cost = RES_JU_SE_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":
                        total_cost = total_cost + FEE_ENG_CMSE_PT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int == 5:
                    cost = RES_JU_SE_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 6 <= credit_int < 12:
                    cost = RES_JU_SE_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 12 <= credit_int <= 18:
                    cost = RES_JU_SE_FLT
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int >= 19:
                    cost = RES_JU_SE_FLT + (RES_JU_SE_PER * (credit_int - 18))
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break    
            else:  
                while True:
                  credit = input("Credits: ")
                  if not credit.isdigit() or int(credit) == 0:
                    print("Invalid input. Try again.")

                  else:
                    credit_int = int(credit)
                    break


                
                
                
                credit_int = credit_int
                
                while credit_int <= 0:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    credit_int = float(credit_int)
                while credit_int % 1 != 0:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    credit_int = float(credit)
                if 0 < credit_int <= 4:
                    cost = RES_JU_SE_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO
                    total_cost = cost + fees
                    if major_cmse == "yes":
                        total_cost = total_cost + FEE_ENG_CMSE_PT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int == 5:
                    cost = RES_JU_SE_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 6 <= credit_int < 12:
                    cost = RES_JU_SE_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 12 <= credit_int <= 18:
                    cost = RES_JU_SE_FLT
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int >= 19:
                    cost = RES_JU_SE_FLT + (RES_JU_SE_PER * (credit_int - 18))
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
        
        
###############################################################################
########################## FRESHMAN CALCULATIONS ##############################
###############################################################################
        
        
    elif level == 'freshman':
        admitted_egr = input("Are you admitted to the " \
                             "College of Engineering (yes/no): ")
        admitted_egr = admitted_egr.lower()
        
        if admitted_egr == "yes":
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            while credit_int % 1 != 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            if 0 < credit_int <= 4:
                cost = RES_FR_PER * credit_int
                fees = FEE_ENG_CMSE_PT + TAX_ASMSU + TAX_RADIO
                total_cost = cost + fees
                if major_cmse == "yes":
                    total_cost = total_cost + FEE_ENG_CMSE_PT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int == 5:
                cost = RES_FR_PER * credit_int
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 6 <= credit_int < 12:
                cost = RES_FR_PER * credit_int
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 12 <= credit_int <= 18:
                cost = RES_FR_FLT
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int >= 19:
                cost = RES_FR_FLT + (RES_FR_PER * (credit_int - 18))
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
        else: 
            jmc = input("Are you in the James Madison College (yes/no): ")
            jmc = jmc.lower()
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            while credit_int % 1 != 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            if jmc == "yes":
                if 0 < credit_int <= 4:
                    cost = RES_FR_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":
                        total_cost = total_cost + FEE_ENG_CMSE_PT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int == 5:
                    cost = RES_FR_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 6 <= credit_int < 12:
                    cost = RES_FR_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 12 <= credit_int <= 18:
                    cost = RES_FR_FLT
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int >= 19:
                    cost = RES_FR_FLT + (RES_FR_PER * (credit_int - 18))
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
            else:
                if 0 < credit_int <= 4:
                    cost = RES_FR_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO
                    total_cost = cost + fees
                    if major_cmse == "yes":
                        total_cost = total_cost + FEE_ENG_CMSE_PT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int == 5:
                    cost = RES_FR_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 6 <= credit_int < 12:
                    cost = RES_FR_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 12 <= credit_int <= 18:
                    cost = RES_FR_FLT
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                    total_cost = cost + fees
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int >= 19:
                    cost = RES_FR_FLT + (RES_FR_PER * (credit_int - 18))
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break


##############################################################################
########################## SOPHOMORE CALCULATION #############################
##############################################################################
                        
                                 
    elif level == "sophomore":
        admitted_egr = input("Are you admitted to the " \
                             "College of Engineering (yes/no): ")
        admitted_egr = admitted_egr.lower()
        major_cmse = input("Is your major CMSE (“Computational Mathematics " \
                           "and Engineering”) (yes/no): ")
        major_cmse = major_cmse.lower()
        if admitted_egr == "yes":
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
        while credit_int <= 0:
            print("Invalid input. Try again.")
            credit = input("Credits: ")
            credit_int = int(credit)
        if admitted_egr == "yes":
            if 0 < credit_int <= 4:
                cost = RES_SO_PER * credit_int
                fees = FEE_ENG_CMSE_PT + TAX_ASMSU + TAX_RADIO
                total_cost = cost + fees
                if major_cmse == "yes":
                    total_cost = total_cost + FEE_ENG_CMSE_PT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int == 5:
                cost = RES_SO_PER * credit_int
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 6 <= credit_int < 12:
                cost = RES_SO_PER * credit_int
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 12 <= credit_int <= 18:
                cost = RES_SO_FLT
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int >= 19:
                cost = RES_SO_FLT + (RES_SO_PER * (credit_int - 18))
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO + TAX_NEWS
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
        else: 
            jmc = input("Are you in the James Madison College (yes/no): ")
            jmc = jmc.lower()
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            while credit_int % 1 != 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            if jmc == "yes":
                if 0 < credit_int <= 4:
                    cost = RES_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":
                        total_cost = total_cost + FEE_ENG_CMSE_PT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int == 5:
                    cost = RES_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 6 <= credit_int < 12:
                    cost = RES_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 12 <= credit_int <= 18:
                    cost = RES_SO_FLT
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int >= 19:
                    cost = RES_SO_FLT + (RES_SO_PER * (credit_int - 18))
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
            else:
                if 0 < credit_int <= 4:
                    cost = RES_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO
                    total_cost = cost + fees
                    if major_cmse == "yes":
                        total_cost = total_cost + FEE_ENG_CMSE_PT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int == 5:
                    cost = RES_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 6 <= credit_int < 12:
                    cost = RES_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 12 <= credit_int <= 18:
                    cost = RES_SO_FLT
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int >= 19:
                    cost = RES_SO_FLT + (RES_SO_PER * (credit_int - 18))
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                
    else:
        print("Invalid input. Try again.")
        continue
while resident != "yes":
    international = input("International (yes/no): ")
    intr = international.lower()
    level = input("Level—freshman, sophomore, junior, senior: ")
    level = level.lower()
    if level == "junior" or level == "senior":
        college = None
        college = input("Enter college as business, engineering, health, " \
                        "sciences, or none: ")
        college = college.lower()
        major_cmse = input("Is your major CMSE (“Computational Mathematics " \
                           "and Engineering”) (yes/no): ")
        major_cmse = major_cmse.lower()
            
        
        if college == "business":
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            while credit_int % 1 != 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            if 0 < credit_int <= 4:
                cost = INTR_JU_SE_PER * credit_int
                fees = FEE_BUS_FT + TAX_ASMSU + TAX_RADIO + FEE_INTR_PT
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int == 5:
                cost = INTR_JU_SE_PER * credit_int
                fees = FEE_BUS_FT + TAX_ASMSU + TAX_RADIO + FEE_INTR_FT
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 6 <= credit_int < 12:
                cost = INTR_JU_SE_PER * credit_int
                tax =  TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_BUS_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost))                 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 12 <= credit_int <= 18:
                cost = INTR_JU_SE_FLT
                tax =  TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_BUS_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
               
            elif credit_int >= 19:
                cost = INTR_JU_SE_FLT + ((credit_int - 18) * INTR_JU_SE_PER)
                tax =  TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_BUS_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
        elif college == "engineering":
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            while credit_int % 1 != 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            if 0 < credit_int <= 4:
                cost = INTR_JU_SE_PER * credit_int
                fees = FEE_ENG_CMSE_PT + TAX_ASMSU + TAX_RADIO + FEE_INTR_FT
                total_cost = cost + fees
                if major_cmse == "yes":
                    total_cost = total_cost
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int == 5:
                cost = INTR_JU_SE_PER * credit_int
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO + FEE_INTR_FT
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 6 < credit_int < 12:
                cost = INTR_JU_SE_PER * credit_int
                tax = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_ENG_CMSE_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 12 <= credit_int <= 18:
                cost = INTR_JU_SE_FLT
                tax = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_ENG_CMSE_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int >= 19:
                cost = INTR_JU_SE_FLT + (INTR_JU_SE_PER *(credit_int - 18))
                tax = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_ENG_CMSE_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
        elif college == "health" or college == "sciences":
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            while credit_int % 1 != 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            if 0 < credit_int <= 4:
                cost = INTR_JU_SE_PER * credit_int
                fees = FEE_HLTH_SCI_PT + TAX_ASMSU + TAX_RADIO + FEE_INTR_FT
                total_cost = cost + fees
                if major_cmse == "yes":
                    total_cost = total_cost + FEE_ENG_CMSE_PT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int == 5:
                cost = INTR_JU_SE_PER * credit_int
                fees = FEE_HLTH_SCI_FT + TAX_ASMSU + TAX_RADIO + FEE_INTR_FT
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 6 <= credit_int < 12:
                cost = INTR_JU_SE_PER * credit_int
                tax = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_HLTH_SCI_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 12 <= credit_int <= 18:
                cost = INTR_JU_SE_FLT
                tax = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_HLTH_SCI_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int >= 19:
                cost = INTR_JU_SE_FLT + (INTR_JU_SE_PER *(credit_int - 18)) 
                tax = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_HLTH_SCI_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
        else:
            jmc = input("Are you in the James Madison College (yes/no): ")
            jmc = jmc.lower()
            
            if jmc == "yes":
                credit = input("Credits: ")
                credit = credit
                try:
                    credit_int = int(credit)
                except:
                    while credit == credit:
                        print("Invalid input. Try again.")
                        credit = input("Credits: ")
                        try: 
                            credit_int = int(credit)
                            if type(credit_int) is not int:
                                continue
                            
                            
                        except:
                            credit_int = (int(credit))
            
                while credit_int <= 0:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    credit_int = float(credit_int)
                while credit_int % 1 != 0:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    credit_int = float(credit)
                if 0 < credit_int <= 4:
                    cost = INTR_JU_SE_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_JMC + FEE_INTR_PT
                    total_cost = cost + fees
                    if major_cmse == "yes":
                        total_cost = total_cost + FEE_ENG_CMSE_PT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int == 5:
                    cost = INTR_JU_SE_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_JMC + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 6 <= credit_int < 12:
                    cost = INTR_JU_SE_PER * credit_int
                    taxes = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    fees = taxes + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 12 <= credit_int <= 18:
                    cost = INTR_JU_SE_FLT
                    taxes = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    fees = taxes + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int >= 19:
                    cost = INTR_JU_SE_FLT + (INTR_JU_SE_PER * credit_int)
                    taxes = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    fees = taxes + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break    
            else:  
                while True:
                  credit = input("Credits: ")
                  if not credit.isdigit() or int(credit) == 0:
                    print("Invalid input. Try again.")

                  else:
                    credit_int = int(credit)
                    break


                
                
            
                credit_int = credit_int

                while credit_int <= 0:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    credit_int = float(credit_int)
                while credit_int % 1 != 0:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    credit_int = float(credit)
                if 0 < credit_int <= 4:
                    cost = INTR_JU_SE_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":
                        total_cost = total_cost + FEE_ENG_CMSE_PT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int == 5:
                    cost = INTR_JU_SE_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 6 <= credit_int < 12:
                    cost = INTR_JU_SE_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 12 <= credit_int <= 18:
                    cost = INTR_JU_SE_FLT
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int >= 19:
                    cost = INTR_JU_SE_FLT + (INTR_JU_SE_PER * credit_int)
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
        
        
###############################################################################
########################## FRESHMAN CALCULATIONS ##############################
###############################################################################
        
        
    elif level == 'freshman':
        admitted_egr = input("Are you admitted to the " \
                             "College of Engineering (yes/no): ")
        admitted_egr = admitted_egr.lower()
        
        if admitted_egr == "yes":
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            while credit_int % 1 != 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            if 0 < credit_int <= 4:
                cost = INTR_FR_SO_PER * credit_int
                fees = FEE_ENG_CMSE_PT + TAX_ASMSU + TAX_RADIO + FEE_INTR_FT
                total_cost = cost + fees
                if major_cmse == "yes":
                    total_cost = total_cost + FEE_ENG_CMSE_PT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int == 5:
                cost = INTR_FR_SO_PER * credit_int
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO + FEE_INTR_FT
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 6 <= credit_int < 12:
                cost = INTR_FR_SO_PER * credit_int
                tax = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_ENG_CMSE_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 12 <= credit_int <= 18:
                cost = INTR_FR_SO_FLT
                tax = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_ENG_CMSE_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int >= 19:
                cost = INTR_FR_SO_FLT + (INTR_FR_SO_PER * (credit_int - 18))
                tax = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_ENG_CMSE_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
        else: 
            jmc = input("Are you in the James Madison College (yes/no): ")
            jmc = jmc.lower()
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            while credit_int % 1 != 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            if jmc == "yes":
                if 0 < credit_int <= 4:
                    cost = INTR_FR_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_JMC + FEE_INTR_PT
                    total_cost = cost + fees
                    if major_cmse == "yes":
                        total_cost = total_cost + FEE_ENG_CMSE_PT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int == 5:
                    cost = INTR_FR_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_JMC + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 6 <= credit_int < 12:
                    cost = INTR_FR_SO_PER * credit_int
                    taxes = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    fees = taxes + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 12 <= credit_int <= 18:
                    cost = INTR_FR_SO_FLT
                    taxes = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    fees = taxes + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int >= 19:
                    cost = INTR_FR_SO_FLT + (INTR_FR_SO_PER *(credit_int - 18))
                    taxes = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    fees = taxes + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
            else:
                if 0 < credit_int <= 4:
                    cost = INTR_FR_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + FEE_INTR_PT
                    total_cost = cost + fees
                    if major_cmse == "yes":
                        total_cost = total_cost + FEE_ENG_CMSE_PT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int == 5:
                    cost = INTR_FR_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + FEE_INTR_FT
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 6 <= credit_int < 12:
                    cost = INTR_FR_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 12 <= credit_int <= 18:
                    cost = INTR_FR_SO_FLT
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + FEE_INTR_FT
                    total_cost = cost + fees
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int >= 19:
                    cost = INTR_FR_SO_FLT + (INTR_FR_SO_PER *(credit_int - 18))
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break


##############################################################################
########################## SOPHOMORE CALCULATION #############################
##############################################################################
                        
                                 
    elif level == "sophomore":
        admitted_egr = input("Are you admitted to the " \
                             "College of Engineering (yes/no): ")
        admitted_egr = admitted_egr.lower()
        
        if admitted_egr == "yes":
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
        if admitted_egr == "yes":
            if 0 < credit_int <= 4:
                cost = INTR_FR_SO_PER * credit_int
                fees = FEE_ENG_CMSE_PT + TAX_ASMSU + TAX_RADIO + FEE_INTR_PT
                total_cost = cost + fees
                
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int == 5:
                cost = INTR_FR_SO_PER * credit_int
                fees = FEE_ENG_CMSE_FT + TAX_ASMSU + TAX_RADIO + FEE_INTR_FT
                total_cost = cost + fees
                
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 6 <= credit_int < 12:
                cost = INTR_FR_SO_PER * credit_int
                tax = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_ENG_CMSE_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif 12 <= credit_int <= 18:
                cost = INTR_FR_SO_FLT
                tax = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_ENG_CMSE_FT + FEE_INTR_FT + tax
                total_cost = cost + fees
                if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
            elif credit_int >= 19:
                cost = INTR_FR_SO_FLT + (INTR_FR_SO_PER * (credit_int - 18))
                tax = TAX_ASMSU + TAX_RADIO + TAX_NEWS
                fees = FEE_ENG_CMSE_FT + FEE_INTR_FT + tax
                total_cost = cost + fees

                print("Tuition is ${:,.2f}.".format(total_cost)) 
                another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                another_calc = another_calc.lower()
                if another_calc == "yes":
                    resident = input("Resident (yes/no): ")
                    resident = resident.lower()
                    continue
                else:
                    break
        else: 
            jmc = input("Are you in the James Madison College (yes/no): ")
            jmc = jmc.lower()
            credit = input("Credits: ")
            credit = credit
            try:
                credit_int = int(credit)
            except:
                while credit == credit:
                    print("Invalid input. Try again.")
                    credit = input("Credits: ")
                    try: 
                        credit_int = int(credit)
                        if type(credit_int) is int:
                            break
                    except:
                        continue
                else:
                    credit_int = (int(credit))
                credit_int = (int(credit))
            while credit_int <= 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            while credit_int % 1 != 0:
                print("Invalid input. Try again.")
                credit = input("Credits: ")
                credit_int = int(credit)
            if jmc == "yes":
                if 0 < credit_int <= 4:
                    cost = INTR_FR_SO_FLT * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_JMC + FEE_INTR_PT
                    total_cost = cost + fees
                    if major_cmse == "yes":
                        total_cost = total_cost + FEE_ENG_CMSE_PT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int == 5:
                    cost = INTR_FR_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_JMC + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 6 <= credit_int < 12:
                    cost = INTR_FR_SO_PER * credit_int
                    taxes = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    fees = taxes + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 12 <= credit_int <= 18:
                    cost = INTR_FR_SO_FLT
                    taxes = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    fees = taxes + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int >= 19:
                    cost = INTR_FR_SO_FLT + (INTR_FR_SO_PER *(credit_int - 18))
                    taxes = TAX_ASMSU + TAX_RADIO + TAX_NEWS + TAX_JMC
                    fees = taxes + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
            else:
                if 0 < credit_int <= 4:
                    cost = INTR_FR_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + FEE_INTR_PT
                    total_cost = cost + fees
                    if major_cmse == "yes":
                        total_cost = total_cost + FEE_ENG_CMSE_PT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int == 5:
                    cost = INTR_FR_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 6 <= credit_int < 12:
                    cost = INTR_FR_SO_PER * credit_int
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif 12 <= credit_int <= 18:
                    cost = INTR_FR_SO_FLT
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                elif credit_int >= 19:
                    cost = INTR_FR_SO_FLT + (INTR_FR_SO_PER *(credit_int - 18))
                    fees = TAX_ASMSU + TAX_RADIO + TAX_NEWS + FEE_INTR_FT
                    total_cost = cost + fees
                    if major_cmse == "yes":   
                        total_cost = total_cost + FEE_ENG_CMSE_FT
                    print("Tuition is ${:,.2f}.".format(total_cost)) 
                    another_calc = input("Do you want to do another" \
                                     " calculation (yes/no): ") 
                    another_calc = another_calc.lower()
                    if another_calc == "yes":
                        resident = input("Resident (yes/no): ")
                        resident = resident.lower()
                        continue
                    else:
                        break
                
    else:
        print("Invalid input. Try again.")
        continue
