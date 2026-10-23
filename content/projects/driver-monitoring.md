---
slug: driver-monitoring
title: From facial landmarks to timed observations.
summary: A webcam prototype combining pretrained vision, geometry and temporal logic.
category: vision
kind: Computer vision prototype
period: Current portfolio
role: Vision integration & state-based monitoring
tools:
- Python
- OpenCV
- MediaPipe
- NumPy
order: 50
image: assets/images/vision.svg
image_alt: From facial landmarks to timed observations. — explanatory diagram
image_caption: Explanatory schematic created for this portfolio; not a photograph,
  application screenshot or measured output.
featured: false
draft: false
sources:
- label: Implementation, tests and safety limitations
  url: https://github.com/aravindsudheer01-arch/driver-monitoring-system
repository: https://github.com/aravindsudheer01-arch/driver-monitoring-system
---

## The problem
A single image does not explain whether eye closure or a head movement persists. This project explores how webcam landmarks and time-based logic can distinguish brief events from sustained observations.

## My contribution
I built a Python prototype around pretrained MediaPipe facial landmarks, OpenCV webcam processing, eye and mouth geometry, timed monitoring states and audible alerts. Geometry, tracking state, head-pose estimation and sound handling are separated into modules.

## Technical approach
Eye aspect ratio and a mouth-opening ratio feed temporal monitoring logic. The application counts detected blink events and tracks sustained eye closure and possible yawning events.

For head pose, six 2D landmarks are matched to a generic 3D face template through OpenCV `solvePnP`. A neutral reference and temporal filtering distinguish brief motion from sustained deviations. An eye-closure observation can be combined with a head-pose observation, without treating a head turn alone as sleep.

## Results & evidence
The public repository contains synthetic geometry and timestamp-based state tests, a model-download helper and documented webcam setup. The README reports local webcam checks on an Intel MacBook. These are development checks, not measured accuracy or real-driving validation.

The illustration above explains landmark geometry. It is not a captured frame, a biometric recording or a validated detection result.

## Limitations & safe use
**Educational prototype only. Test while stationary, never as a driving aid.** It is not an automotive safety system or a medical assessment.

Camera intrinsics are approximated and the 3D face template is generic. Lighting, glasses, occlusion, frame rate and facial geometry affect the measurements. Heuristic labels cannot confirm fatigue, sleep or a medical condition.

This project integrates a pretrained model; it does not train a facial-landmark detector. Synthetic tests establish behavior under their inputs, not sensitivity, specificity or reliability across people and environments.
