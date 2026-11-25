#!/usr/bin/env python3
"""Write the roast line to $ENTRY_OUTPUT_DIR/entry.txt (default /output)."""
import os

LINE = "My agent searched fourteen times, found nothing, then confidently quoted a doc page that doesn't exist and volunteered to rewrite it."

def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
