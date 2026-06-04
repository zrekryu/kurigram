from __future__ import annotations

from dataclasses import dataclass

from pyrogram.types import Message


@dataclass(frozen=True, slots=True)
class MessageUpdateContext:
    message: Message
