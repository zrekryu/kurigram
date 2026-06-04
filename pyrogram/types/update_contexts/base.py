from __future__ import annotations

from dataclasses import dataclass

from pyrogram.raw.base import Chat, Update, User


@dataclass(frozen=True, slots=True)
class BaseUpdateContext:
    update: Update
    users: dict[int, User]
    chats: dict[int, Chat]
