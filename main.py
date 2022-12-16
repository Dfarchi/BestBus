import pickelfuncs
import classes
import os
#
if __name__ == '__main__':
    if not os.path.exists('busrouts.pickle'):

        print('welcome bla bla bla')
        bus_company = classes.BestBus()
    else:
        print("hello again lala")
        bus_company = pickelfuncs.load_object('busrouts.pickle')
    # print(bus_company.all_routs[0])
    # for ride in bus_company.all_routs:
    classes.BestBus.manager_passenger(bus_company)
    pickelfuncs.save_object(bus_company)
    print('saved')

#  ###########################PASSWORD FOR MANAGER - " RideWithUs! " ###########################

#     classes.BestBusCompany.manager_passenger(bus_company)
#     fh.write(classes.BestBusCompany().all_routs)