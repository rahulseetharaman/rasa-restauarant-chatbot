# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime,timedelta
from rasa_sdk.events import SlotSet



class ActionTellTime(Action):

    def name(self) -> Text:
        return "action_tell_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        now=datetime.now()
        duration=tracker.get_slot("duration")
        print(duration)
        numbers = [int(word) for word in duration.split() if word.isdigit()]
        print(numbers)
        if "hour" in duration:
            after=now+timedelta(hours=numbers[0])
        elif "minute" in duration:
            after=now+timedelta(minutes=numbers[0])
        elif "second" in duration:
            after=now+timedelta(seconds=numbers[0])
        else:
            dispatcher.utter_message(text="Invalid duration")
            return []
        dispatcher.utter_message(text=after.strftime("%H:%M:%S %p"))

        return []


class ActionOkay(Action):

    def name(self) -> Text:
        return "action_okay"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        rtype=tracker.get_slot("rtype")
        print(rtype)
        print(len(rtype))
        nums=tracker.get_slot("nums")
        if "alpha" in rtype:
            print("Coming")
            return [SlotSet("rtype","Simple")]
        elif "beta" in rtype:
            return [SlotSet("rtype","Deluxe")]
        else:
            return []
