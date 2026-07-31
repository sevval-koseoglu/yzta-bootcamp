import sqlite3
from datetime import datetime
from pathlib import Path

from ai_analyzer import redact_sensitive_data


DEFAULT_DB_PATH = Path(__file__).with_name("analysis_history.db")


def _connect(db_path=DEFAULT_DB_PATH):
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database(db_path=DEFAULT_DB_PATH):
    with _connect(db_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS analyses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                message_summary TEXT NOT NULL,
                score INTEGER NOT NULL,
                level TEXT NOT NULL
            )
            """
        )


def create_message_summary(message, max_length=120):
    """Hassas numaraları maskeleyerek geçmiş ekranı için kısa bir özet oluşturur."""
    safe_message = " ".join(redact_sensitive_data(message).split())
    if len(safe_message) <= max_length:
        return safe_message
    return safe_message[: max_length - 3].rstrip() + "..."


def save_analysis(message, score, level, db_path=DEFAULT_DB_PATH):
    initialize_database(db_path)
    with _connect(db_path) as connection:
        connection.execute(
            "INSERT INTO analyses (created_at, message_summary, score, level) VALUES (?, ?, ?, ?)",
            (
                datetime.now().isoformat(timespec="seconds"),
                create_message_summary(message),
                score,
                level,
            ),
        )


def get_analyses(limit=100, db_path=DEFAULT_DB_PATH):
    initialize_database(db_path)
    with _connect(db_path) as connection:
        rows = connection.execute(
            "SELECT id, created_at, message_summary, score, level "
            "FROM analyses ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [dict(row) for row in rows]


def get_dashboard_stats(db_path=DEFAULT_DB_PATH):
    initialize_database(db_path)
    with _connect(db_path) as connection:
        summary = connection.execute(
            "SELECT COUNT(*) AS total, COALESCE(AVG(score), 0) AS average_score FROM analyses"
        ).fetchone()
        level_rows = connection.execute(
            "SELECT level, COUNT(*) AS count FROM analyses GROUP BY level"
        ).fetchall()

    distribution = {"Düşük Risk": 0, "Orta Risk": 0, "Yüksek Risk": 0}
    distribution.update({row["level"]: row["count"] for row in level_rows})
    return {
        "total": summary["total"],
        "average_score": round(summary["average_score"], 1),
        "distribution": distribution,
    }


def clear_analyses(db_path=DEFAULT_DB_PATH):
    initialize_database(db_path)
    with _connect(db_path) as connection:
        connection.execute("DELETE FROM analyses")
