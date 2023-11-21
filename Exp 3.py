def water_jug_puzzle(small_jug, big_jug, target):
    small = 0
    big = 0

    while big != target:
        if big == 0:
            print(f"Fill the {big_jug}-liter jug")
            big = big_jug
        else:
            print(f"Pour water from the {big_jug}-liter jug to the {small_jug}-liter jug")
            transfer_amount = min(big, small_jug - small)
            small += transfer_amount
            big -= transfer_amount

        if small == small_jug:
            print(f"Empty the {small_jug}-liter jug")
            small = 0

        print("------")

    print(f"Desired amount of {target} liters achieved in the {big_jug}-liter jug!")

small_jug_size = 3
big_jug_size = 4
target_amount = 2

water_jug_puzzle(small_jug_size, big_jug_size, target_amount)
