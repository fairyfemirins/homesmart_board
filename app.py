#!/usr/bin/env python3
"""
HomeSmart Board: A digital smart board for small spaces.
Combines task management, media display, and note-taking.
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Database setup
DATABASE = os.path.join(os.path.dirname(__file__), 'homesmart.db')


def init_db():
    """Initialize the SQLite database."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'pending'
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()


@app.route('/')
def index():
    """Render the main dashboard."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        cursor.execute('SELECT * FROM notes ORDER BY created_at DESC LIMIT 5')
        notes = cursor.fetchall()
    return render_template('index.html', tasks=tasks, notes=notes)


@app.route('/add_task', methods=['POST'])
def add_task():
    """Add a new task."""
    title = request.form.get('title')
    description = request.form.get('description')
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
        conn.commit()
    return redirect(url_for('index'))


@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    """Update task status."""
    status = request.form.get('status')
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (status, task_id))
        conn.commit()
    return redirect(url_for('index'))


@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    """Delete a task."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
    return redirect(url_for('index'))


@app.route('/add_note', methods=['POST'])
def add_note():
    """Add a new note."""
    content = request.form.get('content')
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO notes (content) VALUES (?)', (content,))
        conn.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)