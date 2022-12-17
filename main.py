import pickelfuncs
import classes
import os

if __name__ == '__main__':
    if not os.path.exists('busrouts.pickle'):

        print('welcome bla bla bla')
        bus_company = classes.BestBus()
    else:
        print("hello again lala")
        bus_company = pickelfuncs.load_object('busrouts.pickle')
    classes.BestBus.manager_passenger(bus_company)
    pickelfuncs.save_object(bus_company)
    print('saved')

#  ###########################PASSWORD FOR MANAGER - " RideWithUs! " ###########################

