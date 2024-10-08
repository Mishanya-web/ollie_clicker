# Real-Time Clicker Game

A real-time multiplayer web application game built with Django, Django Channels, and WebSockets. Players compete to click as many times as possible in real-time, with live updates and leaderboards.

## Features

- Real-time click counter using WebSockets
- Live leaderboard to track top players
- Responsive design for mobile and desktop
- Scalable backend with Django Channels and Redis

## Tech Stack

- **Backend**: Django, Django Channels
- **Frontend**: HTML, CSS, JavaScript (WebSockets)
- **Database**: PostgreSQL (or SQLite for local development)
- **Real-time Communication**: WebSockets (via Django Channels)
- **Other Tools**: Redis (for channels layer), Docker (for deployment)

## Installation

### Prerequisites

- Python 3.8+
- Redis (for Django Channels)
- PostgreSQL (optional, can use SQLite for development)

### Clone the repository

```bash
git clone https://github.com/yourusername/realtime-clicker-game.git
cd realtime-clicker-game
