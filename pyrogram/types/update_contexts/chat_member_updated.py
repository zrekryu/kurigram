from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .base import BaseUpdateContext


if TYPE_CHECKING:
    from pyrogram.types import ChatMemberUpdated


@dataclass(frozen=True, slots=True)
class ChatMemberUpdatedUpdateContext(BaseUpdateContext):
    chat_member_updated: ChatMemberUpdated
