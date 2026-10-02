#!/usr/bin/env python3
"""Full-text search across the WPDS skill references.

Usage:
    python scripts/search_docs.py "dark mode color"
    python scripts/search_docs.py tooltip props

Zero dependencies: standard library only. Ranks documents by weighted term
frequency (title > frontmatter description > headings > body) and prints the
best-matching line from each result so you can decide which file to read.
"""

import re
import sys
from pathlib import Path

REFERENCES_DIR = Path(__file__).resolve().parent.parent / "references"
MAX_RESULTS = 8
MAX_SNIPPETS = 3

WEIGHTS = {"title": 8, "description": 4, "headings": 2, "body": 1}
BODY_TERM_CAP = 10  # cap per-term body hits so one spammy file can't dominate

# English function words that carry no routing signal; dropped from queries so
# "how to add a tooltip" ranks by "add tooltip", not by who says "to" most.
STOPWORDS = frozenset("""
a an the and or but if then else for of to in on at by with from into about as
is are was were be been being do does did done how what when where which who
whom why can could should would may might will shall must i me my we our you
your it its this that these those there here not no nor so than too very s t
don now use using used get got make makes
""".split())


def tokenize(text):
    return [t for t in re.split(r"[^a-z0-9$-]+", text.lower()) if t and t not in STOPWORDS]


def split_parts(text):
    """Split a document into (frontmatter, headings, body) text blobs."""
    frontmatter, headings, body_lines = "", [], []
    in_fm = text.startswith("---\n")
    for i, line in enumerate(text.splitlines()):
        if in_fm:
            frontmatter += "\n" + line
            if i > 0 and line.strip() == "---":
                in_fm = False
        elif line.lstrip().startswith("#"):
            headings.append(line.lstrip("# ").strip())
        else:
            body_lines.append(line)
    return frontmatter, "\n".join(headings), "\n".join(body_lines)


def phrase_score(terms, title, frontmatter, headings, body):
    """Bonus for verbatim contiguous runs (n>=2) of query terms, per part.

    Matching only the full query is brittle — "server side rendering setup"
    must still hit docs that say "server side rendering" — so every
    contiguous sub-phrase is scored, longer runs weighted higher.
    """
    if len(terms) < 2:
        return 0
    ngrams = []
    for n in range(len(terms), 1, -1):
        for i in range(len(terms) - n + 1):
            ngrams.append(" ".join(terms[i:i + n]))
    parts = ((title, 6), (frontmatter, 3), (headings, 2), (body, 1))
    score = 0
    for ngram in ngrams:
        n = len(ngram.split())
        for text, mult in parts:
            score += min(text.lower().count(ngram), 3) * n * 4 * mult
    return score


def score_doc(terms, title, frontmatter, headings, body):
    """Return (score, {term: weighted_hits}) for one document."""
    score, detail = 0, {}
    parts = {
        "title": tokenize(title),
        "description": tokenize(frontmatter),
        "headings": tokenize(headings),
        "body": tokenize(body),
    }
    for term in terms:
        weighted = 0
        for part, tokens in parts.items():
            hits = tokens.count(term)
            if part == "body":
                hits = min(hits, BODY_TERM_CAP)
            weighted += hits * WEIGHTS[part]
        if weighted:
            detail[term] = weighted
            score += weighted
    score += phrase_score(terms, title, frontmatter, headings, body)
    return score, detail


def snippets(lines, terms):
    """First few body lines that contain a query term, trimmed for display."""
    out = []
    for line in lines:
        if any(t in line.lower() for t in terms):
            out.append(line.strip()[:140])
            if len(out) >= MAX_SNIPPETS:
                break
    return out


def main():
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print(__doc__)
        print("No query given. For topic routing, read references/index.md instead.")
        return 0
    query = " ".join(sys.argv[1:])
    terms = tokenize(query)
    if not terms:
        print("Query contained no searchable terms (all stopwords?).")
        print("For topic routing, read references/index.md instead.")
        return 1

    if not REFERENCES_DIR.is_dir():
        print(f"references/ not found at {REFERENCES_DIR}", file=sys.stderr)
        return 1

    results = []
    for path in sorted(REFERENCES_DIR.rglob("*.md")):
        if path.name == "index.md":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as e:
            print(f"skipping {path}: {e}", file=sys.stderr)
            continue
        frontmatter, headings, body = split_parts(text)
        title = re.search(r"^#\s+(.+)$", text, re.M)
        title = title.group(1) if title else path.stem
        score, detail = score_doc(terms, title, frontmatter, headings, body)
        if score > 0:
            results.append((score, path, title, detail, snippets(body.splitlines(), terms)))

    if not results:
        print(f'No matches for "{query}" in references/.')
        print("Check references/index.md for the topic routing table.")
        return 1

    results.sort(key=lambda r: (-r[0], str(r[1])))
    print(f'"{query}" — {len(results)} file(s) matched, top {min(MAX_RESULTS, len(results))}:\n')
    for score, path, title, detail, snips in results[:MAX_RESULTS]:
        rel = path.relative_to(REFERENCES_DIR.parent)
        print(f"[{score:>4}] {rel}  ({title})")
        print(f"      terms: {', '.join(f'{k}:{v}' for k, v in sorted(detail.items()))}")
        for s in snips:
            print(f"      > {s}")
        print()
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
    sys.exit(main())
