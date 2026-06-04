from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyrogram.raw.base import Chat, Update, User


@dataclass(frozen=True, slots=True)
class RawUpdateContext:
    """
    update (:obj:`~pyrogram.raw.base.Update`):
            The received update, which can be one of the many single Updates listed in the
            :obj:`~pyrogram.raw.base.Update` base type.

    users (``dict``):
        Dictionary of all :obj:`~pyrogram.raw.base.User` mentioned in the update.
        You can access extra info about the user (such as *first_name*, *last_name*, etc...) by using
        the IDs you find in the *update* argument (e.g.: *users[1768841572]*).

    chats (``dict``):
        Dictionary of all :obj:`~pyrogram.raw.base.Chat` mentioned in the update.
        You can access extra info about the chat (such as *title*, *participants_count*, etc...)
        by using the IDs you find in the *update* argument (e.g.: *chats[1701277281]*).
    """

    update: Update
    users: dict[int, User]
    chats: dict[int, Chat]