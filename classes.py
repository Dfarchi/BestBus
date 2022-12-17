

class Ride:

    def __init__(self, counter, origin_time, final_time, driver_name, hobby):
        # self.side = 'front'
        self.id = counter
        self.origin_time = origin_time
        self.final_time = final_time
        self.driver = driver_name
        self.drivers_hobby = hobby
        self.delays = 0

    # def __repr__(self):
    #     return f"Ride ID: {str(self.id)}\n" \
    #            "Departure time: {self.origin_time}\n" \
    #            f"Arrival time: {self.final_time}\n" \
    #            f"Driver: {self.driver}, likes {self.drivers_hobby}\n" \
    #            f"Delays: {self.delays}"
    #
    # def __str__(self):
    #     return self.id
    #


class Route:

    def __init__(self, line: int, origin: str, final: str):
        self.line_num = line
        self.origin = origin
        self.final = final
        self.stops = []
        self.rides = {}

    def __repr__(self):
        return f"Line number: {self.line_num}\n" \
               f"Origin: {self.origin}\n" \
               f"Destination: {self.final}\n" \
               f"Stops: {self.stops}\n" \
               f"Scheduled rides: {self.rides}"

    def __str__(self):
        return self.line_num


def is_manager():
    counter = 0
    while counter < 3:
        password = input('password =')
        if password == '':  # RideWithUs!
            return True
        else:
            counter += 1
            print('wrong password', 3 - counter, 'tries remaining')
    print('blocked')
    return False


