

i = 2
car_started = False
car_stopped = False
while i > 1:
    action = str(input(">").lower())
    i += 1
    if action == "start":
        if not car_started:
            car_started = True
            print("Car started...Ready to go!")
        else:
            print("Car already started")
    elif action == "stop":
        if not car_stopped:
            car_stopped = True
            print("Car stopped")
        else:
            print("Car already stopped")
    elif action == "quit":
        exit()
    else:
        print("I don't understand that...")