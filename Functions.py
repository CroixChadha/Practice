true = ["t", "r", "u", "e"]
love = ["l","o","v","e"]

def calculate_love_score(name1, name2):
    combined_name = name1.lower() + name2.lower()
    t = combined_name.count("t")
    r = combined_name.count("r") 
    u = combined_name.count("u")
    e1 = combined_name.count("e") 
    true_sum = t + r + u + e1
    l = combined_name.count("l")
    o = combined_name.count("o")
    v = combined_name.count("v")
    e2 = combined_name.count("e")
    love_sum = l + o + v + e2
    total = str(true_sum) + str(love_sum)
    print(total)

calculate_love_score("Angela Yu", "Jack Bauer")
