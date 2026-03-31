import feedparser
import os
import re
from datetime import datetime, timezone, timedelta

VELOG_RSS = "https://v2.velog.io/rss/@addung"
POSTS_DIR = "_posts"

TAG_MAP = [
    (["python"],                              "python"),
    (["c언어", "c language", "c-language"],   "c-language"),
    (["html", "css"],                         "html-css"),
    (["java"],                                "java"),
    (["ai", "머신러닝", "딥러닝", "machine learning", "deep learning"], "ai-study"),
    (["데이터분석", "data analysis", "pandas"], "data-analysis"),
]


def map_category(tags: list[str]) -> str:
    tags_lower = [t.lower() for t in tags]
    for keywords, category in TAG_MAP:
        for kw in keywords:
            if any(kw in tag for tag in tags_lower):
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
            if slug in fname:
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

        slug     = slugify(title)
        category = map_category(tags)

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
        body        = extract_body(entry)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter + body)

        print(f"  [new] {filepath}")
        new_count += 1

    print(f"\nDone. {new_count} new post(s) added.")


if __name__ == "__main__":
    main()
