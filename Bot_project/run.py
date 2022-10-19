from booking.booking import Booking

# teardown=True
with Booking() as bot:
    bot.land_first_page()
    bot.choose_currency(currency='KES')
    bot.select_destination('Nairobi')
    bot.select_dates(checkin='2022-10-14', checkout='2022-10-20')
    # bot.select_adults(10)
    bot.search_destination()
