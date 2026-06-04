from __future__ import annotations

from dataclasses import dataclass

from pyrogram.types import CallbackQuery


@dataclass(frozen=True, slots=True)
class CallbackQueryUpdateContext:
    callback_query: CallbackQuery