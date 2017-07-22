#!/bin/bash

PROJECT_NAME=ev3-folkrace-p6rrap6rra
EV3_HOST=ev3dev.local
EV3_USER=robot
EV3_USER_HOST=$EV3_USER@$EV3_HOST
EV3_HOME_DIR=/home/$EV3_USER
EV3_PROJECT_DIR=$EV3_HOME_DIR/$PROJECT_NAME

# Create remode project directory if it does not exist.
# This prompts for password.
ssh $EV3_USER_HOST "mkdir -p $EV3_PROJECT_DIR"
if [ $? -eq 0 ]
then
  echo "== Successfully created remote project directory in EV3 brick (if it did not exist) =="
else
  echo "== !! Failed to create remote project directory in EV3 brick !!==" >&2
  exit 1
fi

# Copy all non-test Python files to the project folder in EV3 brick. 
# This prompts for password again.
scp ./*.py $EV3_USER_HOST:$EV3_PROJECT_DIR
if [ $? -eq 0 ]
then
  echo "== Successfully copied program files to project directory in EV3 brick =="
else
  echo "== !! Failed to copy program files to project directory in EV3 brick !!==" >&2
  exit 1
fi

