import pyautogui as myGui

def isInventoryOpen():
    if myGui.locateOnScreen("./images/inventory.png", confidence = 0.9):
        print("Inventory is closed...")
        print("opening Inventory")
        tuple = myGui.locateOnScreen("./images/inventory.png", confidence = 0.9)
        cords = myGui.center(tuple)
        myGui.moveTo(cords)
        myGui.click()

    else:
        print("cant find Inventory on screen")

def drop():
    tuple = myGui.locateOnScreen("./images/copper_ore.png",confidence = 0.7)
    cords = myGui.center(tuple)
    myGui.rightClick(cords)
    tuple = myGui.locateOnScreen("./images/drop_copper_ore.png", confidence = 0.7)
    cords = myGui.center(tuple)
    myGui.click(cords)
    print("dropped ore")
