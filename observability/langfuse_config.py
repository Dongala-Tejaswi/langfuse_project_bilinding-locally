import os
from typing import Any, Optional

from langfuse import Langfuse


def _get_langfuse_host() -> str:
    return os.getenv("LANGFUSE_HOST", "http://localhost:3000").rstrip("/")


def get_langfuse_client() -> Optional[Langfuse]:
    public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
    secret_key = os.getenv("LANGFUSE_SECRET_KEY")
    if not public_key or not secret_key:
        return None

    return Langfuse(public_key=public_key, secret_key=secret_key, host=_get_langfuse_host())


def get_langfuse_callback_handler() -> Optional[Any]:
    try:
        # Optional dependency: the callback integration requires LangChain.
        from langfuse.callback import CallbackHandler  # type: ignore
    except Exception:
        return None

    public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
    secret_key = os.getenv("LANGFUSE_SECRET_KEY")
    if not public_key or not secret_key:
        return None

    return CallbackHandler(public_key=public_key, secret_key=secret_key, host=_get_langfuse_host())


# Backwards-compatible name used by existing code.
def get_langfuse_handler():
    return get_langfuse_client()