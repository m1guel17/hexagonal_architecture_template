# hexagonal_architecture_template
Welcome to my hexagonal_architecture_template repository! Designed to jump-start your next Software as a Service (SaaS) product using Hexagonal Architecture principles and Layered Architecture principles (In progres). This template provides you with a solid foundation to handle common SaaS requirements, including API integrations, data management, business logic, user authentication, and customizable frontends.

> [!CAUTION]
> This is still a work in progress
>

 
# Table of Contents
1. [Project Overview](#Project-Overview)
2. [Architecture Overview](#Architecture-Overview)
3. [Directory Structure](#Directory-Structure)
4. [Getting Started](#Getting-Started)
5. Development Guide
6. [Common Modules and Extensions](#Common-Modules-and-Extensions)
7. [Best Practices](#Best-Practices)

## Project Overview
This stack aims to simplify building SaaS solutions by adopting the Hexagonal (Ports and Adapters) Architecture, ensuring that your core business logic remains independent from external systems (such as databases, third-party APIs, or UI frameworks).


## Architecture Overview
Hexagonal Architecture—also known as Ports and Adapters—is a pattern that promotes a clear separation between the application core (domain logic) and the infrastructure (external resources and services).

### Core principles
* Domain-Centric: The domain layer represents your core business logic and is free from technology-specific details.
* Use Cases: Encapsulate the specific functionalities or actions available in the application (in the application layer).
* Ports: Define interfaces for inputs and outputs (e.g., REST endpoints, message queues, databases).
* Adapters: Implement these interfaces in the infrastructure layer (e.g., adapters to talk to databases or external APIs).

This approach allows faster development cycles by making the code modular, testable, and easy to maintain.

## Directory Structure
```
hexagonal_architecture_template/
├── application/
│   ├── ports/
│   │   ├── output/
│   │   └── input/
│   └── usecases/
├── domain/
│   ├── entity/
│   └── value_object/
├── infrastructure/
│   └── adapters/
│       ├── output/
│       └── input/
├── driver/
├── run.py
└── requirements.txt
```
*Project structure details can be found* [here](https://github.com/m1guel17/hexagonal_architecture_template/blob/main/readme_support/directory_details.md)

## Getting Started

Prerequisites
* Python 3.12
* Flask for handling HTTP requests.
* PostgreSQL/MySQL (or any other compatible DB) for data persistence.
* Message Broker (e.g., Redis, RabbitMQ) if the project requires asynchronous messaging.
* Any additional libraries required for specific SaaS features (e.g., payment gateways, analytics).

Deployment
1. **Clone the repository:**
   ```bash
   git clone https://github.com/m1guel17/hexagonal_architecture_template.git
   cd hexagonal_architecture_template
   ```
2. **Set Up the Virtual Environment:**
    ```bash
    python -m venv venv
    source venv\Scripts\activate   # On Linux: venv/bin/activate
    ```
3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up the Environment Variables:**
   ```
   ENV_VARIABLE=<value_here>
   ```
   <!-- *Description and examples for keys can be found* [here](https://github.com/m1guel17/hexagonal_architecture_template/blob/main/keys_description.md) <br /><br /> -->
5. **Run the application:**
   ```bash
   python3.12 run.py
   ```

## Development Guide
_Work in progress_

## Common Modules and Extensions
_Work in progress_

## Best Practices
1. Keep the Domain Clean: Avoid cluttering domain entities with infrastructure or UI details.
2. Dependency Injection: Pass adapters (implementing output ports) into use cases or domain services to keep the application flexible.
3. SRP (Single Responsibility Principle): Each class or function should have one job (i.e., handle one type of input or output).

<!-- 
> [!NOTE]
> This is still a work in progress
>

> [!TIP]
> This is still a work in progress
> 

> [!IMPORTANT]
> This is still a work in progress
> 

> [!WARNING]
> This is still a work in progress
> -->
