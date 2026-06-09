#!/usr/bin/env python3
"""Download high-resolution thumbnails (1280x720_2x) for all WWDC26 sessions."""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
IMAGE_DIR = ROOT / "public/images/sessions/2026"

def download_hd_image(session_id: str, source_url: str) -> bool:
    """Download 1280x720 2x version of the thumbnail."""
    hd_url = source_url.replace("_wide_250x141_2x", "_wide_1280x720_2x")
    output_path = IMAGE_DIR / f"{session_id}.jpg"

    result = subprocess.run(
        ["curl", "-s", "-o", str(output_path), hd_url],
        capture_output=True
    )

    if result.returncode != 0:
        print(f"❌ {session_id}: Failed to download")
        return False

    # Verify file size (should be > 100KB for HD images)
    size = output_path.stat().st_size
    if size < 100_000:
        print(f"⚠️  {session_id}: File too small ({size} bytes), might be low-res")
        return False

    print(f"✅ {session_id}: Downloaded HD thumbnail ({size // 1024}KB)")
    return True

def main():
    metadata_path = ROOT / "scripts/wwdc2026-metadata.json"

    with open(metadata_path) as f:
        metadata = json.load(f)

    print(f"Downloading HD thumbnails for {len(metadata)} sessions...")
    print(f"Target directory: {IMAGE_DIR}")
    print()

    success = 0
    failed = 0

    for session in metadata:
        sid = session["id"]
        source = session.get("thumbnailSource", "")

        if not source:
            print(f"⚠️  {sid}: No thumbnail source URL")
            failed += 1
            continue

        if download_hd_image(sid, source):
            success += 1
        else:
            failed += 1

    print()
    print(f"Summary: {success} succeeded, {failed} failed")

    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
