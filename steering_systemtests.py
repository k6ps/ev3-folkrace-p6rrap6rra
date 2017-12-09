#!/usr/bin/python3

import logging
import time
from steering import Steering

logging.basicConfig(format='%(asctime)s %(message)s', filename='steering_systemtest.log', level=logging.DEBUG)


if __name__ == "__main__":
    logging.info('Steering system test: starting')
    steering = Steering(
        steering_motor_address='outC',
        steering_motor_speed_factor=10,
        steering_speed=5,
        steering_max_range=35,
        steering_motor_position_factor=-1
    )

    logging.info('=== Steering system test: Initialize ===')
    steering.initialize()
    logging.info('Steering system test: steering position = ' + str(steering.get_current_steering_position()))
    time.sleep(1)

    logging.info('=== Steering system test: turn to 100% left ===')
    steering.set_steering_position(-100)
    logging.info('Steering system test: steering position = ' + str(steering.get_current_steering_position()))
    logging.info('Steering system test: steering motor state = ' + str(steering.steering_motor.state))
    time.sleep(1)

    logging.info('=== Steering system test: turn to 50% right ===')
    steering.set_steering_position(50)
    logging.info('Steering system test: steering position = ' + str(steering.get_current_steering_position()))
    logging.info('Steering system test: steering motor state = ' + str(steering.steering_motor.state))
    time.sleep(1)

    logging.info('=== Steering system test: turn to 100% right ===')
    steering.set_steering_position(100)
    logging.info('Steering system test: steering position = ' + str(steering.get_current_steering_position()))
    logging.info('Steering system test: steering motor state = ' + str(steering.steering_motor.state))
    time.sleep(1)

    logging.info('=== Steering system test: turn to 50% left: ===')
    steering.set_steering_position(-50)
    logging.info('Steering system test: steering position = ' + str(steering.get_current_steering_position()))
    logging.info('Steering system test: steering motor state = ' + str(steering.steering_motor.state))
    time.sleep(1)

    logging.info('=== Steering system test: turn to center: ===')
    steering.set_steering_position(0)
    logging.info('Steering system test: steering position = ' + str(steering.get_current_steering_position()))
    logging.info('Steering system test: steering motor state = ' + str(steering.steering_motor.state))
    time.sleep(1)

    logging.info('Steering system test: ending')

