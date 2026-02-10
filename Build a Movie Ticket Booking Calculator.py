def movie_ticket (base_price: int, age: int, seat_type: str,
show_time:str) -> str:
    r"""Function to book movie tickets
    
    <description>

    Parameters
    ----------
    base_price : int
        The base price of the movie ticket.
    age : int
        The age of the person booking movie ticket.
    seat_type : str
        The Seat type the person needs either Gold or Platinum.
    show_time : str
        The show timing of movie either Morning or Evening.
    
    Returns
    -------
    str
        The final price of movie ticket.
        
    """


    ret_str = ''
    if age > 17:
        ret_str+='User is eligible to book a ticket'

    if age >= 21:
        ret_str('User is eligible for Evening shows')
    else:
        ret_str('User is not eligible for Evening shows')

    is_member = False
    is_weekend = False

    discount = 0
    if is_member and age >= 21:
        discount = 3
        ret_str('User qualifies for membership discount')
    else:
        ret_str('User does not qualify for membership discount')
        ret_str('Discount:', discount)

    extra_charges = 0
    if is_weekend or show_time == 'Evening':
        extra_charges = 2
        ret_str('Extra charges will be applied')
    else:
        ret_str('No extra charges will be applied')
    ret_str('Extra charges:', extra_charges)

    if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
        ret_str('Ticket booking condition satisfied')

        service_charges = 0
        if seat_type == 'Premium':
            service_charges = 5
        elif seat_type == 'Gold':
            service_charges = 3
        else:
            service_charges = 1
        ret_str('Service charges:', service_charges)

        final_price=service_charges+extra_charges+base_price-discount
        ret_str("Final price of ticket:",final_price)    
    else:
        ret_str('Ticket booking failed due to restrictions')
    
    return ret_str
