full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    name_check = check_name(name)
    if name_check != True:
        return name_check
    stat_check = check_stat(strength, intelligence, charisma)
    if stat_check != True:
        return stat_check
    char_stats = f"{name}"
    if name_check == True and stat_check == True:
        print("Character created successfully!")
        stats = {"STR": strength, "INT": intelligence, "CHA": charisma}
        for i in stats:
            full_dots = full_dot * stats[i]
            empty_dots = empty_dot*(10 - stats[i])
            char_stats += f"\n{i} {full_dots}{empty_dots}"
        return f"""{char_stats}"""

def check_name(name):
    # checks if name is a string
    if not isinstance(name, str):
        return "The character name should be a string"
    
    # checks if name is empty
    if not name:
        return "The character should have a name"
    
    # checks if name is longer than 10 characters
    if len(name) > 10:
        return "The character name is too long"
    
    # checks if name contains spaces
    if " " in name:
        return "The character name should not contain spaces"
    
    else:
        return True

def check_stat(strength, intelligence, charisma):
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    
    else:
        return True

print(create_character("ren",4,2,1))