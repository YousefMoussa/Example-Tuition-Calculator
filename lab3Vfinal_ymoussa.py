I_deposit = 2000
M_deposit = 200
RESP_A_interest = 0.0625
Arts_tuition = 5550
Science_tuition = 6150
Engg_tuition = 6550
Tuition_increase = 0.07
Art_start = 1
Science_start = 1
Engg_start = 1
## Saving Calculation
# This section initializes an array naming it 'Savings_balance' with the initial deposit as its
# starting number. It then uses the formula for the RESP interest to calculate the amount in the 
# RESP account for every month over the 18 years. Finally, it prints the last number in 'Savings_balance'
# which is the total amount left in the account saved after 18 years.
Savings_balance = np.array([I_deposit])
for i in range(215):
    Savings_balance = np.append(Savings_balance, Savings_balance[-1] + (Savings_balance[-1]*(RESP_A_interest/12)) + M_deposit)
print("The savings amount is $%.2f"% Savings_balance[-1])

## Tuition Calculation
# This section initializes an array for each discipline with their starting tuitions as the start of each array.
# It then uses the tuition annual increase formula to calculate the tuition for every year for a span of 22 years.
# It then sums the tuition cost for the last for years for each discipline by summing each array's last four numbers,
# then printing this amount as the predicted total education cost of that program over four years.
Art_t = np.array([Arts_tuition])
Science_t = np.array([Science_tuition])
Engg_t = np.array([Engg_tuition])
for i in range(21):
    Art_t = np.append(Art_t, Art_t[-1] + Art_t[-1]*Tuition_increase)
    Science_t = np.append(Science_t, Science_t[-1] + Science_t[-1]*Tuition_increase)
    Engg_t = np.append(Engg_t, Engg_t[-1] + Engg_t[-1]*Tuition_increase)
Art_total = np.sum(Art_t[-4:])
Science_total = np.sum(Science_t[-4:])
Engg_total = np.sum(Engg_t[-4:])
print("The cost of the arts program is $%.2f"% Art_total)
print("The cost of the science program is $%.2f"% Science_total)
print("The cost of the engg program is $%.2f"% Engg_total)

## Plot
# Here A plot of the tuition amount every year for 18 years is created. As well as, a line representing the total program cost
# for each discipline over four years is established. The x-axis and y-axis are then adjusted for their desired outline with labels 
# created for both. Finally, a title is created for the graph and a legend established, the graph is then shown.
plt.plot(range(19), np.append(Savings_balance[::12], Savings_balance[-1]), label = 'Saving Balance')
plt.axhline(Art_total, color = 'orange', label = 'Arts')
plt.axhline(Science_total, color = 'green', label = 'Science')
plt.axhline(Engg_total, color = 'red', label = 'Engineering')
plt.xlim([0,18])
plt.xticks(range(19))
plt.ylim([0,1e5])
plt.xlabel("Years")
plt.ylabel("Amount $")
plt.legend()
plt.title("Savings vs Tuition")
plt.show()

## Optimization
# Here the user first is asked for a number input relative to the program as which they wish to enter. If the inputted number is not 
# one that belongs to a discipline an error code is printed. Then the amount saved relative to the initial investment plan is 
# compared to the cost of entering that discipline for a four year degree. If there is enough saved the program prints that there 
# is enough saved, if not the program will say that there is not enough saved. Then starting at one dollar and using a while loop 
# the system calculated the lowest monthly contribution to save the amount of money necessary for that program. The loop will start 
# at a dollar a month contribution and add one dollar to the contribution and restart the calculations for each month over eighteen 
# years until the amount sufficient to cover the cost of the program is the final savings amount. Then a statement is printed 
# indicating the minimum monthly contribution required.
print('Version 2 - Solution')
program = int(input('Enter a program 1.Arts, 2.Science, 3. Engineering :'))
if program == 1:
    Cost = Art_total
    if Art_total <= Savings_balance[-1]:
        print("Congratulation!!! You have saved enough for the arts program")
    else: 
        print("Unfortunately!!! You do not have enough saved for the arts program")

if program == 2:
    Cost = Science_total
    if Science_total <= Savings_balance[-1]:
        print("Congratulation!!! You have saved enough for the science program")
    else: 
        print("Unfortunately!!! You do not have enough saved for the science program")

if program == 3:
    Cost = Engg_total
    if Engg_total <= Savings_balance[-1]:
        print("Congratulation!!! You have saved enough for the engineering program")
    else: 
        print("Unfortunately!!! You do not have enough saved for the engineering program")
    
P_save = np.array([I_deposit])
Initial_invest = 1
while Cost > P_save[-1]:
    P_save = np.array([I_deposit])
    for i in range(215):
        P_save = np.append(P_save, P_save[-1] + (P_save[-1]*(RESP_A_interest/12)) + Initial_invest)
    Initial_invest = Initial_invest + 1
Final_invest = Initial_invest - 1
print("The optimal monthly contribution amount is $%.f" %Final_invest)

