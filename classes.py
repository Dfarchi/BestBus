class Ride:

    def __init__(self, counter, origin_time, final_time, driver_name, hobby):
        # self.side = 'front'
        self.id = counter
        self.origin_time = origin_time
        self.final_time = final_time
        self.driver = driver_name
        self.drivers_hobby = hobby
        self.delays = 0

    def __str__(self):
        return f"Ride number: {self.id}\n" \
               f"time of departure: {self.origin_time}\n" \
               f"estimated time of arrival: {self.final_time}\n"

    def __repr__(self):
        return self.origin_time


class Route:

    def __init__(self, line: int, origin: str, final: str):
        self.line_num = line
        self.origin = origin
        self.final = final
        self.stops = []
        self.rides = {}

    # def __repr__(self):

    def __str__(self):
        return f"Line number: {self.line_num}\n" \
               f"Origin: {self.origin}\n" \
               f"Destination: {self.final}\n" \
               f"Stops: {self.stops}\n" \
               f"Scheduled rides: {self.rides}"


def is_manager() -> bool:
    """checks manager password"""
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


def get_ride(route: Route, ride: str) -> Ride:
    """ Takes Route instance and a ride id, returns Ride instance  """
    while ride not in route.rides:
        print(f"route {route.line_num} rides id's:")
        [print(route.rides[r].id) for r in route.rides]
        ride = input("no ride with that id, try a new one -")
    else:
        return route.rides[ride]


