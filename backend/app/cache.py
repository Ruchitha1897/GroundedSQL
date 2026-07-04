"""Simple in-process TTL cache for repeated questions.
Swap for Redis/ElastiCache in a multi-instance deployment — same interface."""
from cachetools import TTLCache
from app.config import settings

_cache = TTLCache(maxsize=500, ttl=settings.CACHE_TTL_SECONDS)


def cache_get(key: str):
    return _cache.get(key)


def cache_set(key: str, value):
    _cache[key] = value


def make_cache_key(question: str) -> str:
    return question.strip().lower()