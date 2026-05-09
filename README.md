# Backend Quest

Backend Quest is a Python console survival game about learning backend development while managing energy, coffee, knowledge, money, and stress.

The player travels through different locations, makes choices, experiences random events, and tries to reach the final career milestone prepared enough to become interview-ready.

This project started as a story-driven Python game and is being developed into a stronger backend-focused portfolio project with clean architecture, external API integration, database persistence, and testing planned for future versions.

---

## Project Status

Current version: **Initial Console MVP**

The current version is a working command-line game built with Python. It includes player state management, location-based travel, random events, mock weather effects, win/loss conditions, final score calculation, invalid choice penalty, and a refactored game loop.

---

## Current Features

- Player state management
- Travel between multiple locations
- Energy, coffee, knowledge, money, and stress stats
- Coffee survival mechanic
- Invalid choice penalty
- Random event system
- Mock weather system
- Location effects
- Win and loss conditions
- Final score summary
- Refactored game loop with helper functions
- Modular project structure

---

## Game Concept

The player moves through a series of locations while trying to survive the journey toward a backend engineering career.

Each action affects the player’s stats:

- **Travel** moves the player to the next location
- **Rest** restores energy and lowers stress
- **Study** increases knowledge but costs energy and coffee
- **Find Coffee** restores coffee and resets the coffee counter

The player can win by reaching the final location with enough knowledge to be considered interview-ready.

The player can lose by running out of energy, money, coffee tolerance, or reaching too much stress.

---

## Player Stats

The game tracks the following player stats:

- `energy`
- `coffee`
- `knowledge`
- `money`
- `stress`
- `turns_without_coffee`
- `current_location_index`

These stats represent the player’s physical energy, focus, financial resources, learning progress, and stress level throughout the game.

---

## Current Game Outcomes

The game currently supports several final statuses:

- `Interview Ready`
- `Reached Final Location, But Not Ready`
- `Burned Out`
- `Broke But Learning`
- `Coffee Crush`
- `Stress Collapse`
- `Still On The Quest`

---

## Weather System

The current version includes a mock weather system.

Weather effects are applied when the player travels to a new location. This keeps gameplay balanced and prevents weather from repeatedly draining stats while the player stays in the same place.

Current mock weather can affect:

- energy
- coffee
- knowledge
- stress

Future versions will replace the mock weather system with a real external Weather API integration.

Planned Weather API improvements:

- Fetch real weather data based on the player’s current location
- Use environment variables for API keys
- Add API error handling
- Add fallback mock weather if the external API fails
- Include weather details in future API responses

---

## Random Events

The game includes random events connected to both the player’s action and current location.

Events can affect:

- energy
- coffee
- knowledge
- money
- stress

Examples of event categories:

- travel delays
- study breakthroughs
- rest recovery
- coffee shop encounters

---

## Tech Used

- Python
- Object-Oriented Programming
- Modular project structure
- Dictionaries and lists
- Random events
- Mock data
- Manual testing
- Git version control

---

## Project Structure

```text
backend-quest/
│
├── actions.py
├── constants.py
├── events.py
├── game.py
├── locations.py
├── player.py
├── weather.py
├── README.md
└── .gitignore
```
---
## Next Steps
Planned improvements:
* Improve score balance
* Add save/load functionality
* Move core logic into a GameEngine service
* Add a Flask REST API
* Add SQLite database persistence
* Integrate a real Weather API
* Add unit tests with pytest
* Add simple frontend interface
* Deploy the project
* Improve README with screenshots and API documentation

---
## Long-Term Goal

The long-term goal is to turn Backend Quest from a console-based Python game into a backend-powered simulation project that demonstrates:

* API design
* database persistence
* external API integration
* clean architecture
* testing
* deployment
* backend development readiness

This project is part of my preparation for backend apprenticeship and junior developer opportunities.