class BestBus:

    def __init__(self):
        self.routs = {}
        self.rout_counter = 1
        self.ride_counter = 1

    def manager_passenger(self):
        choice = input('log in as manager - 1 or passenger - 2')
        while not choice.isdigit() or int(choice) < 0 or int(choice) > 2:
            choice = input('log in as manager - 1 or passenger - 2')
        if int(choice) == 1 and is_manager():
            return self.manager_menu()
        elif choice == '2':
            return self.passenger_menu()

    def manager_menu(self):
        print('manager menu \n'
              '1 = add route \n'
              '2 = delete route \n'
              '3 = update route \n'
              '4 = add ride to route schedule \n'
              '5 = remove ride from route schedule \n'
              '6 = update specific ride \n'
              '7 = see all routs \n'
              '8 = see all scheduled rides for a route \n'
              '0 = exit')
        while True:
            option = input('what do you want to do? 0 to quit')
            while not option.isnumeric() or not 0 <= int(option) <= 8:
                option = input('what do you want to do?')
            if option == '1':
                self.add_route()
            elif option == '2':
                del self.routs[str(self.get_route(input('line num - ')).line_num)]
                # input=get_validated_input(input_type = driver_number, input)
            elif option == '3':
                self.update_route(self.get_route(input('line num - ')))
            elif option == '4':
                self.add_ride(input('line num - '))
            elif option == '5':
                route = self.get_route(input('choose route'))
                ride = self.get_ride(str(route.line_num), input('which ride ?'))
                del route.rides[str(ride)]
            elif option == '6':
                route = self.get_route(input('choose route'))
                ride = self.get_ride(str(route.line_num), input('which ride ?'))
                self.update_ride(route, ride)
            elif option == '7':
                if len(self.routs) == 0:
                    print('no routs yet, plz update system')
                    pass
                for route in self.routs.keys():
                    print(f"route number {self.routs[route].line_num} leaves {self.routs[route].origin} and stops at:\n"
                          f"{self.routs[route].stops} final stop - {self.routs[route].final}")
            elif option == '8':
                if len(self.routs) == 0:
                    print('no routs yet, plz update system')
                    pass
                else:
                    route = self.get_route(input('what route-'))
                    if len(route.rides) == 0:
                        print('no rides for this route yet, you can update new ones from the update menu')
                        pass
                    for r in route.rides.keys():
                        ride = self.get_ride(str(route.line_num), r)
                        print(
                            f'line {route.line_num} ride id {ride.id} leaves {route.origin} at {ride.origin_time} arrives to {route.final} at {ride.final_time} \n '
                            f'stops at {route.stops}'
                            f'Driver {ride.driver} likes {ride.drivers_hobby}')
            elif option == '0':
                break

    def add_route(self):
        new = Route(self.rout_counter,
                    input('origin of Route -'),
                    input('final stop - '))
        self.routs[str(self.rout_counter)] = new
        self.rout_counter += 1

    def update_route(self, route: Route):
        print('update menu:\n'
              '1 - line number\n'
              '2 - origins\n'
              '3 - final\n'
              '4 - add stop\n'
              '5 - remove stop\n'
              '0 - back')
        while True:
            update = input('what do you want to update? 0 to go back')
            while not update.isdigit() or not 0 <= int(update) <= 5:
                update = input(print('what do you want to update?'))
            if update == '1':
                self.routs[str(route.line_num)].line_num(int(input('new line number -')))
            elif update == '2':
                # route.stops.remove(route.origin)
                self.routs[str(route.line_num)].origin = input('new line origin -')
                # route.stops.insert(0, route.origin)
            elif update == '3':
                # route.stops.remove(route.final)
                self.routs[str(route.line_num)].final = input('new line final stop -')
                # route.stops.insert(-1, route.final)
            elif update == '4':
                stop = input('new line stop - ')
                route.stops.append(stop)
            elif update == '5':
                stop = input('which stop - ')
                if stop in route.stops:
                    route.stops.remove(stop)
                else:
                    print('no such stop for this line')
            elif update == '0':
                return

    def get_route(self, route: str) -> Route or None:
        return self.routs[route]

    def add_ride(self, route_num: str):
        route = self.get_route(route_num)
        new = Ride(self.ride_counter,
                   input('time of departure -'),
                   input('time of arrival - '),
                   input('drivers name -'),
                   input('drivers hobby -'))
        route.rides[str(self.ride_counter)] = new
        self.ride_counter += 1

    def get_ride(self, route_num: str, ride: str) -> Ride:
        return self.get_route(route_num).rides[ride]

    def update_ride(self, route: Route, ride: Ride):
        print('1 - update startime\n'
              '2 - update endtime \n'
              '3 - update driver name \n'
              '4 - updat drivers hobby \n'
              '0 back')
        command = input('what do you want to do?')
        while not command.isnumeric() or not 0 <= int(command) <= 4:
            command = input('what do you want to do?')
        match command:
            case '1':
                self.routs[str(route.line_num)].rides[str(ride.id)].origin_time = input('startime -')
        match command:
            case '2':
                self.routs[str(route.line_num)].rides[str(ride.id)].final_time = input('endtime-')
        match command:
            case '3':
                self.routs[str(route.line_num)].rides[str(ride.id)].driver = input('drivers name -')
        match command:
            case '4':
                self.routs[str(route.line_num)].rides[str(ride.id)].drivers_hobby = input('drivers hobby -')
        match command:
            case '0':
                return

    def passenger_menu(self):
        print('passenger menu:')
        command = input('what do you want to do?')
        while not command.isnumeric() or not 0 <= int(command) <= 4:
            command = input('what do you want to do?')
        match command:
            case '1':
                begin = str(input('from -'))
                end = str(input('to - '))
                when = int(input('when? -'))
                searchlst =[]
                for route in self.routs.keys():
                    serachstoplst = self.routs[route].stops
                    serachstoplst.append(self.routs[route].origin)
                    serachstoplst.append(self.routs[route].final)
                    if begin and end in serachstoplst:
                        searchlst.append(route)
                for route in searchlst:
                    for ride in self.routs[route].rides:
                        if when == int(self.routs[route].rides[ride].origin_time):
                            print(f'route {route} leaves {begin} at {when}')
            case '2':
                route = self.get_route(str(input('what route?')))
                ride = self.get_ride(route, str(input('what ride?')))
                self.routs[str(route.line_num)].rides[str(ride.id)].delay += 1
                print('Thank you for reporting this delay we are making every effort to crunch them down')
            case '0':
                pass




#