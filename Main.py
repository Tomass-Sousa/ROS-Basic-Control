#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import sys
import select
import termios
import tty

# Commandes clavier et mapping vers Twist
key_bindings = {
    'z': (0.2, 0.0),    # avancer
    's': (-0.2, 0.0),   # reculer
    'q': (0.0, 0.5),    # tourner à gauche
    'd': (0.0, -0.5),   # tourner à droite
    ' ': (0.0, 0.0),    # arrêt
}

def get_key():
    """Lecture non bloquante d’une touche au clavier"""
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def move_robot():
    rospy.init_node('robot_controller', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    max_linear_speed = rospy.get_param('~max_linear_speed', 0.5)  # paramètre max vitesse linéaire
    max_angular_speed = rospy.get_param('~max_angular_speed', 1.0)  # max vitesse angulaire

    twist = Twist()

    rospy.loginfo("Contrôle du robot par clavier :")
    rospy.loginfo("z/s : avancer/reculer, q/d : tourner, espace : arrêt, Ctrl-C pour quitter")

    try:
        while not rospy.is_shutdown():
            key = get_key()
            if key in key_bindings:
                linear_vel, angular_vel = key_bindings[key]

                # Limiter les vitesses aux max configurés
                twist.linear.x = max(min(linear_vel, max_linear_speed), -max_linear_speed)
                twist.angular.z = max(min(angular_vel, max_angular_speed), -max_angular_speed)

                pub.publish(twist)

                rospy.loginfo(f"Commande reçue : linéaire={twist.linear.x:.2f} m/s, angulaire={twist.angular.z:.2f} rad/s")

            elif key == '\x03':  # Ctrl-C
                break

            rate.sleep()

    except rospy.ROSInterruptException:
        pass
    finally:
        # Arrêter le robot proprement
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        pub.publish(twist)
        rospy.loginfo("Arrêt du robot, fin du programme.")

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    move_robot()
