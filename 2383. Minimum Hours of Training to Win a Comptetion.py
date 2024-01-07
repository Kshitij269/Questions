initialEnergy = 5
initialExperience = 3
energy = [1, 4, 3, 2]
experience = [2, 6, 3, 1]

egy_req = 0
exp_req = 0

for i in range(len(energy)):
    print(initialEnergy,initialExperience,egy_req,exp_req)
    if energy[i] < initialEnergy and experience[i] < initialExperience:
        initialExperience += experience[i]
        initialEnergy -= energy[i]

    elif energy[i] < initialEnergy and experience[i] > initialExperience:
        exp_req += experience[i] - initialExperience
        initialExperience += experience[i]

    elif energy[i] > initialEnergy and experience[i] < initialExperience:
        egy_req += energy[i] - initialEnergy
        initialEnergy -= energy[i]

    elif energy[i] > initialEnergy and experience[i] > initialExperience:
        exp_req += experience[i] - initialExperience
        egy_req += energy[i] - initialEnergy

print(exp_req + egy_req)
