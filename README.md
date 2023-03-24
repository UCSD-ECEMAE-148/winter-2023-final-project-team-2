[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/gpSYe2J3)
# Team 2 ECE/MAE 148 Final Report

## :wave: The Team: 2 Fast 2 Furious

![Team_photo](https://user-images.githubusercontent.com/75888027/227403474-61048822-09dd-433b-932b-de86ef46961f.jpg)

(Left to Right)
- Elias Fang (CSE)
- Ainesh Arumugam (ECE)
- Matthew Merioles (ECE)
- Junhao "Michael" Chen (MAE)


## 📝 Project Overview

Mario Kart in real-life? That's basically what we did. We designed a boost system similar to those in Mario Kart, where detecting colored pieces of paper on the track can change throttle for a short period of time. Depending on the color of the "pad" the car drives over, it will either speed up, slow down, or stop for a few seconds, just like in the game!

![Mario Kart](https://images7.alphacoders.com/821/thumb-1920-821837.jpg)

## 🏎 Our Robot

### Bird's Eye
![Top_view](https://user-images.githubusercontent.com/75888027/227403498-ec14b7c6-baf4-4aa7-a8bd-1ae51b82bc72.jpg)

### Front
![Front_view](https://user-images.githubusercontent.com/75888027/227403522-afdd695f-df96-4322-a394-93922a5811a3.jpg)

### Left
![Left_view](https://user-images.githubusercontent.com/75888027/227403532-8eb23acd-b959-4a8c-8ed9-3731ada305a2.jpg)

### Right
![Right_view](https://user-images.githubusercontent.com/75888027/227403561-73b25258-6376-4955-b1ee-34e0abd57fd8.jpg)

### Back
![Back_view](https://user-images.githubusercontent.com/75888027/227403556-8ad6b249-ec0e-4297-9e9e-726ceafe3b9f.jpg)

### Schematic
![Schematic](https://media.discordapp.net/attachments/1063289633087160320/1066623538372546632/image.png?width=980&height=492)


## 🍄 Final Project

### What We Promised

#### Must haves
[X] Distinguishing different colors through the camera

[X] Adjust the throttle based on the color

#### Nice to haves
[X] Have the car detect a flat piece of paper on the track (like a booster pad)

[ ] Combine with lane-following algorithm

### Gantt Chart
![image](https://user-images.githubusercontent.com/56064410/227400674-06957a98-4ea6-4810-ac88-8386b4b63dd2.png)
https://sharing.clickup.com/9010060626/g/h/8cgn7aj-87/769d44f22562beb

### What We Accomplished

#### Color Detection
- Used OpenCV for color detection and edge tracing
- Used color mask algorithm to detect proportion of frame that color takes up
- Detected multiple colors at the same time
- Determined HSVs for orange, pink, and blue

[Demo](https://youtu.be/FjuSYkTAjqk)

#### PyVESC
- Connection through external webcam
- Different RPM values are sent through PyVesc to achieve different speed for different colors marked by different states:
  - Blue (Boost) = speed up for 3 sec
  - Pink (Slow)= slow down for 3 sec
  - Orange (Stop) = stop for 3 sec
  - Neutral (Normal) = constant rpm

[Blue Demo](https://drive.google.com/file/d/1RUvbSz4l9gmOoFYbJw85eCSTo_RK-lXq/view?resourcekey)

[Pink Demo](https://youtu.be/r8XmqBMGC9A)

[Orange Demo](https://drive.google.com/file/d/1VssNhcCGHQDJhq6Y4HJ77vdUJ9ZV3Z5x/view?resourcekey)

### Presentation
https://docs.google.com/presentation/d/1oJPRLYIKvHUXEIK9hoYpPFoFAyHuG6sE7ZrU9NQPG8g/edit?usp=sharing

### Code
https://github.com/UCSD-ECEMAE-148/winter-2023-final-project-team-2/blob/main/MarioKart.py

### Possible Future Work
- Change the colored paper into Mario Kart items (mushroom, bananas, etc.) for the car to identify
- Allow the car to run autonomously on a track and still apply speed changes
- Race with other teams 😉


## 🏁 Autonomous Laps

[DonkeyCar](https://drive.google.com/file/d/12lLbkOE0VR50-O4KYxcbiw1VTY5s4e8l/view?usp=drivesdk)

[ROS2 Line Following](https://drive.google.com/file/d/10e9qd0lBde_-DVO0b2UsK-CHRWfg3vam/view?usp=drivesdk)

[ROS2 Lanes](https://drive.google.com/file/d/112mjOGJSfqOsfviWcJS7yKuZAAfUkezo/view?usp=drivesdk)

[GNSS]()


## Acknowledgements
Thanks for Professor Jack Silberman, TA Kishore Nukala, and Tutor Moises Lopez!
