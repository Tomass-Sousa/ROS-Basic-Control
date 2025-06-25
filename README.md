# Basic Robot Control via ROS with Keyboard Input

## Description

This Python script allows basic teleoperation of a robot using ROS (Robot Operating System).  
It publishes velocity commands (`geometry_msgs/Twist`) on the `/cmd_vel` topic based on keyboard inputs.

### Features

- Real-time robot control via keyboard:
  - **z**: move forward
  - **s**: move backward
  - **q**: turn left
  - **d**: turn right
  - **space**: stop immediately
- Configurable maximum linear and angular speeds through ROS parameters.
- Graceful shutdown with safe robot stop on Ctrl+C interrupt.
- Console feedback showing current velocity commands.

---

## Prerequisites

- ROS installed and properly configured (tested on ROS Noetic, Melodic)
- Python 3
- ROS Python packages: `rospy`, `geometry_msgs`
- Terminal supporting raw keyboard input (Linux/macOS)

---

## Installation

1. Place the script in your ROS package `scripts` directory, e.g., `scripts/keyboard_control.py`.
2. Make it executable:

```bash
chmod +x keyboard_control.py
```

3. Ensure a node subscribing to /cmd_vel is running (e.g., robot driver or simulator).

## Usage

1. Run the script using:

```bash
rosrun <your_package_name> keyboard_control.py
```

2. Optional ROS parameters

~max_linear_speed (default: 0.5) — max linear velocity (m/s)
~max_angular_speed (default: 1.0) — max angular velocity (rad/s)

Example with custom speeds:

```bash
rosrun <your_package_name> keyboard_control.py _max_linear_speed:=1.0 _max_angular_speed:=2.0
```

## Keyboard Controls

Key	Action
z	Move forward
s	Move backward
q	Turn left
d	Turn right
Space	Stop immediately
Ctrl+C	Exit program

## Notes

Designed for Linux/macOS terminals with raw input mode. Windows support requires modification.
Make sure ROS master is running and the robot or simulator is ready to receive /cmd_vel.

## Example Output

Robot teleoperation via keyboard:
z/s: forward/backward, q/d: turn left/right, space: stop, Ctrl-C to quit
Command sent: linear=0.30 m/s, angular=0.00 rad/s
Command sent: linear=0.00 m/s, angular=0.50 rad/s
Command sent: linear=0.00 m/s, angular=0.00 rad/s
