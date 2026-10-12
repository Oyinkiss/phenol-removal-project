print("===========================================")
print("PHENOL  REMOVAL EFFICIENCY CALCULATOR")
print("===========================================")
#Step 1: Collect input data from user
initial_concentration = float(input("Enter the initial concentration of phenol (mg/L): "))
final_concentration = float(input("Enter the final concentration of phenol (mg/L): "))

#Step 2:Validate input data

if initial_concentration <= 0:
    print("Error: Initial concentration must be greater than zero.")
elif final_concentration < 0:
    print("Error: Final concentration cannot be negative.") 
elif final_concentration > initial_concentration:
    print("Error: Final concentration cannot be greater than initial concentration.")
    
else:
    #Step 3: Calculate removal efficiency
    removal_efficiency = ((initial_concentration - final_concentration) / initial_concentration) * 100
    #Step 4: Display the result
    print("\n==================RESULT========================")
    print(f"Initial Concentration:"f"{initial_concentration:.2f} mg/L")
    print(f"Final Concentration:"f"{final_concentration:.2f} mg/L")
    print(f"Removal Efficiency of Phenol:"f"{removal_efficiency:.2f}%")
    print("=================================================")
