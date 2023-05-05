
import control_functions
from control_functions import *

ACTION_LOOKUP = {
	# Unadded yet:

	#15: "write_text",
	# 27: "close_app",
	# open_finder
	# open_app
	# close_app
	# dark_mode
	# clean_trash
	8: 'display_text (sign: medicine)',
	5: 'open_netflix (sign: movie)',
	# write_text
	18: 'open_booking (sign: hotel)',
	19: 'open_youtube (sign: theater)',
	14: 'open_email (sign: email)',

	# Most consistantly classified funcs:
	# 22: "Check Weather (gloss: Weather)" , 
	# 0 : "Open Browser (gloss: Open)",
	# 0 : "Open Twitter (sign: Bird)",
	# 66 : "Dark Mode (gloss: Dark)",
	
	# less consistantly classfified 
	# 13 : "Volume Up (gloss: Loud)",
	# 68 : "Volume Down (gloss: Down)",
	# 6 : "Mute (sign: quiet)",
	# not totally working
	# 4 : "Quit (gloss: Cancel)", 

	# no mapping function yet: 
	20 : "Take Screenshot (sign: camera)", 
	# 101 : "Take Picture",
}

class LogicHandler:

	def __init__(self):
		
		self.input_state = None
		self.action_log = []


	def model_to_command(self, model_result: list):
		"""
		Called in app.py to pass model output to logic handler. 
		
		Checks to see if the result of the model is an action, and calls action_stream_handler to process action
		"""
		#gloss = model_result
		self.input_state = None
		for label in model_result:
			if label in ACTION_LOOKUP:
				self.input_state = ACTION_LOOKUP[label] 
				print("INPUT STATE: ", self.input_state)
				self.action_stream_handler(self.action_log)
				break


	#processes running list of actions into corresponding functions. TODO: Use Stream optimal logic
	def action_stream_handler(self, action_log):
		"""
		Calls the proper control function based on the input_state. 
		"""

		cur_action = self.input_state
		
		if cur_action == "Mute (sign: quiet)":
			control_functions.mute()

		if cur_action == 'open_email (sign: email)':
			control_functions.open_email()

		if cur_action == "open_youtube (sign: theater)":
			control_functions.open_youtube()

		if cur_action == "open_netflix (sign: movie)":
			control_functions.open_netflix()
		
		if cur_action == "open_booking (sign: hotel)":
			control_functions.open_booking()

		if cur_action == "Take Picture":
			control_functions.take_picture()

		if cur_action == "Take Screenshot":
			control_functions.screenshot()
		
		if cur_action == "Check Weather (gloss: Weather)":
			control_functions.check_weather()

		if cur_action == "Open Browser (gloss: Open)":
			control_functions.open_browser()

		if cur_action == "Open Twitter (sign: Bird)":
			control_functions.open_twitter()
		
		if cur_action == "Dark Mode (gloss: Dark)":
			control_functions.dark_mode()

		if cur_action == "Volume Up / Loud":
			control_functions.volume(direction="UP")

		if cur_action == "Volume Down (gloss: Down)":
			control_functions.volume(direction="DOWN")

		if cur_action == "Quit (gloss: Cancel)":
			control_functions.cancel()
        
		# unadded yet:

		if cur_action == "open_finder":
			control_functions.open_finder()

		if cur_action == "open_app":
			control_functions.open_app()
		
		if cur_action == "close_app":
			control_functions.close_app()

		if cur_action == "dark_mode":
			control_functions.dark_mode()
		
		if cur_action == "clean_trash":
			control_functions.clean_trash()

		if cur_action == "display_text (sign: medicine)":
			control_functions.display_text()
		
		if cur_action == "write_text":
			control_functions.write_text()
		
		if cur_action == "Take Screenshot (sign: camera)":
			control_functions.screenshot()
		
		
		action_log.append(cur_action)
	
	def get_commands(self):
		# return slider_state+input_state
		return self.input_state

