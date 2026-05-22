# HomeSmart Board

**A digital smart board for small spaces.**

HomeSmart Board combines task management, media display, and note-taking into a single, space-efficient interface. Perfect for small bedrooms, home offices, or dorm rooms.

## Features
- **Task Management:** Add, edit, and delete tasks with status tracking.
- **Media Display:** Embed YouTube videos or display images.
- **Note-Taking:** Digital whiteboard for quick notes.

## Tech Stack
- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** Bootstrap (HTML/CSS/JS)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Femirins/homesmart_board.git
   cd homesmart_board
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install flask
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage
- **Tasks:** Add, update, or delete tasks using the task management panel.
- **Media:** Embed YouTube videos by replacing the iframe `src` in `templates/index.html`.
- **Notes:** Add notes using the note-taking panel.

## License
This project is licensed under the **MIT License**.