def create_head(title = "título",lineSize = 60):
    print("-"*lineSize)
    print(title.center(lineSize))
    print("-"*lineSize)


def create_menu(lst : list, title = "menu",lineSize = 60):
    print("-"*lineSize)
    print(title.center(lineSize))
    print("-"*lineSize)
    for i,c in enumerate(lst):
        print("{} - {}".format(i+1,c))
    print("-"*lineSize)


def show_menu(prodDict : dict,mainKey : str,subKey : str):
    create_head("Cardápio")
    create_head("{} {}".format(mainKey.title(),subKey.title()))
    for i,c in enumerate(prodDict[mainKey][subKey]):
        print("-> {}".format(c))
    


def is_payment_valid(productValue : float,userValue : float) -> bool:
    if userValue >= productValue:
        return True
    return False


def make_change(productValue : float,userValue : float) -> float:
    return userValue - productValue

