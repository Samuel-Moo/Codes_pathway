with open("hr_system.txt") as file:
    for name in file:
        
        words = name.split(" ")
        
        Name = words[0]
        Id = words[1]
        Job = words[2]
        Salary = float(words[3])
        
        payment = Salary / 24
        
        if Job == "Engineer":
            payment += 1000
        
        print(f"{Name} (ID: {Id}), {Job} - ${payment:.2f}".strip())
        