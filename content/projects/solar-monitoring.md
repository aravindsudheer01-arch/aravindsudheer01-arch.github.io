---
slug: solar-monitoring
title: Designing a brand-independent solar monitoring RTU.
summary: Two ESP32-based remote terminal units connect solar measurements, industrial protocols and 4G cloud telemetry in an industry-guided final-year project.
category: engineering
kind: Industry-guided final-year project
period: Aug 2024 — Jun 2025
role: Embedded IoT integration and system validation
tools:
  - ESP32
  - Modbus RTU
  - RS-485
  - ESP-NOW
  - Embedded C/C++
  - SIM7600 4G
  - Blynk
  - Electrical validation
order: 40
image: assets/images/fyp-solar-architecture.jpg
image_alt: Original system architecture figure from the final-year report showing solar panel, charge controller, inverter, two RTUs, meter and cloud connection.
image_caption: Original hardware architecture from the ENG4702 final report, page 13. Designed for a brand-independent interface; cross-brand compatibility was not validated.
featured: true
draft: false
gallery:
  - src: assets/images/fyp-solar-backplate.jpg
    alt: Prototype backplate with EPEVER MPPT controller, inverter, energy meter, emergency stop and two RTU boards arranged in the workshop.
    caption: Workshop arrangement and wiring of the electrical components before rooftop installation (report p. 21).
  - src: assets/images/fyp-solar-rooftop.jpg
    alt: Photographs of the solar monitoring enclosure and installed RTU boards during rooftop field testing.
    caption: Rooftop-mounted enclosure and installed monitoring hardware during field trials (report p. 22).
  - src: assets/images/fyp-solar-rtu-boards.jpg
    alt: Close-up photographs of the before-inverter and after-inverter ESP32 RTU prototypes.
    caption: "The two physical RTUs: DC-side acquisition and AC-side aggregation with cellular communication (report p. 22)."
  - src: assets/images/fyp-solar-blynk-dashboard.jpg
    alt: Actual Blynk dashboard screenshots with separate DC and AC gauges and time-series plots.
    caption: Blynk monitoring displays recorded during testing; gauges and trend plots are original report screenshots (report p. 24).
sources:
  - label: Final-year report
    note: "Aravind Sudheer, IoT Integrated Solar Monitoring System, ENG4702 final report, submitted 27 May 2025, especially pp. 13 and 18–31. Selected figures reproduced from the author's report; the full report and code appendix are not public."
---

## The problem

Off-grid solar systems often come with vendor-specific monitoring apps and inconsistent access to electrical measurements. For a rural school or remote operator, switching between dashboards makes troubleshooting unnecessarily difficult. My project explored a **modular remote terminal unit (RTU)** that gathers measurements from the installation and presents them through one monitoring interface.

This was a **final-year engineering consultancy project**, completed with guidance from a professional engineer at Aiszzy Electronics. Its intended application was off-grid solar monitoring; it was **not** a commercial rollout to rural schools.

## My contribution

I worked across the hardware-to-cloud integration process: planning the architecture, assembling and wiring the prototype, integrating ESP32 communication and sensing, setting up the monitoring workflow, and validating the assembled system on the university rooftop.

The project also involved physical layout decisions for cable routing, service access and component spacing; continuity and insulation checks; PCB revisions prompted by localized heating; stakeholder coordination; and project risk assessment. I collaborated with an industry engineer on the hardware and practical engineering constraints rather than treating the work as an isolated software exercise.

## System architecture

The design used **two ESP32-based RTUs** so that both DC-side and AC-side information could be monitored:

1. **Before-inverter RTU:** Polled the EPEVER MPPT solar charge controller using **Modbus RTU over RS-485**, including PV and battery measurements.
2. **Local wireless link:** Transferred DC-side measurements to the second RTU using **ESP-NOW**.
3. **After-inverter RTU:** Combined the received measurements with an **SDM230 Modbus energy meter** and environmental readings from a **BME280**.
4. **Remote telemetry:** Used a **SIM7600 4G modem** to publish monitoring data to the **Blynk** dashboard.

The rooftop assembly also integrated a solar module, 500 W inverter, electrical protection, an emergency stop and a mounted backplate. The architecture figure above comes from page 13 of my final report.

## Prototype implementation and field testing

After reviewing several physical layouts, the components were mounted and wired on a steel backplate, then installed in a rooftop enclosure. The final system collected **18 electrical and environmental parameters** and delivered data to the cloud at **60-second intervals** during the trials.

A design revision widened PCB traces to address localized heating. The after-inverter board also provided separate input-power control for subsystems, allowing them to be isolated for testing and maintenance.

## Results and evidence

The report documents spot comparisons with the charge-controller and energy-meter displays, a short no-load series, and a 36 W load test.

| Validation check | Reported result |
| --- | --- |
| PV voltage | 33.37 V measured vs 33.0 V reference (**1.1% error**) |
| PV current | 0.73 A measured vs 0.70 A reference (**4.3% error**) |
| AC voltage, no load | Deviation **below 0.05%** across 200 readings |
| Active power, 36 W load | 36.46 W measured vs 36.4 W reference (**about 0.16% difference**) |
| Cloud telemetry | Monitoring updates **every 60 seconds** during field testing |

These comparisons met the project's **±5% measurement-accuracy target** within the tested conditions. The quantitative accuracy evidence covers selected readings and a **32-minute continuous serial capture**, not every operating condition or long-term reliability.

## What I learned

The most valuable part was integrating several disciplines into one tested system: physical wiring, embedded firmware, industrial data acquisition, wireless communication, cloud dashboards, and real measurements. Field work exposed issues—particularly component heating, integration delays and service limits—that weren't apparent from the initial architecture alone.

The experience strengthened my ability to debug the interface between hardware and software, adapt project scope, document limitations and collaborate with a practising engineer.

## Limitations and next steps

- **Cross-brand compatibility:** The configurable design was intended to support different vendors, but Modbus polling was tested only on an **EPEVER** controller. Interoperability with other products remains unverified.
- **Test duration:** The logged study covered one **32-minute** daytime window plus brief reference snapshots. Long-term stability and varying weather conditions were not evaluated.
- **Cloud restrictions:** Blynk's free-tier data and export limits constrained the available history despite the underlying telemetry working during the test.
- **Thermal behaviour:** Continuous USB logging increased ESP32 case temperature to approximately **49°C**, limiting extended tethered recording.
- **Unverified extensions:** The LoRa path was not field-tested, and proposed machine-learning fault prediction was **future work**, not an implemented feature.

No credentials, authentication tokens, private configuration files or full source-code appendix are published on this page.
