import os
import re
import shutil

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


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_after_closing_dashes)."""
    if not content.startswith("---"):
        return {}, content
    end = content.index("---", 3)
    fm_text = content[3:end].strip()
    body = content[end + 3:]

    fm = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
    return fm, body


def update_categories_in_content(content: str, new_category: str) -> str:
    """Replace the categories frontmatter value with new_category."""
    return re.sub(
        r"^(categories:\s*\[)[^\]]*(\])",
        rf"\g<1>{new_category}\2",
        content,
        count=1,
        flags=re.MULTILINE,
    )


def collect_moves() -> list[tuple[str, str, str]]:
    """Return list of (src_path, dst_path, new_category) for files that need moving."""
    moves = []
    for root, _, files in os.walk(POSTS_DIR):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            src_path = os.path.join(root, fname)
            with open(src_path, encoding="utf-8") as f:
                content = f.read()

            fm, body = parse_frontmatter(content)
            title = fm.get("title", "").strip('"')
            current_category = os.path.basename(root)
            new_category = map_category(title, body)

            if new_category == current_category:
                continue

            dst_dir = os.path.join(POSTS_DIR, new_category)
            dst_path = os.path.join(dst_dir, fname)
            moves.append((src_path, dst_path, new_category))

    return moves


def main():
    moves = collect_moves()

    if not moves:
        print("모든 파일이 이미 올바른 폴더에 있습니다.")
        return

    print(f"재분류 대상: {len(moves)}개 파일\n")
    col = max(len(src) for src, _, _ in moves) + 2
    for src, dst, cat in moves:
        print(f"  {src:<{col}} →  {dst}  [{cat}]")

    print()
    answer = input("위 내용대로 이동하시겠습니까? [y/N] ").strip().lower()
    if answer != "y":
        print("취소했습니다.")
        return

    for src, dst, new_category in moves:
        dst_dir = os.path.dirname(dst)
        os.makedirs(dst_dir, exist_ok=True)

        with open(src, encoding="utf-8") as f:
            content = f.read()

        updated = update_categories_in_content(content, new_category)

        with open(dst, "w", encoding="utf-8") as f:
            f.write(updated)

        os.remove(src)
        print(f"  [moved] {src}  →  {dst}")

    # 빈 폴더 정리
    for root, dirs, files in os.walk(POSTS_DIR, topdown=False):
        if root == POSTS_DIR:
            continue
        if not os.listdir(root):
            os.rmdir(root)
            print(f"  [rmdir] {root}")

    print(f"\n완료. {len(moves)}개 파일 이동.")


if __name__ == "__main__":
    main()
