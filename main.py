from typing import Type
import pyautogui as myGui
import time

#input position data from position.py into "rockCords" x cords first, then y cords
rockCords = [1892,511]

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
    try:
        tuple = myGui.locateOnScreen("./images/copper_ore.png",confidence = 0.7)
        cords = myGui.center(tuple)
        myGui.rightClick(cords)
        tuple = myGui.locateOnScreen("./images/drop_copper_ore.png", confidence = 0.7)
        cords = myGui.center(tuple)
        myGui.click(cords)
        print("dropped ore")
    except TypeError:
        print("TYPE ERROR in drop()")

def mine():
    myGui.moveTo(rockCords[0],rockCords[1])
    myGui.click()
    time.sleep(5)

isInventoryOpen()
while True:
    mine()
    drop()