# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import webbrowser



class ActionVideo(Action):
    def name(self) -> Text:
        return "action_video"


    async def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        video_url = "https://youtu.be/HIj8wU_rGIU"
        dispatcher.utter_message("wait... playing your video")
        webbrowser.open(video_url)
        return []


class ValidateResponse(Action):
    def name(self) -> Text:
        return "user_details_form"
    
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
     ) -> List[EventType]:
        required_slots = ["name", "email"]

        for slot_name in required_slots:
            if tracker.slot.get(slot_name) is None:
                return [SlotSet("requested_slot", slot_name)]
        
        return [SlotSet("requested_slot", None)]


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template= "utter_details_thanks", Name = tracker.get_slot("name"), Email = tracker.get_slot("email"))