## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later


## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent: book_room
- i would like to book a room
- i want a room
- i need rooms
- book some rooms
- have room

## intent: clean_room
- i want my room cleaned
- my room needs a wash
- my room needs a cleaning
- some cleaning is to be done
- dust my room
- could you send a cleaner up here
- clean my room
- i want it done right
- i would like my room to be cleaned
- i want my room to be cleaned



## intent: clean_room_immediately
- i want it done right now
- i would prefer immediately
- want it done right away
- i would like my room to be cleaned right away
- i want my room to be cleaned now
- clean my room now

## intent: schedule_time_to_clean
- i want it done [2 minutes](duration) later
- i prefer it [3 hours](duration) afterwards
- i would like it to be [4 hours](duration) later
- [5 days](duration) later
- [6 minutes](duration) afterwards
- [30 minutes](duration) from now
- after [2 hours](duration)
- after [1 minute](duration)
- [13 hours](duration) later
- i want to clean my room [2 minutes](duration) later
- i prefer to clean my room [3 hours](duration) afterwards
- i need my room to be cleaned [4 hours](duration) from now



## intent: tell_num_rooms
- [3](nums) rooms
- i would like [4](nums)
- prefer [3](nums)
- prefer [2](nums)
- would like [3](nums)
- [4](nums) rooms
- book a [2](nums) room
- i prefer a [5](nums) room
- i need you to book a [7](nums) room
- i need you to book the [9](nums) one
- would like to make a booking for [2](nums) rooms

## intent: tell_simple_deluxe
- (simple)[rtype] room
- (deluxe)[rtype] room
- [simple](rtype)
- [deluxe](rtype)
- i want [simple](rtype)
- i need [deluxe](rtype)
- book a [deluxe](rtype) room
- i prefer a [simple](rtype) room
- i need you to book a [simple](rtype) room
- i need you to book the [simple](rtype) one
- would like to make a [deluxe](rtype) booking

## intent: room_all_details
- [2](nums) [simple](rtype) rooms
- would like to make [2](nums) [deluxe](rtype) bookings
- book [3](nums) [simple](rtype) rooms
- want [simple](rtype) [3](nums)
- would like [2](nums) [deluxe](rtype) booking 
- book [2](nums) rooms of [deluxe](rtype)
- are there [2](nums) [deluxe](rtype) rooms available ?
- want to book [3](nums) [deluxe](rtype) rooms
- availability of [2](nums) [deluxe](rtype) rooms

## intent: ask_check_in_timings
- what are your check in timings
- what time do I have to check in
- what time to come to check in counter
- when do you expect me to check in
- when do I check in
- Time to check in ?

## intent: ask_check_out_timings
- what time do I have to check out
- what time to come to check out counter
- when do you expect me to check out
- when do you expect me to checkout
- when do I check out
- when do I checkout
- Time to check out ?
- what are your checkout timings
- what are your check out timings

## intent: ask_cancellation_policy
- what is your cancellation policy ?
- what policy do you follow for cancelling ?
- what policy is followed for cancellation ?
- know about cancellations

## intent: ask_restaurant
- is there a place to eat
- is there a place to have [food_type] ?
- where can I get [food_type] ?
- does the [restro] have a [restro] ?
- is there a [restro] where I can have food ?
- is there a [restro] where I can eat ?


## lookup: food_type
- breakfast
- lunch
- meals
- food
- brunch
- dinner

## lookup: restro
- bistro
- restaurant
- pizzeria
- hotel
- restaurant

## intent: ask_breakfast_timings
- does the [restro] offer breakfast ?
- time in the morning I can get food ?
- when to order breakfast ?
- when to get food in the morning ?
- when does the [restro] offer breakfast ?
- when does the [restro] offer food in the morning ?
- what time is food available in the morning ?
- what time is breakfast available ?
- when can I get breakfast ?
- know the breakfast timings.
- know when can I order breakfast.
- know when to order food in the morning.
- know the timings for breakfast.
- know when I will get breakfast.


## intent: ask_breakfast_availability
- is there breakfast available ?
- is there food in the morning ?
- can I get breakfast ?
- can I order breakfast ?
- can I order food in the morning ?
- does the [restro] offer food in the morning ?

## intent: ask_restaurant_timings
- till what time is the [restro] open
- what are the [restro] timings
- when does the [restro] close
- when does the [restro] open
- what time does the [restro] open 

## intent: ask_to_cancel
- cancel my reservation
- i need to cancel my booking
- cancel my room
- i have to cancel my booking