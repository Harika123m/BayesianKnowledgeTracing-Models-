## Part 2 : Multi KC Model

# Set the default parameters

p_L = float(0.5)
p_T = float(0.75)
p_G = float(0.3)
p_S = float(0.1)

# Define a fuction to calculate learning and correctness probabilities for all KC's
def calc(t):
    # Initialize empty arrays to append all the calculations
    prob1 = []
    prob2 = []
    prob3 = []
    prob4 = []
    prob5 = []
    prob6 = []
    prob7 = []
    corr1 = []
    corr2 = []
    corr3 = []
    corr4 = []
    corr5 = []
    corr6 = []
    corr7 = []

    # create an array to retain old values for calculations
    # Just the first values are given so that from second iteration, these values are automatically updated through the code.

    prev = [[-1, 'stu1'], [-1, 'stu1'], [-1, 'stu1'], [-1, 'stu1'], [-1, 'stu1'], [-1, 'stu1'], [-1, 'stu1']]
    for j in range(0, 7): # Since there are 7 KCs

        for i, record in enumerate(t): # For each record from the data..

            correct = record[2] # Variable to store if the student has done the step right or wrong
            current_stud_name = record[0]  # Variable to store student name

            current_K_C = record[j + 3]  # The KC values started after column 3 in the data set
            if (i > 0):  # While index is greater than 0 ( As previous values cannot be calculated for the first row

                if ((current_K_C == '1') or (current_K_C == '1\n')): # If the KC has been used
                    old_value = prev[j][0]   # Obtain old values for calculations
                    old_stud = prev[j][1]
                    if (current_stud_name == old_stud):     # If the same student is continuing
                        if (correct == '1'):   # If the student has done the step correctly
                            c = float(old_value * (1 - p_S))
                            d = float((1 - old_value) * p_G)
                            e = float(c / (c + d))
                            f = float(e + ((1 - e) * p_T))

                            if (f > 0.99): # Due to continuously doing correct, the probability may reach 1.0 ( cummulaitve effect).
                                f = 0.99   # Since we do not want probability to be equal or grater than 1.0, in that case we replace it with 0.99
                                prev[j][0] = 0.99
                                prev[j][1] = current_stud_name
                            else:
                                prev[j][0] = f
                                prev[j][1] = current_stud_name
                            if (old_value == -1):
                                f = p_L
                                prev[j][0] = f

                            exec("%s%d.append(%f)" % ('prob', (j + 1), f)) # Append Learning probability
                            exec("%s%d.append(%f)" % ('corr', (j + 1), ((f*(1-p_S))+((1-f)*p_G))))  # Append correctness probability



                        else:   # If the student has done the step wrong
                            c = float(old_value * (p_S))
                            d = float((1 - old_value) * (1 - p_G))
                            e = float(c / (c + d))
                            f = float(e + ((1 - e) * p_T))
                            if (f > 0.99):
                                f = 0.99
                                prev[j][0] = f
                                prev[j][1] = current_stud_name
                            else:
                                prev[j][0] = f
                                prev[j][1] = current_stud_name
                            # prob1.append(f)
                            exec("%s%d.append(%f)" % ('prob', (j + 1), f)) # Append Learning probability
                            exec("%s%d.append(%f)" % ('corr', (j + 1),((f*(1-p_S))+((1-f)*p_G)))) # Append correctness probability

                    else:   ## If a new student name is encountered, enter the p_L (initial value)
                        prev[j][0] = p_L
                        prev[j][1] = current_stud_name
                        exec("%s%d.append(%f)" % ('prob', (j + 1), p_L)) # Append Learning probability
                        exec("%s%d.append(%f)" % ('corr', (j + 1), ((p_L*(1-p_S))+((1-p_L)*p_G))))  # Append correctness probability


                else:
                    exec("%s%d.append(%s)" % ('prob', (j + 1), "'NA'")) # Append Learning probability
                    exec("%s%d.append(%s)" % ('corr', (j + 1), "'NA'"))  # Append correctness probability


            else:  # While index is zero that is, for the first iteration, check the relevance of the KC
                if (current_K_C == '0' or current_K_C=='0\n'):
                    exec("%s%d.append(%s)" % ('prob', (j + 1), "'NA'")) # Append Learning probability
                    exec("%s%d.append(%s)" % ('corr', (j + 1), "'NA'"))  # Append correctness probability

                else:
                    exec("%s%d.append(%f)" % ('prob', (j + 1), p_L))  # Append Learning probability
                    prev[j][0]=p_L
                    exec("%s%d.append(%f)" % ('corr', (j + 1), ((p_L*(1-p_S))+((1-p_L)*p_G))))  # Append correctness probability


    result_of_seven_kcs = list(zip(prob1, prob2, prob3, prob4, prob5, prob6, prob7,corr1,corr2,corr3,corr4,corr5,corr6,corr7))
    return result_of_seven_kcs


