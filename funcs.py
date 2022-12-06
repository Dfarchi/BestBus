# import classes
#
#
# def manager_passenger():
#     choice = input(print('log in as manager - 1 or passenger - 2'))
#     while not choice.isdigit() or int(choice) < 0 or int(choice) > 2:
#         choice = input(print('log in as manager - 1 or passenger - 2'))
#     if int(choice) == 1 and is_manager():
#         return manager_menu()
#     elif choice == '2':
#
#         return passenger_menu()
#
#
# def is_manager():
#     counter = 0
#     while counter < 3:
#         password = input('password =')
#         if password == 'RideWithUs!':
#             return True
#         else:
#             counter += 1
#             print('wrong password', 3 - counter, 'tries remaining')
#     print('blocked')
#     return False
#
#
# def passenger_menu():
#     print('passenger menu')
#     option = input('what do you want to do?')
#     while not option.isnumeric() or not 0 < int(option) < 4:
#         option = input('what do you want to do?')
#     if option == '1':
#         search_route()
#     elif option == '2':
#         report_delay()
#     pass
#
#
# def manager_menu():
#     print('manager menu')
#     option = input('what do you want to do?')
#     while not option.isnumeric() or not 0 < int(option) <= 4:
#         option = input('what do you want to do?')
#     if option == '1':
#         classes.BestBusCompany.add_route()
#     elif option == '2':
#         classes.BestBusCompany.delete_route()
#     elif option == '3':
#         classes.BestBusCompany.update_route()
#     elif option == '4':
#         classes.ScheduledRide.add_scheduled_ride()
