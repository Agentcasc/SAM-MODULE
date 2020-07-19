COVID_SYMP = ['FEVER','CHILLS','COUGH','SHORTNESS OF BREATH','BREATHING DIFFICULTY'
,'FATIGUE','MUSCLE' ,'BODY ACHES','HEADACHE','SORE THROAT','LOSS OF TASTE','LOSS OF SMELL','CONGESTION','NAUSEA' ,'VOMITING',]

#print(','.join(COVID_SYMP))

questionlist = ['have you had any chills lately?','have you had a fever in the past week?','Have you been dry coughing this week?','Have you been experiencing shortness of breath?',
'Have you been experiencing fatigue?','Have you had muscle or body aches this week?','How often have you had headaches this week?','Have you had a sore throat?','Are you experiencing nausea?' 
]
INPUTVALUES = {
 
'yes' : 5,
'no' : 0,  
}

OVSCORE = 0

SCOREADDON = []

for i in range(len(questionlist)):
    print(questionlist[i])
    VALUEINPUT = input()
    SCOREADDON.append(INPUTVALUES[VALUEINPUT])
    

 #ENDSCORE MODULE   
for ele in range(0, len(SCOREADDON)): 
    OVSCORE = OVSCORE + SCOREADDON[ele] 
if OVSCORE > 30:
    print('Our Short Assessment Module system predicts that you have been contracted with COVID-19')

else: 
    print('our system does not think you have covid, but please feel free to access our testing site database and information')
