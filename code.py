# Patrick McCorkell
# April 2022
# US Naval Academy
# Robotics and Control TSD
#


print("Hello " + __name__)

from music import Music
from pingpong import Pingpong
import atexit

lab = Pingpong()



###################################
########## Notes to Self ##########
###################################
###################################

# sensor		21888	at bottom

# pwm		0.266	when it can maintain a current (~ 50 mA)






###################################
####### Example Controllers #######
###################################
###################################

# error = 0
# last_error = 0
# i_term = 0
# # @tictoc
# def control_loop_P():
# 	global pid, target_speed, error, last_error
# 	quanser_305.encoder_loop()
# 	error = target_speed - (quanser_305.get_dx() / quanser_305.get_dt())
# 	p_term = pid['Kp'] * error
# 	last_error = error
# 	# print('p: '+str(p_term)+', i: '+str(0)+', d: '+str(0)+', err: '+str(error))
# 	quanser_305.digipot.set_pot(bias + p_term)

# # @tictoc
# def control_loop_PI():
# 	global pid, target_speed, error, last_error, i_term
# 	quanser_305.encoder_loop()
# 	dt = quanser_305.get_dt()
# 	error = target_speed - (quanser_305.get_dx() / dt)
# 	p_term = pid['Kp'] * error
# 	i_term += (pid['Ki'] * error * dt)
# 	last_error = error
# 	# print('p: '+str(p_term)+', i: '+str(i_term)+', d: '+str(0)+', err: '+str(error))
# 	quanser_305.digipot.set_pot(bias + p_term + i_term)

# # @tictoc
# def control_loop_PID():
# 	global pid, target_speed, error, last_error, i_term
# 	quanser_305.encoder_loop()
# 	dt = quanser_305.get_dt()
# 	error = target_speed - (quanser_305.get_dx() / dt)
# 	p_term = pid['Kp'] * error
# 	i_term += pid['Ki'] * error * dt
# 	d_term = pid['Kd'] * (error - last_error) / dt
# 	# print('p: '+str(p_term)+', i: '+str(i_term)+', d: '+str(d_term)+', err: '+str(error))
# 	quanser_305.digipot.set_pot((bias + p_term + i_term + d_term))
# 	last_error = error



###################################
##### Control the Controllers #####
###################################
###################################

# controller_func_name = control_loop_PID
# time_limit = 1
# controller_rate = 0.00005
# target_pos = (10 / tau) * encoder_counts_per_rev / 10**9		# 10 rad/s
# bias = 20/511
# sample_offset = 2	# Change how many samples away to get dx and dt.
# 					# ie,	last sample is 100th pair of position and time.
# 					# 		If set to 1, compares that to the 99th entry.
# 					#		To compare against 98th entry, set this to 2.
# pid = {
# 	'Kp' : 0.00003 * 10**9,
# 	'Ki' : 0.0004,
# 	'Kd' : 0.00000001  * 10**18
# }


# def runit():
# 	# quanser_305.auto_control()
# 	global controller_rate, time_limit, controller_func_name, target_speed, sample_offset
# 	quanser_305.change_sample_offset(sample_offset)
# 	quanser_305.attach_controller(controller_func_name, controller_rate, time_limit)
# 	quanser_305.run_controller()
# 	print("LOG: final err: %0.2f%%" %(100 * last_error / target_speed))
# 	sleep(1)



###################################
######## Reset and Program ########
########## Exit Section ###########
###################################

def reset():
	import microcontroller
	microcontroller.reset()

intro = 0
def exit_program():
	if (str(type(intro))=="<class 'Music'>" ):
		intro.deinit_all()
	lab.set_pwm(0)
	lab.deinit_all()
	# print('LOG: exiting program')

atexit.register(exit_program)



###################################
######## Startup Section ##########
###################################
###################################

if __name__ == '__main__':
	intro = Music(pass_pwm=lab.mosfet,auto=True)
	lab.tsd_profile_characteristics()

if __name__ == 'code':
	intro = Music(pass_pwm=lab.mosfet,auto=True)
	lab.tsd_profile_characteristics()
