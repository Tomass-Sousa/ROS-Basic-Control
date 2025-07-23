# Contrôle de base d'un robot via ROS avec le clavier

---

## Description

Ce script Python permet la téléopération basique d’un robot en utilisant ROS (Robot Operating System).  
Il publie des commandes de vitesse (`geometry_msgs/Twist`) sur le topic `/cmd_vel` en fonction des touches pressées au clavier.

---

### Fonctionnalités

- Contrôle du robot en temps réel via le clavier :
  - **z** : avancer
  - **s** : reculer
  - **q** : tourner à gauche
  - **d** : tourner à droite
  - **espace** : arrêt immédiat
- Vitesses linéaire et angulaire maximales configurables via des paramètres ROS.
- Arrêt sécurisé du robot en cas d’interruption Ctrl+C.
- Retour console affichant les commandes de vitesse en cours.

---

## Prérequis

- ROS installé et correctement configuré (testé sur ROS Noetic, Melodic)
- Python 3
- Paquets Python ROS : `rospy`, `geometry_msgs`
- Terminal supportant l’entrée clavier en mode brut (Linux/macOS)

---

## Installation

1. Placez le script dans le dossier `scripts` de votre package ROS, par exemple `scripts/keyboard_control.py`.
2. Rendez le script exécutable :

```bash
chmod +x keyboard_control.py
```

3. Assurez-vous qu’un nœud abonné à /cmd_vel est en cours d’exécution (par exemple un pilote de robot ou un simulateur).

---

## Utilisation

1. Lancez le script avec:

```bash
rosrun <your_package_name> keyboard_control.py
```

2. Paramètres ROS optionnels :

~max_linear_speed (par défaut : 0.5) — vitesse linéaire maximale (m/s)
~max_angular_speed (par défaut : 1.0) — vitesse angulaire maximale (rad/s)

Exemple avec des vitesses personnalisées :

```bash
rosrun <your_package_name> keyboard_control.py _max_linear_speed:=1.0 _max_angular_speed:=2.0
```

---

## Commandes clavier

Touche	Action
Touche	Action
z	Avancer
s	Reculer
q	Tourner à gauche
d	Tourner à droite
Espace	Arrêt immédiat
Ctrl+C	Quitter le programme

---

## Remarques

Conçu pour les terminaux Linux/macOS en mode d’entrée brut. Le support pour Windows nécessite des modifications.
Assurez-vous que le ROS master est en cours d’exécution et que le robot ou simulateur est prêt à recevoir sur /cmd_vel.

---

## Example Output

Exemple de sortie
Téléopération du robot via le clavier :
z/s : avancer/reculer, q/d : tourner à gauche/droite, espace : arrêt, Ctrl-C pour quitter
Commande envoyée : linéaire = 0.30 m/s, angulaire = 0.00 rad/s
Commande envoyée : linéaire = 0.00 m/s, angulaire = 0.50 rad/s
Commande envoyée : linéaire = 0.00 m/s, angulaire = 0.00 rad/s
