def main():
    user_input = int(input("Enter a number: "))
    if user_input > 0:
        liftoff_down(user_input)
    elif user_input < 0:
        liftoff_up(user_input)
    else:
        liftoff_up(user_input)

if __name__ == "__main__":
    main()