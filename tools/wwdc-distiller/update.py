#!/usr/bin/env python3
"""Incremental update entrypoint for the standalone WWDC Notes skill."""

import sys

sys.dont_write_bytecode = True

from distill import main

if __name__ == "__main__":
    raise SystemExit(main())
