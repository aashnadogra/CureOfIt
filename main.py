bt = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
btq = [0, 0, 0, 0, 0, 0, 0, 10]
pName=[]
pDob=[]
pGender=[]
pContact=[]
pAddress=[]
pDis=[]
pAge=[]
pTreatment=[]
Ap=[]
Apcont=[]

months_30Days="2,4,6,9,11"
months_31Days="1,3,5,7,8,10,12"
while True:
    print('''
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|
|                                                                   |
|                          CUREOFIT HOSPITAL                        |
|                                                                   |
|<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<|
_____________________________________    
Enter 1 For Patient Enquiry
_____________________________________
Enter 2 For Patient Admission
_____________________________________
Enter 3 For Booking An Appointment
_____________________________________
Enter 4 For Doctors Info
_____________________________________
Enter 5 To Access Blood Bank
_____________________________________
Enter 6 For Patient Discharge
_____________________________________
Enter 7 To Exit Program
_____________________________________''')
    user_input=int(input("ENTER HERE:   "))

    if user_input not in range(1,8):
        print("Invalid Input")
        gg=input("Press Enter to returne to Menue")

#Patient admittion



    if user_input==2:
        print("...................PATIENT ADMISSION FORM...................")
        print(".                                                          .")
        print(".        KINDLY FILL ALL THE CREDENTIALS CAREFULL          .")
        print(".                                                          .")
        print("............................................................")
        
        while True:            
            print("Admission for treatment of:")
            print('''
Enter 1 for Cardiology
Enter 2 for Neurology
Enter 3 for Orthopaedict''')
            de_input=int(input("Enter Here:"))
            if de_input==1:
                pTreatment.append("Cardiology")
                break
            elif de_input==2:
                pTreatment.append("Neurology")
                break
            elif de_input==3:
                pTreatment.append("Orthopaedict")
                break
            else:
                print("Invalid Input")
                ss=input("Press Enter to Start again")

        p_name=input("Enter Patient Name: ")
        while True:
            p_age=input("Enter Patient Age: ")
            xy=int(p_age)
            if xy in range(1,200):
                yx=str(xy)
                pAge.append(yx)
                break
            else:
                print("Invalid Input")
        while True:
            p_DOBd,p_DOBm,p_DOBy=input("Enter Patients Date of Birth (dd:mm:yy): ").split(":")
            if int(p_DOBm)<13 and p_DOBm in months_30Days and int(p_DOBd) <=30 or p_DOBm in months_31Days and int(p_DOBd)<= 31:
                a=p_DOBd+":"+p_DOBm+":"+p_DOBy
                pDob.append(a)
                break
            else:
                print("Invalid Input") 
        while True: 
            print('''
Enter 1 For Male
Enter 2 For Female
Enter 3 Other''')
            ginput=int(input("Enter Gender:  "))
            if ginput==1:
                rx="Male"
                pGender.append(rx)
                break
            elif ginput==2:
                xr="Female"
                pGender.append(xr)
                break
            elif ginput==3:
                ro="Other"
                pGender.append(ro)
                break
            else:
                print("Invalid Input")
                ii=input("Press Enter to Retrne")

        while True:
            p_contact_no=input("Enter Patients Contact no: ")
            if len(p_contact_no)==10:
                pContact.append(p_contact_no)
                break
            else:
                print("Enter a Valid Number ")
        p_Address=input("Enter Patients Address: ")
       
        pName.append(p_name)
       
        pAddress.append(p_Address)
       
        pDis.append("In Hospital")
       
        print("...........................THE FORM IS COMPLETE..............................")
        ww=input("PRESS ENTER TO RETURN TO MENUE")    
    #patient enquiry
    
    if user_input==1:
        while True:
            print("..............................PATIENT ENQUIRY................................")
            print("                                                                             ")
            print("Enter The Registered Phone Number:> ")
            print("Enter 1 to return to Menue")
            iq_patient_ph_no=input("Enter Here:  ")
            koi=int(iq_patient_ph_no)
            print("                                                                             ")
            print("                                                                             ")
            if koi==1:
                break
            else:
                if iq_patient_ph_no in pContact:
                    er=pContact.index(iq_patient_ph_no)
                    print("________________________________________________________________________")
                    print("Patient Name       -    "+ pName[er])
                    print("________________________________________________________________________")
                    print("Patient DOB        -    "+ pDob[er])
                    print("________________________________________________________________________")
                    print("Patient Gender     -    "+ pGender[er])
                    print("________________________________________________________________________")
                    print("Patient Phone NO.  -    "+ pContact[er])
                    print("________________________________________________________________________")
                    print("Patient Address    -    "+ pAddress[er])
                    print("________________________________________________________________________")
                    print("Patient Age        -    "+ pAge[er])
                    print("________________________________________________________________________")
                    print("Under Going Treatment of: "+ pTreatment[er])
                    print("________________________________________________________________________")
                    print("Patient Status     -      "+pDis[er])
                    print("________________________________________________________________________")
                    op=input("Press Enter to Return to menue")
                    break
                elif iq_patient_ph_no not in pContact:
                    if len(iq_patient_ph_no)!=10:
                        print("Invalid Number")
                        orrr=input("Press Enter to Return")
                    else:
                        print("No Patient is registered by this number")
                        uu=input("Press Enter to Return to Menue:")
                        break
                        
                elif len(iq_patient_ph_no)!=10:
                    print("Invalid Number")

        

