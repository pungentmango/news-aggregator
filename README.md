# News Aggregator

This is a full-stack news aggregator application that fetches and displays news articles from various sources. The application consists of a **Flask** backend that retrieves news from RSS feeds, and a **React** frontend that presents these news articles in a tabbed layout. The frontend and backend are containerized using **Docker** for easy deployment.

## Features

- Flask backend serves as an API that fetches news from various RSS feeds (e.g., world news, technology, business, etc.).
- React frontend that displays the news in a clean, user-friendly tabbed interface.
- The application is fully containerized using Docker for simple setup and deployment.
- Dynamic tabs in the frontend for various news categories (e.g., Technology, Business, World).
- Responsiveness and mobile-friendly layout.

## Technologies Used

- **Frontend**: React, Tailwind CSS
- **Backend**: Flask, Python
- **Database**: (Optional, if any)
- **Docker**: Containerization for both frontend and backend
- **Docker Compose**: Orchestration to run both frontend and backend together

## Prerequisites

Before you start, ensure you have the following installed on your machine:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

To get the project up and running, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/news-aggregator.git
cd news-aggregator
```

### 2. Build and Run the Containers

To build the Docker images and start the containers, run the following command from the root directory where the `docker-compose.yml` file is located:

```bash
docker-compose up --build
```


### 3. Stopping the Containers

To stop and remove the running containers, use the following command:

```bash
docker-compose down
```

This will gracefully stop the services and clean up the containers. To restart, run the docker-compose up --build command again.

### 4. Development Tips

Live Code Changes
If you want to reflect live changes without rebuilding the Docker images, you can make use of Docker volumes. The current setup in docker-compose.yml syncs your local code with the running containers, so you should be able to edit your code (both backend and frontend) and see the changes immediately without rebuilding the containers.

Adding New RSS Feeds
To add new RSS feeds for other categories, modify the backend to fetch articles from the new sources and ensure the frontend displays the new categories as dynamic tabs.