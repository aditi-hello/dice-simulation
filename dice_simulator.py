import random
 
x = "y"
while x == "y":

    num = random.randint(1,6)
    # num = int(input("enter: "))

    if num == 1:
        print("\n",
            "┌─────────┐\n",
            "│         │\n",
            "│    ●    │\n",
            "│         │\n",
            "└─────────┘",)
        # print("[=====]")
        # print("[     ]")
        # print("[  0  ]")
        # print("[     ]")
        # print("[=====]")
    if num == 2:
        print("\n",
        "┌─────────┐\n",
        "│  ●      │\n",
        "│         │\n",
        "│      ●  │\n",
        "└─────────┘\n",
        )
    if num == 3:
        print("\n",
            "┌─────────┐\n",
            "│  ●      │\n",
            "│    ●    │\n",
            "│      ●  │\n",
            "└─────────┘\n",
        )
    if num == 4:
        print("\n",
            "┌─────────┐\n",
            "│  ●   ●  │\n",
            "│         │\n",
            "│  ●   ●  │\n",
            "└─────────┘\n",
        )
    if num == 5:
        print("\n",
            "┌─────────┐\n",
            "│  ●   ●  │\n",
            "│    ●    │\n",
            "│  ●   ●  │\n",
            "└─────────┘\n",
        )
    if num == 6:
        print("\n",
            "┌─────────┐\n",
            "│  ●   ●  │\n",
            "│  ●   ●  │\n",
            "│  ●   ●  │\n",
            "└─────────┘\n",
       )

    x = input(f"press \"Y\" to roll again and \"N\" to exit: ")




# while True:
#     print('''1. Roll the dice   2. To exit ''')
#     user = int(input("What you want to do? "))

#     if user == 1:
#         number = random.randint(1,6)
#         print("Number :", number)
#     else:
#         break