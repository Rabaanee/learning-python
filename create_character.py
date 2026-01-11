full_dot = '●'
empty_dot = '○'

def create_character(character_name,strength,intelligence,charisma):
    if not isinstance(character_name,str):
        return"The character name should be a string"
    if character_name == "":
        return "The character should have a name"
    if len(character_name) > 10:
        return "The character name is too long"
    for letter in character_name:
        if letter == " ":
            return "The character name should not contain spaces"
    if not isinstance(strength,int) :
        return "All stats should be integers"
    if not isinstance(intelligence,int) :
        return "All stats should be integers"
    if not isinstance(charisma,int) :
        return "All stats should be integers"
    if not isinstance(intelligence,int) :
        return "All stats should be integers"
    if not isinstance(charisma,int) :
        return "All stats should be integers"    
    if strength  < 1:
        return "All stats should be no less than 1"
    if intelligence < 1:
        return "All stats should be no less than 1"
    if charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4:
        return "All stats should be no more than 4"
    if intelligence > 4:
        return "All stats should be no more than 4"
    if charisma > 4:
        return "All stats should be no more than 4"
    total_score = strength + intelligence + charisma
    if total_score != 7:
        return "The character should start with 7 points" 
    thing1 = "STR" + " " + (full_dot * strength) + (empty_dot * (10-strength))
    thing2 = "INT" + " " + (full_dot * intelligence) + (empty_dot * (10-intelligence))
    thing3 = "CHA" + " " + (full_dot * charisma) + (empty_dot * (10-charisma))
    return character_name + "\n" + thing1 + "\n" + thing2 + "\n" + thing3 
