from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .base import BaseUpdateContext

if TYPE_CHECKING:
    from pyrogram.types import CallbackQuery


@dataclass(frozen=True, slots=True)
class CallbackQueryUpdateContext(BaseUpdateContext:
    callback_query: CallbackQuery