class BestBus:

    def __init__(self):
        self.routs = {}
        self.rout_counter = 1
        self.ride_counter = 1

    def manager_passenger(self):
        """First function that user meets returns correct menu"""
        choice = input('log in as manager - 1 or passenger - 2')
        while not choice.isdigit() or int(choice) < 0 or int(choice) > 2:
            choice = input('log in as manager - 1 or passenger - 2')
        if int(choice) == 1 and is_manager():
            return self.manager_menu()
        elif choice == '2':
            return self.passenger_menu()

    def manager_menu(self):
        """Manager menu, mainly validates inputs and call necessary functions"""
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
                self.rout_counter -= 1
            elif option == '3':
                route = self.get_route(input('Route num - '))
                if route:
                    self.update_route(route)
            elif option == '4':
                if len(self.routs) == 0:
                    print('no routs yet, plz update system')
                    pass
                else:
                    route = self.get_route(input('line num - '))
                    if route:
                        self.add_ride(route)
            elif option == '5':
                if len(self.routs) == 0:
                    print('no routs yet, plz update system')
                    pass
                route = self.get_route(input('choose route'))
                if len(route.rides) == 0:
                    print('no rides for this rout yet, plz update system')
                    pass
                else:
                    ride = get_ride(route, input('ride id -'))
                    del route.rides[str(ride.id)]
                    self.ride_counter -= 1
            elif option == '6':
                if len(self.routs) == 0:
                    print('no routs yet, plz update system')
                    pass
                route = self.get_route(input('choose route'))
                if len(route.rides) == 0:
                    print('no rides for this route yet, you can update new ones from the update menu')
                    pass
                else:
                    ride = get_ride(route, input('ride id -'))
                    self.update_ride(route, ride)
            elif option == '7':
                self.get_all_routes()
                # if len(self.routs) == 0: print('no routs yet, plz update system') pass for route in
                # self.routs.keys(): print(f"route number {self.routs[route].line_num} leaves {self.routs[
                # route].origin} and stops at:\n" f"{self.routs[route].stops} final stop - {self.routs[route].final}")
            elif option == '8':
                self.get_all_rides()
            elif option == '0':
                break

    def add_route(self):
        """"creates new Route class instance"""
        new = Route(self.rout_counter,
                    input('origin of Route -'),
                    input('final stop - '))
        self.routs[str(self.rout_counter)] = new
        self.rout_counter += 1

    def update_route(self, route: Route):
        """update menu, redefines or edit specific Route class instances by attribute"""
        print(route)
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
                update = input('what do you want to update?')
            if update == '1':
                self.routs[str(route.line_num)].line_num = (int(input('new line number -')))
            elif update == '2':
                self.routs[str(route.line_num)].origin = input('new line origin -')
            elif update == '3':
                self.routs[str(route.line_num)].final = input('new line final stop -')
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
        """gets Route id and returns Routs instance or None"""
        if route in self.routs.keys():
            return self.routs[route]
        else:
            print('cant find route')

    def add_ride(self, route: Route):
        """"creates new Ride class instance"""
        departure = input('time of departure -')
        for ride in route.rides.keys():
            while route.rides[ride].origin_time == departure:
                print('there is already a ride that departs at this hour time')
                departure = input('time of departure -')
        arrival = input('time of arrival - ')
        name = input('drivers name -')
        hobby = input('drivers hobby -')
        new = Ride(self.ride_counter, departure, arrival, name, hobby)
        route.rides[str(self.ride_counter)] = new
        self.ride_counter += 1

    def update_ride(self, route: Route, ride: Ride):
        """update menu, redefines specific Route class instances by attribute"""
        print(ride)
        ride_in_dict = self.routs[str(route.line_num)].rides[str(ride.id)]
        # shortcut to update the DB instead of Ride.attribute which caused problems
        print('1 - update star time\n'
              '2 - update end time \n'
              '3 - update driver name \n'
              '4 - update drivers hobby \n'
              '0 back')
        command = input('what do you want to do?')
        while not command.isnumeric() or not 0 <= int(command) <= 4:
            command = input('what do you want to do?')
        match command:
            case '1':
                ride_in_dict.origin_time = input('start time -')
        match command:
            case '2':
                ride_in_dict.final_time = input('end time-')
        match command:
            case '3':
                ride_in_dict.driver = input('drivers name -')
        match command:
            case '4':
                ride_in_dict.drivers_hobby = input('drivers hobby -')
        match command:
            case '0':
                return

    def get_all_routes(self):
        """prints all routs that the Bus company has"""
        if len(self.routs) == 0:
            print('no routs yet, plz update system')
            pass
        for route in self.routs.keys():
            print(f"--------------------------------------------------------------------\n"
                  f"route number {self.routs[route].line_num} leaves {self.routs[route].origin} and stops at:\n"
                  f"{self.routs[route].stops} final stop - {self.routs[route].final}")
            print(f"--------------------------------------------------------------------\n")

    def get_all_rides(self):
        """prints all rides for specific route"""
        if len(self.routs) == 0:
            print('no routs yet, plz update system')
            pass
        else:
            route = self.get_route(input('what route-'))
            if not route:
                pass
            elif len(route.rides) == 0:
                print('no rides for this route yet, you can update new ones from the update menu')
                pass
            else:
                for r in route.rides.keys():
                    ride = get_ride(route, r)
                    print(f'---------------------------------------------\n'
                          f'line {route.line_num} ride id {ride.id} \n'
                          f'leaves {route.origin} at {ride.origin_time}'
                          f'arrives to {route.final} at {ride.final_time} \n '
                          f'stops at {route.stops} \n '
                          f'Driver -{ride.driver}, likes {ride.drivers_hobby}\n'
                          f'{ride.delays} delays reported')
                print(f"---------------------------------------------\n")

    def passenger_menu(self):
        """Passenger menu use as a search method or as a specific Ride attribute edit"""
        while True:
            print('passenger menu:\n'
                  '1 - search for bus ride \n'
                  '2 - report bus ride delay\n'
                  '3 - see all bus routs \n'
                  '4 - see all rides for route\n'
                  '0 - exit')
            command = input('what do you want to do?')
            while not command.isnumeric() or not 0 <= int(command) <= 4:
                command = input('what do you want to do?')
            match command:
                case '1':
                    self.journey()
                case '2':
                    self.report_delay()
                case '3':
                    self.get_all_routes()
                case '4':
                    self.get_all_rides()
                case '0':
                    break

    def journey(self):
        """search function, user inputs start and end point.
         prints all routs that goes through those stops at that hour"""
        # problem 1 - it only checks for the rides time of departure because I haven't planned ahead enough in advance
        # to add a BusStop class that would hold time of arrival to each stop per ride
        # problem 2 - need to either add a ride.direction attribute or check that begin comes after end
        begin = str(input('from -'))
        end = str(input('to - '))
        when = (input('when? HH format -'))
        searchlst = []
        for route in self.routs.keys():
            serachstoplst = self.routs[route].stops.copy()
            serachstoplst.insert(0, self.routs[route].origin)
            serachstoplst.append(self.routs[route].final)
            if begin and end in serachstoplst and serachstoplst.index(begin) < serachstoplst.index(end):
                searchlst.append(route)
        if len(searchlst) == 0:
            print('seems we dont have any bus route through these stops')
        else:
            for route in searchlst:
                noride = True
                for ride in self.routs[route].rides:
                    if int(when) == int(self.routs[route].rides[ride].origin_time):
                        print(f'route {route} leaves {begin} at {when}')
                        noride = False
                    # add no rides for these hour message
                if noride:
                    print(f"sorry we have no viable rides from {begin} at {when} ")

    def report_delay(self):
        route = self.get_route(str(input('what route?')))
        if not route:
            print("no such route")
            pass
        else:
            if len(route.rides) == 0:
                print("no such ride")
                pass
            ride = get_ride(route, str(input('ride id?')))
            if ride:
                self.routs[str(route.line_num)].rides[str(ride.id)].delays += 1
                print('Thank you for reporting this delay we are making every effort to crunch them down')
