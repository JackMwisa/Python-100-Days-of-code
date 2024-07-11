
def liftoff_up(count):
    if count >= 0:
        print('Liftoff!')
    else:
        print(count)
        liftoff_up(count + 1)