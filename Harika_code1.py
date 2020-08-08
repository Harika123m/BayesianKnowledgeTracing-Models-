## Single value KC Code

# Defintion to find out Probability equation value
def calc(t):
    # Set the default parameters
    p_L=float(0.5)
    p_T=float(0.75)
    p_G=float(0.3)
    p_S=float(0.1)
    prob_value=[]
    prev=0 # Variable to retain old value for calculation
    for i,record in enumerate(t):
        if(i>0):
            a=t[i-1]
            old_stud=a[0]
            old_value=float(prev)

            if(record[0]==old_stud):  ## If the same old student is continuing
                if(record[2]=='1'):  ## If the got the andwer right
                    c=float(old_value*(1-p_S))
                    d=float((1-old_value)*p_G)
                    e=float(c/(c+d))
                    f=float(e+((1-e)*p_T))
                    if(f>0.99):   ## If the student is getting correct continuosly, the Learning probabilty goes to 1 due to 16-bit precision.
                        f=0.99     ## So if increases byond 0.99, set it back to 0.99
                        prev=0.99
                    else:
                        prev = f
                    prob_value.append(f)

                else:  ## If he got the answer wrong
                    c = float(old_value * ( p_S))
                    d = float((1 - old_value) * (1-p_G))
                    e = float(c / (c + d))
                    f=float(e+((1-e)*p_T))
                    if(f>0.99):  ## If the student is getting correct continuosly, the Learning probabilty goes to 1 due to 16-bit precision.
                        f=0.99   ## So if increases byond 0.99, set it back to 0.99
                        prev =0.99
                    else:
                        prev=f
                    prob_value.append(f)

            else:  ## When a new student is encountered, initialize his learning probability to p_L
                prev=p_L
                prob_value.append(p_L)
        else:  ## While index is 0, it can't check previous value, so append it manually
            prev = p_L
            prob_value.append(p_L)

    return prob_value

# Definition to find out Correctness equation value

## Same logic as the function before is applied and then even correctness value is calculated
## (Since it's good that function returns just one array, I've used 2 different functions)
def correq(t):
    p_L = 0.5
    p_T = 0.75
    p_G = 0.3
    p_S = 0.1
    correctness = []
    prev = 0
    for i, record in enumerate(t):
        if (i > 0):
            a = t[i - 1]
            old_stud = a[0]
            old_value = float(prev)

            if (record[0] == old_stud):
                if (record[2] == '1'):
                    c = float(old_value * (1 - p_S))
                    d = float((1 - old_value) * p_G)
                    e = float(c / (c + d))
                    f = float(e + (1 - e) * p_T)
                    if(f>0.99):
                        f=0.99
                        prev=0.99
                    else:
                        prev = f

                    cor=float((f*(1-p_S)+(1-f)*p_G))
                    correctness.append(cor)
                else:
                    c = float(old_value * (p_S))
                    d = float((1 - old_value) * (1 - p_G))
                    e = float(c / (c + d))
                    f = float(e + (1 - e) * p_T)
                    if(f>0.99):
                        f=0.99
                    else:
                        prev = f
                    cor=float((f*(1-p_S)+(1-f)*p_G))
                    correctness.append(cor)
            else:
                prev = p_L
                cor = float((p_L * (1 - p_S) + (1 - p_L) * p_G))
                correctness.append(cor)
        else:

            prev = p_L
            cor = float((p_L * (1 - p_S) + (1 - p_L) * p_G))
            correctness.append(cor)
    return correctness


file=open('data','r') # Open the data from file which is saved on PyCharm folder only
# Create empty arrays to append all the column values so that a list can be formed.
Student_id=[]
Step_id=[]
Correct=[]
kc1=[]
kc2=[]
kc3=[]
kc4=[]
kc5=[]
kc6=[]
kc7=[]
for i,line in enumerate(file):
    word=line.split('\t')
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

res=list(zip(Student_id,Step_id,Correct,kc1,kc2,kc3,kc4,kc5,kc6,kc7))  # Make a list by zippping as columns all the individual arrays

# Create 7 empty arrays to appand the KC respective KC values only if the student had used them
KCone=[]
KCtwo=[]
KCthree=[]
KCfour=[]
KCfive=[]
KCsix=[]
KCseven=[]
for i in res:
    if(i[3]=='1'):
        KCone.append(i)
for i in res:
    if(i[4]=='1'):
        KCtwo.append(i)
for i in res:
    if(i[5]=='1'):
        KCthree.append(i)
for i in res:
    if(i[6]=='1'):
        KCfour.append(i)
for i in res:
    if(i[7]=='1'):
        KCfive.append(i)
for i in res:
    if(i[8]=='1'):
        KCsix.append(i)
for i in res:
    if((i[9]!='0\n') and (i[9]!='KC_21\n')):
        KCseven.append(i)



#### NOTE :
### This program prints only KC models for first(KC1) and last (KC21).
### All KC models can be printed if we uncomment that particular code ( for loop followed by print statement).

## If everything is printed, the console is cluttered. So I gave "print" just for first and last KC so that it's easy to understand.
## Code works fine even if we print all the KC's.


print("The output is displayed for individual KC's only if he has used that particular KC")
print("-------------------------------------------------------------------------------------")

print("For KC1 ")
data1=list(zip(KCone,calc(KCone),correq(KCone))) # Make a list of student data where he used KC1, Probability equation value and Correctness equation value.
for i in data1:
    print(i)
print("--------------------------------------------------------------------------------------")

print("For KC 27")
data2=list(zip(KCtwo,calc(KCtwo),correq(KCtwo)))
# for i in data2:
#     print(i)
print("--------------------------------------------------------------------------------------")

print("For KC 24")
data3=list(zip(KCthree,calc(KCthree),correq(KCthree)))
# for i in data3:
#     print(i)
print("--------------------------------------------------------------------------------------")

print("For KC 14")
data4=list(zip(KCfour,calc(KCfour),correq(KCfour)))
# for i in data4:
#     print(i)
print("--------------------------------------------------------------------------------------")

print("For KC 22")
data5=list(zip(KCfive,calc(KCfive),correq(KCfive)))
# for i in data5:
#     print(i)
print("---------------------------------------------------------------------------------------")

print("For KC 20")
data6=list(zip(KCsix,calc(KCsix),correq(KCsix)))
# for i,j in enumerate(data6):
#     print(i," ",j)
print("---------------------------------------------------------------------------------------")

print("For KC 21")
data7=list(zip(KCseven,calc(KCseven),correq(KCseven)))
for i in data7:
    print(i)

print(" Part one done !!")

