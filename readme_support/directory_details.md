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

- application/
    - ports/
        - input/: Interfaces that define how external requests (like REST calls or CLI commands) interact with the application.
        - output/: Interfaces that define how the application communicates with external services (e.g., databases, APIs).
        - usecases/: Contains the core operations (business logic) that orchestrate domain entities and external adapters.

- domain/
    - entity/: Core business objects, typically representing data with both state and behavior.
    - value_object/: Immutable objects that represent specific domain concepts and do not have an identity (e.g., monetary values, dates, etc.).

- infrastructure/
    - adapters/
        - input/: Real implementations of input ports (e.g., REST controllers, GraphQL resolvers, CLI).
        - output/: Real implementations of output ports (e.g., database repositories, external API clients).
- driver/: Contains application launchers or interface drivers. This could be an HTTP server driver, CLI driver, message queue driver, etc.
- run.py: The entry point to the application. It may initialize dependencies and start up servers or other processes.
- requirements.txt: A list of Python dependencies needed to run the application.