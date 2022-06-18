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
