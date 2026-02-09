#dict is dictionary and should contain settings
#tple is tuple and should contain key-value pairs
def add_setting(settings_dict, tple):
    key_add, value_add = tple
    key_add = key_add.lower()
    value_add = value_add.lower()
    if key_add in settings_dict:
        return f"Setting '{key_add}' already exists! Cannot add a new setting with this name."
    
    if key_add not in settings_dict.keys(): #can be replaced with an else because first if checked that the key is not present
        settings_dict[key_add] = value_add
        return f"Setting '{key_add}' added with value '{value_add}' successfully!"

def update_setting(update_dict, tple):
    key_upd, value_upd = tple
    key_upd = key_upd.lower()
    value_upd = value_upd.lower()
    if key_upd in update_dict:
        update_dict[key_upd] = value_upd
        #update_dict = {**update_dict, key_upd: value_upd} 
        #does same as update_dict[key_upd] = value_upd ==> not really the same it creates another dictionary 
        #so it does not really update it
        return f"Setting '{key_upd}' updated to '{value_upd}' successfully!"
    
    if key_upd not in update_dict:
        return f"Setting '{key_upd}' does not exist! Cannot update a non-existing setting."

def delete_setting(del_dict, tple):
    key_del = tple
    key_del = key_del.lower()
    if key_del in del_dict:
        del_dict.pop(key_del, None) #can use del del_dict but if key does not exist will give KeyError
        return f"Setting '{key_del}' deleted successfully!"
    
    if key_del not in del_dict:
        return f"Setting not found!"

def view_settings(view_dict):
    if len(view_dict) == 0:
        return f"No settings available."
    
    if len(view_dict) != 0:
        lines = "\n".join(f"{key.capitalize()}: {value}" for key, value in view_dict.items())
                #\n is so there is no joining of keys with values
        return f"Current User Settings:\n{lines} \n"

test_settings = {
    "theme": "dark",
    "language": "en",
    "notifications": "enabled",
    "volume": "high"
}
test_settings_empty = {}
test_settings_alt = {
    "theme": "light",
    "language": "nl",
    "notifications": "disabled"
}

add_new_1 = ("timezone", "UTC")
add_new_2 = ("font_size", "Medium")
add_existing = ("Theme", "LIGHT")

update_existing_1 = ("notifications", "DISABLED")
update_existing_2 = ("VOLUME", "LOW")
update_missing = ("privacy_mode", "ON")

delete_existing = "Language"
delete_missing = "brightness"


#print(view_settings(test_settings_empty))
print(view_settings(test_settings))
#print(delete_setting(test_settings, delete_existing))