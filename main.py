import funcs
import classes
import os
#
if __name__ == '__main__':
    if not os.path.exists('busrouts.pickle'):
        print('welcome bla bla bla')
        bus_company = classes.BestBusCompany()
        classes.BestBusCompany.manager_passenger(bus_company)
        funcs.save_object(bus_company.all_routs)
    else:
        print("hello again lala")
        classes.BusRoute.all_routs = funcs.load_object('busrouts.pickle')
        bus_company = classes.BestBusCompany()
        classes.BestBusCompany.manager_passenger(bus_company)
        funcs.save_object(bus_company.all_routs)

# PASSWORD FOR MANAGER IS ########################### " RideWithUs! " ###########################

#     classes.BestBusCompany.manager_passenger(bus_company)
#     fh.write(classes.BestBusCompany().all_routs)