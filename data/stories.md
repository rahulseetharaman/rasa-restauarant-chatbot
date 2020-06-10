## book room path 1
* greet
  - utter_greet
* book_room
  - utter_ask_num_rooms
* tell_num_rooms
  <!-- - utter_ask_simple_deluxe -->
  - utter_with_button
<!-- * tell_simple_deluxe -->
* select_room_type
  - action_okay
  - utter_okay


## book room path 2
* greet
  - utter_greet
<!-- * tell_simple_deluxe -->
* select_room_type
  - utter_ask_num_rooms
* tell_num_rooms
  - action_okay
  - utter_okay

## book room path 3
* greet
  - utter_greet
* tell_num_rooms
  <!-- - utter_ask_simple_deluxe -->
  - utter_with_button
<!-- * tell_simple_deluxe -->
* select_room_type
  - action_okay
  - utter_okay

## book room path 4
* greet
  - utter_greet
* room_all_details
  - action_okay
  - utter_okay

## book room path 5
* greet
 - utter_greet
* tell_simple_deluxe
 - utter_ask_num_rooms
* tell_num_rooms
 - action_okay
 - utter_okay

## clean room path 1
* greet
  - utter_greet
* clean_room
  - utter_ask_time
* clean_room_immediately
  - utter_sending_someone

## clean room path 2
* greet
  - utter_greet
* clean_room
  - utter_ask_time
* schedule_time_to_clean
  - utter_time_to_clean 
  - action_tell_time

## clean room path 3
* greet
  - utter_greet
* schedule_time_to_clean
  - utter_time_to_clean
  - action_tell_time

## clean room path 4
* greet
  - utter_greet
* clean_room_immediately
  - utter_sending_someone

## check in path 1
* greet
  - utter_greet
* ask_check_in_timings
  - utter_check_in_timings

## check out path 1
* greet
  - utter_greet
* ask_check_out_timings
  - utter_check_out_timings


## check out path 1
* greet
  - utter_greet
* ask_cancellation_policy
  - utter_cancellation_policy

## restaurant path 1
* greet
  - utter_greet
* ask_restaurant
  - utter_restaurant


## breakfast timings
* greet
  - utter_greet
* ask_breakfast_timings
  - utter_breakfast_timings

## breafast availability
* greet
  - utter_greet
* ask_breakfast_availability
  - utter_breakfast_availability

## restaurant timings
* greet
 - utter_greet
* ask_restaurant_timings
 - utter_restaurant_timings


## cancellation
* greet
 - utter_greet
* ask_to_cancel
 - utter_ask_to_cancel

## bot challenge
* bot_challenge
  - utter_iamabot
