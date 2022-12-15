class BusRoute:

    def __init__(self, line: str, origin: str, destination: str):
        self.line = line
        self.origin = origin
        self.destination = destination
        self.stops = [self.origin, self.destination]
        self.scheduled_rides = []

    def __repr__(self):
        return self.line

    def __str__(self):
        return f"Line number: {self.line}\n" \
               f"Origin: {self.origin}\n" \
               f"Destination: {self.destination}\n" \
               f"Stops: {self.stops}\n" \
               f"Scheduled rides: {self.scheduled_rides}"

    def get_ride(self, origin_time):
        for ride in self.scheduled_rides:
            if ride.origin_time == origin_time:
                return ride

    # def __getitem__(self, item):
    #     return item


class ScheduledRide:

    def __init__(self, ride_id, startime, endtime, name):
        self.id = ride_id
        self.origin_time = startime
        self.destination_time = endtime
        self.driver_name = name
        self.delays = None

    def __str__(self):
        return f"Id: {self.id}\n" \
               f"Origin time: {self.origin_time}\n" \
               f"Destination time: {self.destination_time}\n" \
               f"Driver: {self.driver_name}\n" \
               f"Delays: {self.delays}"

    def __repr__(self):
        return self.origin_time

    def __getitem__(self, item):
        return item

    def new_ride(self):
        pass


def is_manager():
    counter = 0
    while counter < 3:
        password = input('password =')
        if password == 'RideWithUs!':  #
            return True
        else:
            counter += 1
            print('wrong password', 3 - counter, 'tries remaining')
    print('blocked')
    return False


class BestBusCompany:

    def __init__(self):
        self.rides_counter = 1
        self.rout_nums = 1
        self.all_routs = []

    def manager_passenger(self):
        choice = input('log in as manager - 1 or passenger - 2')
        while not choice.isdigit() or int(choice) < 0 or int(choice) > 2:
            choice = input(print('log in as manager - 1 or passenger - 2'))
        if int(choice) == 1 and is_manager():
            return self.manager_menu()
        elif choice == '2':
            return self.passenger_menu()

    # manager functions---------------------------------------------------------------------------

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
        option = input('what do you want to do?')
        while not option.isnumeric() or not 0 <= int(option) <= 8:
            option = input('what do you want to do?')
        if option == '1':
            self.add_route()
        elif option == '2':
            self.delete_route(self.get_route(input('line num - ')))
            return self.manager_menu()
        elif option == '3':
            self.update_route(self.get_route(input('line num -')))
            return self.manager_menu()
        elif option == '4':
            self.add_scheduled_ride(self.get_route(input('choose route')))
        elif option == '5':
            route = self.get_route(input('choose route'))
            ride = route.get_ride(input('time of departure'))
            self.delete_scheduled_ride(route, ride)
        elif option == '6':
            self.update_scheduled_ride((self.get_route(input('choose route')).get_ride(input('time of departure'))))
            return self.manager_menu()
        elif option == '7':
            print(self.all_routs)
            return self.manager_menu()
        elif option == '8':
            route = self.get_route(input('choose route'))
            for ride in route.scheduled_rides:
                print(f"route number {route.line} leaves {route.origin} at {ride.origin_time}\n"
                      f"Driver - {ride.driver_name} expected arrival at {ride.destination_time}")
            return self.manager_menu()
        elif option == '0':
            pass

    def get_route(self, line):
        # try:
        for route in self.all_routs:
            if route.line == line:
                return route
    # except:

    def add_route(self):
        line = self.rout_nums
        origin = input('original stop -')
        destination = input('final destination -')
        newroute = BusRoute(str(line), origin, destination)
        self.all_routs.append(newroute)
        self.rout_nums += 1
        return self.manager_menu()

    def delete_route(self, line: BusRoute):
        self.all_routs.remove(line)
        return self.manager_menu()

    def update_route(self, line: BusRoute):
        print('update menu:\n'
              '1 - line number\n'
              '2 - origins\n'
              '3 - final\n'
              '4 - add stop\n'
              '5 - remove stop\n'
              '0 - back')
        update = input('what do you want to update?')
        while not update.isdigit() or not 0 <= int(update) <= 5:
            update = input(print('what do you want to update?'))
        if update == '1':
            line.line = input('change line number -')
        elif update == '2':
            line.origin = input('change line origin -')
        elif update == '3':
            line.destination = input('change line finale stop -')
        elif update == '4':
            stop = input('new line stop - ')
            line.stops.append(stop)
        elif update == '5':
            stop = input('which stop - ')
            if stop in line.stops:
                line.stops.remove(stop)
            else:
                print('no such stop for this line')
        elif update == '0':
            return self.manager_menu()

    def add_scheduled_ride(self, route: BusRoute):
        startime = input("insert starting time for ride")
        destination_time = input("insert expected ending time for ride")
        driver_name = input("driver's name -")
        newride = ScheduledRide(self.rides_counter, startime, destination_time, driver_name)
        self.rides_counter += 1
        route.scheduled_rides.append(newride)
        return self.manager_menu()

    def delete_scheduled_ride(self, route: BusRoute, line: ScheduledRide):
        route.scheduled_rides.remove(line)
        return self.manager_menu()

    def update_scheduled_ride(self, ride: ScheduledRide):
        print('1 - update startime\n'
              '2 - update endtime \n'
              '3 update Driver \n'
              '0 back')
        command = input('what do you want to do?')
        while not command.isnumeric() or not 0 <= int(command) <= 3:
            command = input('what do you want to do?')
        match command:
            case '1':
                ride.origin_time = input('startime -')
                return self.manager_menu()
        match command:
            case '2':
                ride.destination_time = input('endtime-')
                return self.manager_menu()
        match command:
            case '3':
                ride.driver_name = input('drivers name -')
                return self.manager_menu()
        match command:
            case '0':
                return self.manager_menu()

    # passenger functions---------------------------------------------------------------------------
    # add the RavKav option?
    def passenger_menu(self):
        print('passenger menu'
              '1 = search route'
              '2 = report delay')
        option = input('what do you want to do?')
        while not option.isnumeric() or not 0 <= int(option) < 4:
            option = input('what do you want to do?')
        if option == '1':
            self.search_route()
        elif option == '2':
            route = self.get_route(input('choose route'))
            ride = route.get_ride(input('time of departure'))
            self.report_delay(route, ride)
            return self.passenger_menu()
        elif option == '0':
            return False

    # Finds only one bus and exact time options for now
    # to do - add multiple rides for one journey, configure time estimation + rounding uo and down
    def search_route(self):
        start = input("from -")
        end = input("to -")
        when = input("when?")
        possible_rides = []
        for route in self.all_routs:
            if start and end in route.stops:
                possible_rides.append(route)
        for route in possible_rides:
            if when in route.scheduled_rides:
                print(route, when)
        return self.passenger_menu()

    def report_delay(self, route: BusRoute, ride: ScheduledRide):
        route.scheduled_rides[ride.origin_time].delays += 1
        return self.passenger_menu()

