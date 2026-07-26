from __future__ import annotations


def summarize_conversation(messages: list[str]) -> str:
    if not messages:
        return "No conversation yet"
    return " | ".join(messages[-3:])
