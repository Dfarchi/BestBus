import funcs
import classes
import os
#
# if __name__ == '__main__':
# if not os.path.exists('bus_company.pickle'):
#     print('welcome bla bla bla')
bus_company = classes.BestBusCompany()
# else:
#     with open('bus_company.pickle', 'rb') as fh:
#         print('hello again...')
#         bus_company = pickle.load(fh)

classes.BestBusCompany.manager_passenger(bus_company)

# with open('bus_company.pickle', 'wb') as fh:
#     pickle.dump(bus_company, fh)
