full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    name_check = check_name(name)
    stat_check = check_stat(strength, intelligence, charisma)
    if name_check == True and stat_check == True:
        stats = {"STR": strength, "INT": intelligence, "CHA": charisma}
        for i in stats:
            full_dots = full_dot * i
            empty_dots = 10 - full_dots
        return f"""Character Created!
        Name {name}
        STR {STR}
        INT {INT}
        CHA {CHA}"""

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