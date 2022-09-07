#Take string 
# SPREAD
# MONEY
# TOTAL
#And each team and format them in a readable way


def sort_elem(s: str):
    print(s)
    
    string_to_add = s.split(" ")
    if len(string_to_add) < 23:
        return

    new_dict_entry = {
        
        f"{string_to_add[0]} {string_to_add[1]}" : #Away Team
            {
                "Spread": f"{string_to_add[4]} / {string_to_add[5]}",
                "Money": f"{string_to_add[6]}",
                "Total": f"{string_to_add[7]} {string_to_add[8]} / {string_to_add[9]}"
            },
        f"{string_to_add[2]} {string_to_add[3]}" : #Home Team
            {
                "Spread": f"{string_to_add[10]} / {string_to_add[11]}",
                "Money": f"{string_to_add[12]}",
                "Total": f"{string_to_add[13]} {string_to_add[14]} / {string_to_add[15]}"             
            },
        
    }   
 
    return new_dict_entry

