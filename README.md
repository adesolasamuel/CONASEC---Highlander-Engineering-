# CONASEC---Highlander-Engineering-
Convenient and Secure Authentication system

# Inspiration
Every day human beings carry out research on improving their security, both physically and online. Sometimes maintaining security does come with lots of uneasiness and stress. This project is about providing easy access to security using a model of a gate or entrance system. In this project, an automatics car passage authentication is used, it can be extended to some other applications too.

# What it does

CONASEC provides facial recognition security for cars into a facility, it is an automatic gate lock system that uses biometrics for authentication.

## How we built it

CONASEC is built using Raspberry pi as a microprocessor. The main part of the application comprises the software and hardware components.

## The Hardware
In this illustration, a Raspberry Pi running Raspbian Operating System was used. A camera module that is attached to the Raspberry Pi is the main input into the system, it takes the facial picture of the driver and sends it to the Raspberry Pi for Machine Learning and Image Processing. The output or the actuator of the system is a servo motor, after authentication has been performed on the Raspberry Pi, it sends commands to the servo motor to open or stay closed depending on whether the person has access or not.

## The Software  

The system majorly runs on Machine Learning and Image Processing Technology, The device was trained with different images of people with access, and using the camera, the facial picture of the individual will be sent to the Raspberry pi for processing.

# Challenges we ran into
One of the major challenges ran into was setting up image processing on the Raspberry Pi. Due to compatibility, the OpenCV was installed using wheels.
Being a hardware project, another challenge ran into was setting up all external modules to directly work with the Raspberry Pi.

# Accomplishments that we're proud of

Being able to achieve this is an accomplishment I am proud of. Also, I was able to control an actuator depending on the input into the system which is a major demand in industrial machinery.

# What we learned

I learned how to work with the OpenCV image processing framework, I also learned how to train the Image Recognition model using the raspberry pi.

# What's next for EquityEngine

Enhancing the system to use Optical Character Reading (OCR) so the system can take text pictures as input and use them to control the actuator. This can make use of the car plate number to grant access to cars. 
