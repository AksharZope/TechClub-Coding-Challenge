

choice = "yes"
while(choice == "yes"):
    chem1 = input("Enter the chemical 1:")
    chem1 = chem1.lower()
    if chem1 != "oxygen" or "hydrogen" or "chlorine" or "carbon":
        print("invalid answer\n")
        break
        
        
    chem2 = input("Enter the chemical  2:")
    chem2 = chem1.lower()
    if chem2 != "oxygen" or "hydrogen" or "chlorine" or "carbon":
        print("invalid answer\n")
        break
            
        
        
        
   
    if chem1 == "oxygen" and chem2 == "hydrogen" or chem1 == "hydrogen" and chem2 == "oxygen":
        print("The mixure is","Water","\n","Symbol = H2O\n")
    if chem1 == "oxygen" and chem2 == "carbon" or chem1 == "carbon" and chem2 == "oxygen":
        print("The mixure is","Carbon-di-oxide","\n","Symbol = CO2\n")
    if chem1 == "oxygen" and chem2 == "chlorine" or chem1 == "chlorine" and chem2 == "oxygen":
        print("The mixure is","Chlorine monoxide","\n","Symbol = CL2O\n")
    if chem1 == "oxygen" and chem2 == "oxygen":
            print("The mixure is","Oxygen 2","\n","Symbol = O2 \n")    
       
        
     
    if chem1 == "carbon" and chem2 == "hydrogen" or chem1 == "hydrogen" and chem2 == "carbon":
        print("The mixure is","Hydocarbon","\n","Symbol = CH4\n")    
    if chem1 == "carbon" and chem2 == "chlorine" or chem1 == "chlorine" and chem2 == "carbon":
        print("The mixure is","Carbon Chlorine","\n","Symbol = CCl4\n")  
    if chem1 == "carbon" and chem2 == "carbon":
            print("The mixure is","Carbon 2","\n","Symbol = C2\n")         
        
    if chem1 == "hydrogen" and chem2 == "chlorine" or chem1 == "chlorine" and chem2 == "hydrogen":
        print("The mixure is","Hydrogen Chlorine","\n","Symbol = HCl\n")
    if chem1 == "hydrogen" and chem2 == "hydrogen":
            print("The mixure is","Hydrogen 2","\n","Symbol = H2\n")        

    if chem1 == "chlorine" and chem2 == "chlorine":
            print("The mixure is","Chlorine 2","\n","Symbol = Cl2\n ")    
    
    choice = input("Enter yes for continuing and no for stopping:")   
    choice = choice.lower()     