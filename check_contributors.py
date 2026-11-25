"""Checks contributor entries below the marker in CONTRIBUTORS.md."""
import sys

MARKER = "<!-- lines below this marker are checked by GitHub Actions CI -->"


def main(path="CONTRIBUTORS.md"):
    text = open(path, encoding="utf-8").read()
    if MARKER not in text:
        print("The marker line was removed. Put it back and add your line below it.")
        return 1
    errors, seen = 0, set()
    for n, line in enumerate(text.split(MARKER, 1)[1].splitlines(), start=1):
        line = line.rstrip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(" - ", 2)]
        if len(parts) != 3 or not all(parts) or len(parts[2]) < 5:
            errors += 1
            print(f"Line {n} after the marker does not match 'Name - Wikimedia username - one tool idea':\n  {line}")
            continue
        user = parts[1].lower()
        if user in seen:
            errors += 1
            print(f"Line {n}: username '{user}' appears twice.")
        seen.add(user)
    if errors:
        print(f"\n{errors} problem(s). Fix your line and push the update to your branch.")
        return 1
    print(f"All {len(seen)} lines look good.")
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
