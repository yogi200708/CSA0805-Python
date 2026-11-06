# TASK 1: Electricity Subsidy Eligibility
def separate_ifs(units, card, elderly):
    result = []
    if units <= 100: result.append("Full subsidy")
    if 101 <= units <= 200 and card: result.append("Partial subsidy")
    if 101 <= units <= 200 and not card: result.append("No subsidy")
    if units > 200 and elderly: result.append("Special subsidy")
    if units > 200 and not elderly: result.append("No subsidy")
    return result

def one_decision(units, card, elderly):
    if units <= 100: return "Full subsidy"
    elif 101 <= units <= 200:
        if card: return "Partial subsidy"
        else: return "No subsidy"
    elif elderly: return "Special subsidy"
    else: return "No subsidy"

data = [(100,False,False),(101,True,False),(101,False,False),(200,True,False),
        (200,False,True),(201,False,False),(201,False,True),(80,True,True)]
for row in data:
    print(row, "| separate ifs:", separate_ifs(*row), "| if-elif:", one_decision(*row))
print("if-elif-else selects one branch; separate if statements are checked independently.")