file = open('data', 'r')  # Open the data from file which is saved on PyCharm folder only
# Create empty arrays to append all the column values so that a list can be formed.
Student_id = []
Step_id = []
Correct = []
kc1 = []
kc2 = []
kc3 = []
kc4 = []
kc5 = []
kc6 = []
kc7 = []
for i, line in enumerate(file):
    word = line.split('\t')
    Student_id.append(word[0])
    Step_id.append(word[1])
    Correct.append(word[2])
    kc1.append(word[3])
    kc2.append(word[4])
    kc3.append(word[5])
    kc4.append(word[6])
    kc5.append(word[7])
    kc6.append(word[8])
    kc7.append(word[9])


# Make a list so that performing operations on data is easy
res = list(zip(Student_id, Step_id, Correct, kc1, kc2, kc3, kc4, kc5, kc6, kc7))
# Send the list data to the function calc
data = calc(res)

# Create empty array so that learning probability value can be appended for Multi KCs
P_present = []
# The relevance factors are given as per frequency . The KC which is repeated more frequently has high relevance factor
# By getting length of individual KC where it has been used, the relevance factors are assigned
r1 = 0.3
r2 = 0.8
r3 = 0.5
r4 = 0.4
r5 = 0.6
r6 = 0.9
r7 = 0.7

## Perform the calculation :
# if there is a learning probability for a KC, multiply it with the relevace factor of that KC.
## Formula for correctnes :
# P(L’) = ∑ Ri * P(Li) if P(Li)  ≠  N / A
# P(C) = [P(L’) *(1 - P(S))] + [(1 - P(L’)) *P(G)]
# where R is relevance factor


for i in data:
    sum123 = 0
    count_of_KC = 0
    if (i[0] != "NA"):
        a = r1 * i[0]
        sum123 += a
    if (i[1] != "NA"):
        b = r2 * i[1]
        sum123 += b
    if (i[2] != "NA"):
        c = r3 * i[2]
        sum123 += c
    if (i[3] != "NA"):
        d = r4 * i[3]
        sum123 += d
    if (i[4] != "NA"):
        e = r5 * i[4]
        sum123 += e
    if (i[5] != "NA"):
        f = r6 * i[5]
        sum123 += f
    if (i[6] != "NA"):
        g = r7 * i[6]
        sum123 += g
    P_present.append(sum123)

# Create a list adding the original data, learning and correctness values and new probabilty for multi KC step
final_one = list(zip(res, data, P_present))

# Create a new array to append the values of Correctness probabilty which is calculated using correctness equation
Multi_correct = []

for i in P_present:
    if (i > 1):
        i = 0.99
    a = i * (1 - p_S)
    b = (1 - i) * p_G
    c = a + b
    if (c > 1):
        d = 0.99
    else:
        d = c
    Multi_correct.append(d)

## Final list is made which consists of
   ## 1. dataset records
   ## 2. 7 sets of Learning and Correctness probability values
   ## 3. The Multi KC learning probability
   ## 4. The correctness probabilty values.



final_two=list(zip(final_one,Multi_correct))


 # NOTE :::
 #    Only the first 1000 records is printed so that the output is eligible.
 #    We can print all the records also


for i,j in enumerate(final_two):
    if(i<1000):
        print(j)


print("---------------------------------------------------------------------------------------------------------")


print("Visualization")
vis_KC1=[]
vis_KC2=[]
vis_KC3=[]
vis_KC4=[]
vis_KC5=[]
vis_KC6=[]
vis_KC7=[]

## Append all correctness values

for i in data:
    vis_KC1.append(i[7])
    vis_KC2.append(i[8])
    vis_KC3.append(i[9])
    vis_KC4.append(i[10])
    vis_KC5.append(i[11])
    vis_KC6.append(i[12])
    vis_KC7.append(i[13])


##  KC1 to comapre with Multi KC
## NOTE : Any KC can be compared against Multi KC.
## Here only per KC model of KC1 is compared against Multi KC
visualize=list(zip(Correct,vis_KC1,Multi_correct))
KC_one_visualize=[]
## Ignore the rows where KC1 is not being used
for i in visualize:
    if(i[1]!="NA"):
        KC_one_visualize.append(i)

#3 Calculate the error.
# To compare the performance of Single KC with multiple KC, the error values of correctness probability are compared.
#
# Error value is  √(actual-observed)2
#
# We square root the squared value to avoid negative values in the analysis.
# The KC1 error values and Multi KC error values are compared and the graph below is it’s result.
# Observing the graph, it can be traced that Multi KC performed well than Single KC.


error_KC1=[]
error_Multi_KC=[]
import math
for i in KC_one_visualize:
    if(i[0]=='1'):
        a=float(i[1])
        b=float(i[2])
        c=(1-a)*(1-a)
        d=(1-b)*(1-b)
        error_KC1.append(math.sqrt(c))
        error_Multi_KC.append(math.sqrt(d))
    else:
        a=float(i[1])
        b=float(i[2])
        c=(0-a)*(0-a)
        d=(0-b)*(0-b)
        error_KC1.append(math.sqrt(c))
        error_Multi_KC.append(math.sqrt(d))

## Copy the following values (output) into excel for visualization

for i in error_KC1:
    print(i)
for i in error_Multi_KC:
    print(i)
