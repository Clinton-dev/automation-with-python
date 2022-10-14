from booking.booking import Booking

# teardown=True
with Booking() as bot:
    bot.land_first_page()
    # bot.choose_currency(currency='KES')
