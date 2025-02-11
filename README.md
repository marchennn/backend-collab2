# IoT Monitoring and Control System

## Overview
This project implements an IoT-based monitoring and control system using various sensors, microcontrollers, and a Raspberry Pi as the central hub. The system collects environmental data (temperature, humidity, and distance measurements) and provides LED control capabilities through a mobile application.
System Architecture
The system consists of several components:
Hardware Components

### Sensors:
- DHT22: Temperature and Humidity sensor
- A02YYUW: Distance sensor
- HC-SR04: Distance sensor


### Controllers:

- Arduino Uno: Interfaces with HC-SR04 sensor
- ESP32: Controls LED output via PWM/ON/OFF commands


### Central Processing:

Raspberry Pi: Acts as the main hub for data collection, processing, and storage

## IoT System Architecture Flow
```mermaid
flowchart TD
    %% Sensors Section
    subgraph Sensors[Input Sensors]
        DHT22[DHT22\nSuhu & Kelembapan]
        A02Y[A02YYUW\nJarak]
        HCSR[HC-SR04\nJarak]
    end
    %% Hardware Controllers
    subgraph Controllers[Hardware Controllers]
        ARD[Arduino Uno]
        ESP[ESP32\nLED Control]
    end
    %% Raspberry Pi System
    subgraph RaspberryPi[Raspberry Pi]
        subgraph DataCollection[Data Collection]
            PY1[Python Serial Reader]
            PY2[Python MQTT Handler]
        end
        subgraph Backend[Backend Services]
            MQTT[MQTT Broker]
            FAST[FastAPI Server]
            PM2[PM2 Process Manager]
        end
        subgraph Storage[Database]
            DB[(PostgreSQL)]
        end
        subgraph Monitoring[Monitoring]
            GRAF[Grafana Dashboard]
        end
    end
    %% Mobile App
    APP[MIT App Inventor\nMobile App]
    %% Connections
    DHT22 -->|Serial| PY1
    A02Y -->|Serial| PY1
    HCSR --> ARD
    ARD -->|Serial| PY1
    
    PY1 -->|Publish| MQTT
    MQTT -->|Subscribe| DB
    DB -->|Metrics| GRAF
    
    FAST <-->|REST API| APP
    
    APP -->|Control Commands| FAST
    FAST -->|LED Control| MQTT
    MQTT <--> PY2
    PY2 -->|Serial| ESP
    ESP -->|PWM/ON/OFF| LED[LED Output]

    %% PM2 Monitoring
    PM2 -.->|Monitor| FAST

    %% Styles
    classDef sensors fill:#f9f,stroke:#333
    classDef controllers fill:#bbf,stroke:#333
    classDef backend fill:#bfb,stroke:#333
    classDef storage fill:#fb9,stroke:#333
    classDef frontend fill:#9bf,stroke:#333
    
    class DHT22,A02Y,HCSR sensors
    class ARD,ESP controllers
    class MQTT,FAST,PM2 backend
    class DB storage
    class APP frontend
```