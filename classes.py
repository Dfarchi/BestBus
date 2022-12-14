
class BusRoute:

    def __init__(self, line: str, origin: str, destination: str, stops=0):
        self.line = line
        self.origin = origin
        self.destination = destination
        self.stops = [self.origin, self.destination]
        self.scheduled_rides = []

    def __repr__(self):
        # return f'line number {self.line}, originates at {self.origin}'
        return self.scheduled_rides

    def __str__(self):
        return self.line


class ScheduledRide:

    def __init__(self, ride_id, startime, endtime, name):
        self.id = ride_id
        self.origin_time = startime
        self.destination_time = endtime
        self.driver_name = name
        self.delays = None

    def __repr__(self):
        return self.id

    def __str__(self):
        return self.origin_time


class BestBusCompany:

    # Stores and manages information about the whole company, including:
    # All the routes and schedules
    # All the actions defined earlier

    def __init__(self):
        self.rides_counter = 1
        self.rout_nums = 1
        self.all_routs = []

    def manager_passenger(self):
        choice = input('log in as manager - 1 or passenger - 2')
        while not choice.isdigit() or int(choice) < 0 or int(choice) > 2:
            choice = input(print('log in as manager - 1 or passenger - 2'))
        if int(choice) == 1 and self.is_manager():
            return self.manager_menu()
        elif choice == '2':
            return self.passenger_menu()

    # passenger functions---------------------------------------------------------------------------
    # add the RavKav option?
    def passenger_menu(self):
        print('passenger menu')
        option = input('what do you want to do?')
        while not option.isnumeric() or not 0 < int(option) < 4:
            option = input('what do you want to do?')
        if option == '1':
            self.search_route()
        elif option == '2':
            self.report_delay()
        pass

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

    def report_delay(self):
        pass

    # manager functions---------------------------------------------------------------------------

    def is_manager(self):
        counter = 0
        while counter < 3:
            password = input('password =')
            if password == '':   #RideWithUs!
                return True
            else:
                counter += 1
                print('wrong password', 3 - counter, 'tries remaining')
        print('blocked')
        return False

    def manager_menu(self):
        print('manager menu \n 1 = add route \n 2 = delete route \n 3 = update route \n 4 = see all routs \n'
              '5 = see all scheduled rides for a route\n'
              '6 = add ride to route schedule(?) \n 0 = exit')
        option = input('what do you want to do?')
        while not option.isnumeric() or not 0 <= int(option) <= 6:
            option = input('what do you want to do?')
        if option == '1':
            self.add_route()
        elif option == '2':
            route = self.all_routs[int(input('choose route'))-1]
            while route not in self.all_routs:
                route = self.all_routs[int(input('line num doesnt exist try another num , 0 to go back- '))]
                if route == '0':
                    return self.manager_menu()
            self.delete_route(route)
        elif option == '3':
            route = self.all_routs[int(input('line num - '))-1]
            while route not in self.all_routs:
                route = self.all_routs[int(input('line num doesnt exist try another num , 0 to go back- '))]
                if route == '0':
                    return self.manager_menu()
            self.update_route(route)
        elif option == '4':
            print(self.all_routs)
            return self.manager_menu()
        elif option == '5':
            route = self.all_routs[int(input('what route - '))-1]
            print(f"route number {route.line} leaves {route.origin} at:")
            for ride in route.scheduled_rides:
                print(ride)
            return self.manager_menu()
        elif option == '6':
            route = self.all_routs[int(input('choose route'))-1]
            self.add_scheduled_ride(route)
        elif option == '0':
            pass
        #     ScheduledRide.add_scheduled_ride()

    # general manging functions
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
        while line not in self.all_routs:
            line = input("no such line try again -")
        print('update menu:\n'
              '1 - line number\n'
              '2 origins\n'
              '3 -finalle\n'
              '4- stops\n'
              '5 - rides\n'
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
            add_remove = input("add - 1 or remove - 2")
            if add_remove == '1':
                stop = input('new line stop - ')
                line.stops.append(stop)
            elif add_remove == '2':
                stop = input('which stop - ')
                if stop in line.stops:
                    line.stops.remove(stop)
                else:
                    print('no such route')
                    return self.manager_menu()
        elif update == '5':
            add_remove = input("add - 1 or remove - 2")
            if add_remove == '1':
                self.add_scheduled_ride(line)
            # elif add_remove == '2':

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



