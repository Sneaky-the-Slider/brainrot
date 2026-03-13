import json
import os
import time
from typing import Dict, List

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
OUTPUT_PATH = os.path.join(ROOT, "content_index.json")

IGNORE_DIRS = {".git", "__pycache__", "node_modules"}

MATURE_KEYWORDS = [
    "guns",
    "weapon",
    "weapons",
    "nsfw",
    "sex",
    "porn",
    "bitch",
    "gangster",
    "drugs",
    "violence",
]


def is_binary(path: str) -> bool:
    try:
        with open(path, "rb") as handle:
            chunk = handle.read(2048)
        return b"\x00" in chunk
    except OSError:
        return True


def safe_preview(path: str, limit: int = 320) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as handle:
            text = handle.read(limit * 2)
    except OSError:
        return ""

    ascii_text = text.encode("ascii", "ignore").decode("ascii")
    normalized = " ".join(ascii_text.split())
    return normalized[:limit]


def classify_rating(path: str) -> str:
    lowered = path.lower()
    for keyword in MATURE_KEYWORDS:
        if keyword in lowered:
            return "mature"
    return "general"


def collect_files() -> List[Dict[str, object]]:
    items: List[Dict[str, object]] = []
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for name in files:
            full_path = os.path.join(root, name)
            rel_path = os.path.relpath(full_path, ROOT)
            if rel_path == os.path.relpath(OUTPUT_PATH, ROOT):
                continue
            ext = os.path.splitext(name)[1].lstrip(".")
            size = os.path.getsize(full_path)
            binary = is_binary(full_path)
            preview = "" if binary else safe_preview(full_path)
            group = rel_path.split(os.sep, 1)[0]
            rating = classify_rating(rel_path)

            items.append(
                {
                    "path": rel_path,
                    "ext": ext or "(none)",
                    "bytes": size,
                    "is_binary": binary,
                    "preview": preview,
                    "group": group,
                    "rating": rating,
                }
            )
    return sorted(items, key=lambda item: item["path"])


def main() -> None:
    payload = {
        "generated_at": int(time.time()),
        "files": collect_files(),
    }
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


if __name__ == "__main__":
    main()
