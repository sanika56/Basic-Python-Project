#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Hospital Room Charge for admitted patient Using Multiple Level inheritance with elif statement.


# In[6]:


p_id = int(input("Please Enter Patient ID : "))
p_nm = input("Please Enter Patient Name : ")
p_add = input("Please Enter Patient Address : ")
p_cn = int(input("Please Enter Patient Contact or Mobile Number : "))
p_days = int(input("\nEnter How Many Days Patient Addmited: "))
print("\nPlease Enter Patient Ward Section : \n1.Generalward \n2.Sharingward \n3.Specialward \n4.ICUward")
choice = int(input("\nEnter The Choice:"))

class Generalward():   
    def choice1(self):
        
        gnwd = 700 
        print("General Ward charges is per day :" , gnwd) 
        rchkup = 500 
        print("Routine check up cost is per day :", rchkup) 
        gnchkup = 800 
        print("General check up cost is per day :", gnchkup)
        dr_munna = 300 
        print("Routine check up fees of the Dr.Munna is per day :", dr_munna) 
        dr_gulathi = 700 
        print("General check up fees of the Dr.Gulathi is per day :",dr_gulathi)
        
        GW_pdc=(gnwd+rchkup+gnchkup+dr_munna+dr_gulathi)
        print("\nGeneral ward per day cost :",GW_pdc)
        
        total_bill=(p_days*GW_pdc)
        print("\nFinal Bill Amount is :",total_bill)
        
class Sharingward():   
    def choice2(self):
        
        shrmwd = 1200 
        print("Sharing Room Ward charges is per day :", shrmwd) 
        rchkup = 500 
        print("Routine check up cost is per day :", rchkup)
        spchkup = 1400 
        print("Specialised check up cost is per day :", spchkup)
        dr_chinki = 900 
        print("Specialised check up fees of the Dr.Chinki is per day :", dr_chinki) 
        dr_munna = 300 
        print("Routine check up fees of the Dr.Munna is per day :", dr_munna)
        
        SW_pdc=(shrmwd+rchkup+spchkup+dr_chinki+dr_munna)
        print("\nSharing Ward per day cost :",SW_pdc)
        
        total_bill=(p_days*SW_pdc)
        print("\nFinal Bill Amount is :",total_bill)
        
    
class Specialward():   
    def choice3(self):
       
        sprmwd = 1800 
        print("Special Room Ward charges is per day :", sprmwd) 
        spchkup = 1400 
        print("Specialised check up cost is per day :", spchkup)
        gnchkup = 800 
        print("General check up cost is per day :", gnchkup)
        dr_chinki = 900 
        print("Specialised check up fees of the Dr.Chinki is per day :", dr_chinki) 
        dr_gulathi = 700 
        print("General check up fees of the Dr.Gulathi is per day :",dr_gulathi)
        
        SpW_pdc=(sprmwd+spchkup+gnchkup+dr_chinki+dr_gulathi)
        print("\nSpecial Ward per day cost :",SpW_pdc)
        
        total_bill=(p_days*SpW_pdc)
        print("\nFinal Bill Amount is :",total_bill)
       
    
class ICUward():   
    def choice4(self):
        
        icuwd = 2500 
        print("ICU Ward charges is per day :", icuwd)
        emchkup = 1800 
        print("Emergency check up cost is per day :", emchkup) 
        spchkup = 1400 
        print("Specialised check up cost is per day :", spchkup)
        gnchkup = 800 
        print("General check up cost is per day :", gnchkup)
        dr_chinki = 900 
        print("Specialised check up fees of the Dr.Chinki is per day :", dr_chinki) 
        dr_gulathi = 700 
        print("General check up fees of the Dr.Gulathi is per day :",dr_gulathi)
        dr_asthana = 1100 
        print("Emergency check up fees of the Dr.Asthana is per day :",dr_asthana)
        
        ICU_pdc=(icuwd+emchkup+spchkup+gnchkup+dr_chinki+dr_gulathi+dr_asthana)
        print("\nICU Ward per day cost :",ICU_pdc)
        
        total_bill=(p_days*ICU_pdc)
        print("\nFinal Bill Amount is :",total_bill)
        
        
        
class Hospital(Generalward,Sharingward,Specialward,ICUward):
    def total(self):
            

        if choice==1:
            print("\nPatient Hospital Total Bill")  
            print("\n1.General Ward\n")
            obj1=Generalward()   
            obj1.choice1()
            
        elif choice==2:  
            print("\nPatient Hospital Total Bill")  
            print("\n2.Sharing Ward\n")
            obj2=Sharingward()   
            obj2.choice2()   

        elif choice==3:  
            print("\nPatient Hospital Total Bill") 
            print("\n3.Special Ward\n")
            obj3=Specialward()   
            obj3.choice3()

        elif choice==4:  
            print("\nPatient Hospital Total Bill")  
            print("\n4.ICU Ward\n")
            obj4=ICUward()   
            obj4.choice4()

        else:  
            print("Oops! Incorrect Choice. Please select correct option.")
    
            
            
obj=Hospital()
obj.total()
   


# In[ ]:





# In[ ]:




