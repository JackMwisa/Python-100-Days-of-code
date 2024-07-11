def liftoff_down(count):
    if count <= 0:
        print("liftoff!")
    else:
        print(count)
        liftoff_down(count - 1)