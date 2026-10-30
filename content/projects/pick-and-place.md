---
slug: pick-and-place
title: Autonomous Pick-and-Place Robot — Mechanical Design & Integration
summary: >-
  A three-person robotics project in which I led SOLIDWORKS CAD and gripper development,
  coordinated 3D-printed parts and supported hardware-software integration and testing.
category: engineering
kind: Academic team project
period: Aug 2024 — Nov 2024
role: Primary Mechanical Engineer · Software integration support
tools:
  - SOLIDWORKS
  - 3D printing
  - Mechanical CAD
  - Servo-actuated gripper
  - PSoC 5LP
  - Sensor integration
  - Motion testing
order: 80
image: assets/images/pick-place-robot-build.webp
image_alt: "Two original photographs of the completed team's puck-handling robot, shown with its yellow outer casing and with sensors and wiring exposed."
image_caption: "Completed robot with and without its casing. Original photographs from Group 11's ECE4191 final report, page 14."
featured: false
draft: false
gallery:
  - src: assets/images/pick-place-cad-isometric.webp
    alt: "Annotated SOLIDWORKS isometric model of the robot, showing its battery holders, sensor layout, wheels and puck gripper."
    caption: "Annotated isometric CAD model of the integrated robot. Mechanical design and CAD were my primary responsibility (report p. 15)."
  - src: assets/images/pick-place-gripper-cad.webp
    alt: "Original SOLIDWORKS rendering of the dark circular puck gripper with its two-pronged actuation mechanism."
    caption: "Servo-driven gripper design used for grasping, lifting and releasing coloured pucks (report p. 21)."
  - src: assets/images/pick-place-robot-chassis.webp
    alt: "Actual assembled underside of the robot showing the two powered wheels, sensor hardware, wiring and caster supports."
    caption: "Physical underside and component integration of the robot built by our team (report p. 13)."
  - src: assets/images/pick-place-cad-bottom.webp
    alt: "Annotated SOLIDWORKS underside view identifying the gripper, funnels, colour sensor, motor with encoder and caster balls."
    caption: "Bottom-view CAD detailing puck guides, wheel layout, gripper and sensor placement (report p. 16)."
sources:
  - label: Project evidence
    note: "ECE4191 Engineering Integrated Design final report (Group 11, 2024), sections 1–2, 4, 6–8. Robot photographs and CAD images are original figures from the group report, credited as collaborative student work. The complete report is not public."
---

## The challenge

Our three-person ECE4191 team developed an autonomous robot for a timed arena challenge: identify coloured pucks, collect and transport them, and arrange them into prescribed geometric patterns. The design had to fit inside a **30 × 30 cm** starting footprint, work within a **RM320 project budget**, and accommodate an opposing robot and moving obstacles. The competition's round limit was **12 minutes**; this was a design constraint, not our measured completion time.

## My role: primary mechanical engineer

I was the team's **Primary Mechanical Engineer**, responsible for completing and finalising the **SOLIDWORKS CAD**, particularly the mechanical puck gripper, and coordinating the **3D printing** required for our custom parts. I also took part in assembling the physical mechanism and integrating it with the rest of the robot.

The overall chassis, locomotion, sensing, electronics and control system were developed **collaboratively**. My lead contribution was the mechanical design, rather than sole ownership of the robot or its firmware.

## Mechanical design decisions

The robot used a **two-deck acrylic chassis** to fit electronics and actuators into the footprint while keeping the structure light and accessible. Two central drive wheels and supporting caster balls enabled compact turning. The team compared gearbox configurations and chose a **38.2:1** ratio to balance movement speed and usable torque.

The puck-manipulation mechanism was central to my CAD work. It used **servo-actuated lifting and gripping**, including interlocking gears to open and close the gripper and compliant material to help hold a puck. We also designed **3D-printed guide funnels** underneath the chassis to channel pucks toward the colour sensor and away from the wheels.

This was an iterative physical design: grip force, servo load, component clearance, mass distribution and manufacturability all affected whether the mechanism worked in the arena.

## How I helped on the software side

Although I was **not the primary firmware engineer**, I supported the team with **hardware-software integration, motion testing and debugging**, including the interaction between the gripper, actuators, sensors and the robot's movement routines.

The team's control system used a **PSoC 5LP** microcontroller, shaft-encoder feedback, ultrasonic obstacle sensing, IR puck detection, colour sensing and servo control. Testing the physical mechanism alongside the control logic helped us identify where seemingly correct commands did not translate into reliable movement or puck handling.

My contribution was collaborative integration and testing; the main control algorithms and firmware were led by a teammate.

## What the team achieved

We progressed from CAD and component selection to a physically assembled, autonomous prototype. According to the group report, the team **completed Level 1 during the final competition**, although the broader two-level task still had unresolved reliability challenges. No competition rank or verified overall completion-time benchmark is claimed.

The report records **RM240.48** in final project expenditure versus **RM302.94** initially proposed, within the **RM320** competition cap. These figures describe the team's documented spending, not a personal saving attributable to me alone.

## Limitations and improvements

The final report identifies persistent alignment difficulties in the patterning zone, colour-sensor mounting issues, gripper slippage during some movements and the power demands of multiple ultrasonic sensors. Completing one competition level did not mean every objective was fully or reliably solved.

Further work would improve the sensor holder, grip mechanism and motion/alignment strategy, then verify their performance through repeatable tests. There is no claim here of a perfect autonomous success rate or ownership of all the software.

## Team attribution

This was a **three-person Monash University project**. Photographs and CAD figures are extracted from our group-authored final report. I am highlighting the mechanical design work I led and the software-integration support I personally contributed, while crediting the full team for the completed robot.
