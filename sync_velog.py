import feedparser
import os
import re
from datetime import datetime, timezone, timedelta

VELOG_RSS = "https://v2.velog.io/rss/@addung"
POSTS_DIR = "_posts"

CATEGORY_MAP = [
    (["bikeeyes", "한이음", "자전거", "노면", "dcc"],                         "projects"),
    (["yolo", "cnn", "딥러닝", "머신러닝", "segmentation", "데이터셋"],         "ai"),
    (["stm32", "임베디드", "gpio", "펌웨어"],                                 "embedded"),
    (["html", "css", "javascript", "자바스크립트", "nodejs", "node.js", "express", "ejs", "dom"], "web"),
    (["python", "파이썬", "tkinter", "pyqt"],                                "python"),
    (["c언어", "c language", "c-language", "포인터", "구조체"],               "c-language"),
]


def map_category(title: str, body: str = "") -> str:
    text = title.lower()
    for keywords, category in CATEGORY_MAP:
        for kw in keywords:
            if kw in text:
                return category
    return "etc"


def slugify(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def slug_exists(slug: str) -> bool:
    for root, _, files in os.walk(POSTS_DIR):
        for fname in files:
            # filename format: YYYY-MM-DD-{slug}.md  (date prefix is 11 chars)
            name = fname[:-3] if fname.endswith(".md") else fname
            if name[11:] == slug:
                return True
    return False


def parse_date(entry) -> datetime:
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        return datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
    return datetime.now(tz=timezone.utc)


def format_date(dt: datetime) -> str:
    kst = dt.astimezone(timezone(timedelta(hours=9)))
    return kst.strftime("%Y-%m-%d %H:%M:%S +0900")


def format_date_prefix(dt: datetime) -> str:
    kst = dt.astimezone(timezone(timedelta(hours=9)))
    return kst.strftime("%Y-%m-%d")


def build_frontmatter(title: str, date_str: str, category: str,
                      tags: list[str], velog_url: str) -> str:
    tags_yaml = ", ".join(f'"{t}"' for t in tags)
    return (
        "---\n"
        "layout: post\n"
        f'title: "{title}"\n'
        f"date: {date_str}\n"
        f"categories: [{category}]\n"
        f"tags: [{tags_yaml}]\n"
        f"velog_url: {velog_url}\n"
        "---\n\n"
    )


def extract_body(entry) -> str:
    if hasattr(entry, "content") and entry.content:
        return entry.content[0].value
    if hasattr(entry, "summary"):
        return entry.summary
    return ""


def main():
    print(f"Fetching RSS: {VELOG_RSS}")
    feed = feedparser.parse(VELOG_RSS)

    if feed.bozo:
        print(f"RSS parse warning: {feed.bozo_exception}")

    new_count = 0
    for entry in feed.entries:
        title = entry.get("title", "untitled").strip()
        link  = entry.get("link", "")
        tags  = [t.term for t in entry.get("tags", [])]
        dt    = parse_date(entry)

        slug = slugify(title)
        body = extract_body(entry)
        category = map_category(title, body)

        if slug_exists(slug):
            print(f"  [skip] already exists: {slug}")
            continue

        date_str    = format_date(dt)
        date_prefix = format_date_prefix(dt)
        filename    = f"{date_prefix}-{slug}.md"
        target_dir  = os.path.join(POSTS_DIR, category)
        os.makedirs(target_dir, exist_ok=True)
        filepath = os.path.join(target_dir, filename)

        frontmatter = build_frontmatter(title, date_str, category, tags, link)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter + body)

        print(f"  [new] {filepath}")
        new_count += 1

    print(f"\nDone. {new_count} new post(s) added.")


if __name__ == "__main__":
    main()
