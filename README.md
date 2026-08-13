# ChatGPTDemo

This repository is a demonstration of **GitHub connectivity with ChatGPT**.

## Purpose

The goal of this repository is to showcase how ChatGPT can interact with a GitHub repository through a connected GitHub integration. Instead of only discussing code, ChatGPT can work directly with the repository and perform common development and project-management operations.

## Demonstration Application

The repository contains a small full-stack calculator application. It provides a concrete example of ChatGPT creating a project structure and pushing multiple files directly to GitHub.

The application consists of:

- A **Flask backend** exposing calculator operations through a REST API.
- A **vanilla HTML/CSS/JavaScript frontend** containing an interactive calculator.
- Communication between the frontend and backend through the `/api/calculate` endpoint.

## Directory Structure

```text
ChatGPTDemo/
├── README.md
├── backend/
│   ├── app.py
│   ├── calculator.py
│   └── requirements.txt
└── frontend/
    ├── index.html
    ├── app.js
    └── style.css
```

### Backend

`backend/calculator.py` contains the basic arithmetic functions for addition, subtraction, multiplication, and division.

`backend/app.py` provides the Flask API:

- `GET /api/health` — health check
- `POST /api/calculate` — perform a calculation

### Frontend

The `frontend` directory contains a simple interactive calculator. It collects the user's input and sends calculations to the Flask backend using the browser Fetch API.

## Running the Application

### Prerequisites

Make sure Python 3.9+ is installed.

### 1. Clone the repository

```bash
git clone https://github.com/Ha-an1/ChatGPTDemo.git
cd ChatGPTDemo
```

### 2. Set up the backend

From the repository root:

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment.

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask server:

```bash
python app.py
```

The backend will run at `http://localhost:5000`.

### 3. Run the frontend

Keep the backend running and open a second terminal. From the repository root, start a simple static HTTP server:

```bash
cd frontend
python -m http.server 8080
```

Then open:

```text
http://localhost:8080
```

The calculator frontend will send calculation requests to the backend running on port `5000`.

### 4. Run the backend tests

From the `backend` directory, run:

```bash
python -m unittest test_calculator.py -v
```

The tests cover addition, subtraction, multiplication, division, decimal calculations, division by zero, and unsupported operations.

## GitHub + ChatGPT Demonstrations

This repository can be used to demonstrate capabilities such as:

- Reading repository files and understanding existing code
- Creating new files
- Updating existing files
- Creating branches
- Committing changes
- Creating and managing issues
- Creating pull requests
- Reviewing pull requests and their changes
- Responding to review comments
- Inspecting commits and repository history
- Checking GitHub Actions and CI results

## Example Workflow

A typical demonstration could look like this:

1. Ask ChatGPT to inspect the repository.
2. Ask ChatGPT to create or modify a file.
3. Ask ChatGPT to create a branch for the change.
4. Ask ChatGPT to commit the changes.
5. Ask ChatGPT to open a pull request.
6. Ask ChatGPT to review the pull request.
7. Make changes based on the review.
8. Merge the pull request.

This makes the repository a simple sandbox for demonstrating how an AI assistant can participate in a GitHub-based development workflow.

## Repository Status

This repository is intentionally lightweight. Its primary purpose is **demonstration and experimentation**, rather than serving as a production application.

## ChatGPT + GitHub

The repository is owned by `Ha-an1` and is connected to ChatGPT through a GitHub integration. The operations performed during demonstrations should be visible in the repository's commits, branches, issues, and pull requests, making it possible to verify the interaction directly from GitHub.
