# Vehicle-Brake-Light-Detection-System

In the world of Autonomous vehicles the need for additional intelligence cannot be overemphasized. With more intelligence, autonomous vehicles would make better predictions needed for navigation. Human vehicle drivers can predict the actions of other drivers just by paying attention to vehicle lights. Vehicle lights are not just instruments of illumination. They function beyond that for good and experience drivers. How about we extending this abilities of paying attention to vehicle lights to autonomous vehicles.

There are different kinds of lights in a vehicle. These lights include;
* Head lights
* Tail lights
* Brake lights
* Daytime running lights
* Fog lights
* Signal Lights/ Trafficating lights
* Hazard lights

These lights all serve different purpose for a vehicle driver and in addition, it can be used as a means of communication to other road users. The goal of this project is to use computer vision to build a vehicle brake/tail light detection system, that would be able to identify when vehicles in front have these lights turned on.

Looking at vehicle brake light images, what one sees are dispersed red colors coming from a light fitting of different shapes and sizes. I would be focusing on the dispersed red lights and not the light fitting to build this detection system.

In building the detection system, the image is first, converted to HSV. The HSV_min and HSV_max that works for the brake light are gotten through a different set of codes. Masked HSV image is converted to gray image. Contours for the gray image is extracted and then converted to a rectangular bounding box. Bounding box within a define area size is retained as the best detector for the brake light. 

![vehicle brakelight detected images-1](https://user-images.githubusercontent.com/71301809/124341477-9bd5ac00-dbb4-11eb-80c6-5011a73af6f5.jpg)
