# Mindstorms EV3 Track Racer

## About This Project

This is software for a self-driving track racer ("folkracer") robot, written for robot built with [LEGO Mindstorms EV3](https://www.lego.com/mindstorms "LEGO Mindstorms EV3") platform, using visual programming with the LEGO Mindstorms original development environment.

Unfortunately the .ev3 file is binary, so i cannot really track changes with Git. However, i can still at least track revisions and versions.

My folkracer was participating in [Robotex](http://www.robotex.ee "Robotex") 2016 ans 2017 in Tallinn, Estonia - one of the biggest robotics events in the world, as they claim. Here is a (very long) video of the Folkrace competition: (https://www.youtube.com/watch?v=ysx26ghvYus)  Now i'm buildig an improved version for 2018.

The module names, comments, and variables in this program are in Estonian language - sorry for that. I originally did this together with my kids, so it would be easier for them to understand. Now we have another simplier version of the program for a bit simplier robot design (one motor per each wheel, no steering, no gyro) with kids. So, i'm rewriting this in Python on top of [EV3Dev](http://www.ev3dev.org "EV3Dev").

## Current Status

The EV3 program (FolkraceRobot.ev3) is more or less done. It has a few issues. I am not currently actively developing it.

The new Python program is not competition-ready yet. My current task is to get it driving seamlessly on a track, using PID controller for EV3 medium motor for steering the front wheels. Next tasks will be about avoiding various obstacles.