#Blood Donation


    if user_input==5:
        while True:
            print("""
Enter 1: To make a Donation
Enter 2: To make a Request
Enter 3: To check the Blood Stock
Enter 4: To Return to Menue""")
            x1 = int(input("Make a choice: "))
            if x1 == 1:
                print(">>BLOOD DONATION FORM:")
                print('''Are you 18 years or above and consent to donate Blood?  
Enter 1 For Yes 
Enter 2 For NO''')
                a1 = input("Enter Here")
                print('''Have you donated Blood in past 3 months?  
Enter 1 For Yes
Enter 2 For No''')
                b1 = int(input("Enter Here")) 
                print('''Are you on any prescribed medication?  
Enter 1 For Yes
Enter 2 For No''')
                c1 = int(input("Enter Here"))
                print('''Have you consumed alcohol in past 3 days?  
Enter 1 For Yes
Enter 2 For No ''')
                d1 = int(input("Enter Here"))

                if int(a1) == 1 and b1 == 2 and c1 == 2 and d1 == 2:
                    print("You are eligible to Donate Your Blood\n")
                    while True:
                        tp = input("Please enter your Blood type: \n").upper()
                        if tp in bt:
                            idx = int(bt.index(tp))
                            btq[idx] += 1
                            print("Please visit the donation counter\n \n")
                            break
                        else:
                            print("Please Enter a valid Blood type")
                else:
                    print("Thankyou, but you are not eligible to Donate your Blood\n \n")
                rr=input("PRESS ENTER TO RETURN TO MENUE")
            if x1 == 2:
                print(">>BLOOD REQUEST:\n\n")
                nu = int(input("Required Amount of Blood in units? "))
                while True:
                    rt = input('''Please Enter Blood type: 
[A+,A-,B+,B-,O+,O-,AB+,AB-]''').upper()
                    if rt in bt:
                        idx = int(bt.index(rt))
                        if btq[idx] >= nu:
                            btq[idx] -= nu
                            print(f"{nu} units available, please collect from withdrawal window.\n")
                        else:
                            print(f"{nu} units of {rt} blood type not available\n")
                        break
                    else:
                        print("Please enter a valid Blood type ")
        

            if x1 == 3:
                print(">>BLOOD STOCK")
                print("[A+,A-,B+,B-,O+,O-,AB+,AB-] Blood Types")
                bst = input("Enter Blood type to check particularly or 'all' to check all stock:  ").upper()
                while True:
                    if bst in bt:
                        indx = bt.index(bst)
                        print(f"{btq[indx]} units available of {bst} blood type.")
                        break
                    elif bst == "ALL":
                        for i in range(8):
                            print(f"{btq[i]} units of blood avialable of {bt[i]} type.")
                        break
                    else:
                        print("please enter a valid input")
                        rrrrr=input("PRESS ENTER TO RETURN TO MENUE")     
            
            if x1==4:
                break


    #DOCTOR INFO

    if user_input==4:

        print("| Enter 1 for Cardiologist Specialist |")
        print("| Enter 2 for Neurologist Specialist |")
        print("| Enter 3 for Orthopedic Specialist |")
        y=int(input("Want Details of doctor of which Specialisation:"))
        if y == 1:
            print("| Enter 1 for Dr. Pravesh Aggarwal |")
            print("| Enter 2 for Dr. Sarvesh Sharma |")
            print("| Enter 3 for Dr. Surbhi Aggarwal |")
            z=int(input())
            if z==1:
                print("| Doctor Name : Dr. Pravesh Aggarwal |")
                print('''| Qualifications: |
                1) MBBS - Christian Medical College, Ludhiana 
                2) MD - General Medicine - PGIMER, Chandigarh
                3) DM - Cardiology - All India Institute of Medical Sciences, Delhi
                4) Specialised in Cardiothoracic and Vascular Surgery
                5) 30 years experience
                6) Senior Consultant & Chief Interventional Cardiologist 
                ''')
                dx=input("Press Enter to Continue")
            elif z==2:
                print("| Doctor Name : Dr. Sarvesh Sharma |")
                print('''| Qualification: |
                1) MBBS - MGM - 1975
                2)MD - General Medicine - Pavlov First Medical University St Petersberg, Russia
                3) Specialised in Vascular Surgery Branch of Cardiology
                4) Diploma in Cardiology - Metro Heart Institute, IGNOU
                5) 28 years experience 
                6) Vice head of Cardiology Department''')
                dx=input("Press Enter to Continue")
            elif z==3:
                print("| Doctor Name : Dr. Surbhi Aggarwal |")
                print('''| Qualifications: |
                1) MBBS - GMC Haldwani
                2) Specialised in Interventinoal surgery
                3) PGDCC - DHLI 
                4) 10 years of experience
                5) Awarded for exceptional work in the field of Interventional Cardiology''')
                dx=input("Press Enter to Continue")
        elif y ==2:
            print("| Enter 1 for Dr. Palak Verma |")
            print("| Enter 2 for Dr. Ajay Singh |")
            print("| Enter 3 for Dr. Dvivedi Singh |")
            x = int(input())
            if x == 1:
                print("| Doctor Name : Dr. Palak Verma |")
                print('''| Qualifications: | 
                1) MS/MBBS - General Medicine - Gandhi Medical College, Bhopal
                2) Specialised in Cerebrovascular and Skull Base Surgery 
                3) DNB (Neurology) - Sir Gangaram Hospital, Delhi
                4) Member of Indian Academy of Neurology, Indian Epilepsy Society and Indian Medical Association
                5) 20 years of Experience
                6) Senior Consultant Neurologist
                7) Successfull surgeries till now''')
                dx=input("Press Enter to Continue")

            elif x == 2:
                print("Doctor Name : Dr. Ajay Singh")
                print('''Qualifications:
                1) MBBS - GSVM Medical College, Kanpur
                2) MD- Medicine - GSVM Medical College, Kanpur
                3)DM- Neurology - DR RML Hospital, New Delhi
                4)Specialised in Neuro-Trauma and Neurological Critical Care branch of Neurology
                5) 21 years of Experience''')
                dx=input("Press Enter to Continue")

            elif x==3:
                print("| Doctor Name : Dr. Dvivedi Singh |")
                print('''| Qualifications: |
                1) Msc. Developmental Neuropsychology (U.K) - Essex Univ. (UK)
                2) Specialised in Neuro-Oncology and Interventional branch of Neurology
                3) PhD. Neuropsychology - Delhi University
                4) Chartered Member of British Psychological Society
                5) 10 years of Experience''')
                dx=input("Press Enter to Continue")
        elif y==3:
            print("| Enter 1 for Dr. Rahul Yadav |")
            print("| Enter 2 for Dr. Mehak Singh |")
            print("| Enter 3 for Dr. Hasrshita Mohan |")
            x=int(input())
            if x==1:
                print("| Doctor Name : Dr. Rahul Yadav |")
                print('''| Qualifications: |
                1) MBBS - AIIMS, New Delhi
                2) MS - AIIMS, New Delhi
                3) FIMSA - International Medical Sciences Academy
                4) Specialised in primary total Knee and Hip Arthropalsty
                5) 30 years of Experience
                6) Senior consultant
                ''')
                dx=input("Press Enter to Continue")
            elif x==2:
                print("| Doctor Name : Dr. Mehak Singh |")
                print('''| Qualifications: |
                1) MBBS - AIIMS ,Rajkot
                2) MS Ortho - AIIMS
                3) Diploma in Tissue Banking - NUH, Singapore
                4) Specialised in Computer navigation Assisted Joint replacement
                5) Former key member of the Bone Bank at AIIMS.
                6) 20 years of experience.''')
                dx=input("Press Enter to Continue")
            elif x==3:
                print("| Doctor Name : Dr. Harshita Mohan |")
                print('''| Qualifications: |
                1) MBBS – SNMC, Bagalkot, Karnataka.
                2) MS Orthopaedics - All India Institute of Medical Sciences,New Delhi
                3)  Specialised in Arthroplasty and Sports Surgery
                4) Senior Research Fellow, AIIMS, New Delhi.
                5) 17 years of experience''')
                dx=input("Press Enter to Continue")

    #patient discharge


    if user_input==6:
        dis_patient_phNO=input("Enter Registered Phone Number:> ")
        xo=pContact.index(dis_patient_phNO)
        yt=input("Enter Ok to confirm Patient Discharge:  ")
        if yt =="ok":
            pDis[xo]="Discharged"
        else:
            pass

           
    





    if user_input==3:

        a=input("Book your appointment")
        print(a)
        print("| Enter 1 if you have Cardio related problem |")
        print("| Enter 2 if you have Neuro related problem |")
        print("| Enter 3 if you have Ortho relted problem |")
        b=int(input())
        if b==1:
            print("You have selected cardio related problem")
            print("Availability timings of all the doctors are:")
            print("1. Dr. Pravesh Aggarwal -> 10:00 AM to 01:00 PM")
            print("2. Dr. Sarvesh Sharma -> 03:00 PM to 06:00 PM")
            print("3. Dr. Surbhi Aggarwal -> 09:00 PM to 12:00 AM")
            print("Enter number accordingly to book your appointment with doctor")
            c=int(input())
            if c==1:
                print("You have selected Dr. Pravesh Aggarwal")
                r1=input("Enter your name: ")
                r2=int(input("Enter your age: "))
                r3=input("Enter your gender (M/F): ")
                while True:
                    r4=input("Enter your phone number: ")
                    if len(r4)==10:
                        Apcont.append(r4)
                        break
                    else:
                        print("Enter a Valid Number ")
                while True:
                    r5_d,r5_m,r5_y=input("Enter date of appointment (dd:mm:yy): ").split(':')
                    if int(r5_m)<13 and r5_m in months_30Days and int(r5_d)<=30 or r5_m in months_31Days and int(r5_d)<= 31:
                        ag=r5_d+":"+r5_m+":"+r5_y
                        Ap.append(ag)
                        break
                    else:
                        print("Invalid Input") 
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Your appointment has been registered, Please be there on time.")
            elif c==2:
                print("You have selected Dr. Sarvesh Sharma")
                p1=input("Enter your name: ")
                p2=int(input("Enter your age: "))
                p3=input("Enter your gender (M/F): ")
                while True:
                    p4=input("Enter your phone number: ")
                    if len(p4)==10:
                        Apcont.append(p4)
                        break
                    else:
                        print("Enter a Valid Number ")
                while True:
                    p5_d,p5_m,p5_y=input("Enter date of appointment (dd:mm:yy): ").split(':')
                    if int(p5_m)<13 and p5_m in months_30Days and int(p5_d)<=30 or p5_m in months_31Days and int(p5_d)<= 31:
                        ag=p5_d+":"+p5_m+":"+p5_y
                        Ap.append(ag)
                        break
                    else:
                        print("Invalid Input") 
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Your appointment has been registered. Please be there on time!")
            elif c==3:
                print("You have selected Dr. Surbhi Aggarwal")
                q1=input("Enter your name: ")
                q2=int(input("Enter your age: "))
                q3=input("Enter your gender (M/F): ")
                while True:
                    q4=input("Enter your phone number: ")
                    if len(q4)==10:
                        Apcont.append(q4)
                        break
                    else:
                        print("Enter a Valid Number ")
                while True:
                    q5_d,q5_m,q5_y=input("Enter date of appointment (dd:mm:yy): ").split(':')
                    if int(q5_m)<13 and q5_m in months_30Days and int(q5_d)<=30 or q5_m in months_31Days and int(q5_d)<= 31:
                        ag=q5_d+":"+q5_m+":"+q5_y
                        Ap.append(ag)
                        break
                    else:
                        print("Invalid Input") 
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Your appointment has been registered. Please be there on time!")
        elif b==2:
            print("You have selected Neuro related issues")
            print("Availability timings of all the doctors are:")
            print("1. Dr. Palak Verma -> 10:00 AM to 01:00 PM")
            print("2. Dr. Ajay Singh -> 03:00 PM to 06:00 PM")
            print("3. Dr. Deepanshi Singh -> 09:00 PM to 12:00 AM ")
            print("Enter number accordingly to book your appointment with doctor")
            d=int(input())
            if d==1:
                print("You have selected Dr. Palak Verma")
                s1=input("Enter your name: ")
                s2=int(input("Enter your age: "))
                s3=input("Enter your gender (M/F): ")
                while True:
                    s4=input("Enter your phone number: ")
                    if len(s4)==10:
                        Apcont.append(s4)
                        break
                    else:
                        print("Enter a Valid Number ")
                while True:
                    s5_d,s5_m,s5_y=input("Enter date of appointment (dd:mm:yy): ").split(':')
                    if int(s5_m)<13 and s5_m in months_30Days and int(s5_d)<=30 or s5_m in months_31Days and int(s5_d)<= 31:
                        ag=s5_d+":"+s5_m+":"+s5_y
                        Ap.append(ag)
                        break
                    else:
                        print("Invalid Input") 
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Your appointment has been registered. Please be there on time!")
            elif d==2:
                print("You have slected Dr. Ajay Singh")
                t1=input("Enter your name: ")
                t2=int(input("Enter your age: "))
                t3=input("Enter your gender (M/F): ")
                while True:
                    t4=input("Enter your phone number: ")
                    if len(t4)==10:
                        Apcont.append(t4)
                        break
                    else:
                        print("Enter a Valid Number ")
                while True:
                    t5_d,t5_m,t5_y=input("Enter date of appointment (dd:mm:yy): ").split(':')
                    if int(t5_m)<13 and t5_m in months_30Days and int(t5_d)<=30 or t5_m in months_31Days and int(t5_d)<= 31:
                        ag=t5_d+":"+t5_m+":"+t5_y
                        Ap.append(ag)
                        break
                    else:
                        print("Invalid Input") 
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Your appointment has been registered. Please be there on time!")
            elif d==3:
                print("You have selected Dr. Deepanshi Singh")
                u1=input("Enter your name: ")
                u2=int(input("Enter your age: "))
                u3=input("Enter your gender (M/F): ")
                while True:
                    u4=input("Enter your phone number: ")
                    if len(u4)==10:
                        Apcont.append(u4)
                        break
                    else:
                        print("Enter a Valid Number ")
                while True:
                    u5_d,u5_m,u5_y=input("Enter date of appointment (dd:mm:yy): ").split(':')
                    if int(u5_m)<13 and u5_m in months_30Days and int(u5_d)<=30 or u5_m in months_31Days and int(u5_d)<= 31:
                        ag=u5_d+":"+u5_m+":"+u5_y
                        Ap.append(ag)
                        break
                    else:
                        print("Invalid Input")
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Your appointment has been registered. Please be there on time!")
        elif b==3:
            print("You have selected Ortho related issues")
            print("Availability timings of all the doctors are:")
            print(" 1. Dr. Rahul Yadav -> 10:00 AM to 01:00 PM")
            print("2. Dr. Mehak Singh -> 03:00 PM to 06:00 PM")
            print("3. Dr. Harshita Mohan -> 09:00 PM to 12:00 AM")
            print("Enter number accordingly to book your appointment with doctor")
            e=int(input())
            if e==1:
                print("You have selected Dr. Rahul Yadav")
                v1=input("Enter your name: ")
                v2=int(input("Enter your age: "))
                v3=input("Enter your gender (M/F): ")
                while True:
                    v4=input("Enter your phone number: ")
                    if len(v4)==10:
                        Apcont.append(v4)
                        break
                    else:
                        print("Enter a Valid Number ")
                while True:
                    v5_d,v5_m,v5_y=input("Enter date of appointment (dd:mm:yy): ").split(':')
                    if int(v5_m)<13 and v5_m in months_30Days and int(v5_d)<=30 or v5_m in months_31Days and int(v5_d)<= 31:
                        ag=v5_d+":"+v5_m+":"+v5_y
                        Ap.append(ag)
                        break
                    else:
                        print("Invalid Input") 
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Your appointment has been registered. Please be there on time!")
            elif e==2:
                print("You have selected Dr. Mehak Singh")
                w1=input("Enter your name: ")
                w2=int(input("Enter your age: "))
                w3=input("Enter your gender (M/F): ")
                while True:
                    w4=input("Enter your phone number: ")
                    if len(w4)==10:
                        Apcont.append(w4)
                        break
                    else:
                        print("Enter a Valid Number ")
                while True:
                    w5_d,w5_m,w5_y=input("Enter date of appointment (dd:mm:yy): ").split(':')
                    if int(w5_m)<13 and w5_m in months_30Days and int(w5_d)<=30 or w5_m in months_31Days and int(w5_d)<= 31:
                        ag=w5_d+":"+w5_m+":"+w5_y
                        Ap.append(ag)
                        break
                    else:
                        print("Invalid Input") 
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Your appointment has been registered. Please be there on time!")
            elif e==3:
                print("You have selected Dr. Harshita Mohan")
                x1=input("Enter your name: ")
                x2=int(input("Enter your age: "))
                x3=input("Enter your gender (M/F): ")
                while True:
                    x4=input("Enter your phone number: ")
                    if len(x4)==10:
                        Apcont.append(x4)
                        break
                    else:
                        print("Enter a Valid Number ")
                while True:
                    x5_d,x5_m,x5_y=input("Enter date of appointment (dd:mm:yy): ").split(':')
                    if int(x5_m)<13 and x5_m in months_30Days and int(x5_d)<=30 or x5_m in months_31Days and int(x5_d)<= 31:
                        ag=x5_d+":"+x5_m+":"+x5_y
                        Ap.append(ag)
                        break
                    else:
                        print("Invalid Input") 
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("Your appointment has been registered. Please be there on time!")


    if user_input==7:
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<EXITING PROGRAM>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            break