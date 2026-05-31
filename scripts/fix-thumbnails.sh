#!/bin/bash
# fix-thumbnails.sh — 验证并修复所有 session 文章的缩略图 URL
# 用法: bash scripts/fix-thumbnails.sh [--fix]
#   --fix  自动修复已知的 403 URL（默认只检查）

set -euo pipefail
cd "$(dirname "$0")/.."

FIX_MODE=false
[[ "${1:-}" == "--fix" ]] && FIX_MODE=true

# Apple CDN 只允许 250x141 和 1280x720 两个尺寸
# 其他尺寸（700x394, 720x405 等）都返回 403
VALID_SIZES=("250x141" "1280x720")

CONTENT_DIR="src/content"
FAILED=0
FIXED=0

echo "=== 检查缩略图 ==="

for dir in "$CONTENT_DIR"/wwdc*; do
  [[ -d "$dir" ]] || continue
  year=$(basename "$dir")

  for md in "$dir"/*.md; do
    [[ -f "$md" ]] || continue

    # Extract thumbnail URL
    thumb=$(grep '^thumbnail:' "$md" | head -1 | sed 's/thumbnail: *//' | tr -d '"' | tr -d "'")

    if [[ -z "$thumb" ]]; then
      echo "EMPTY: $md"
      ((FAILED++))
      continue
    fi

    # Check local files
    if [[ "$thumb" == /* ]]; then
      if [[ ! -f "public${thumb}" ]]; then
        echo "MISSING LOCAL: $md → $thumb"
        ((FAILED++))
      fi
      continue
    fi

    # Check CDN URLs
    if [[ "$thumb" == *devimages-cdn* ]]; then
      # Extract size from URL
      size=$(echo "$thumb" | grep -o '_wide_[0-9x]*_' | sed 's/_wide_//;s/_//')
      if [[ "$size" != "1280x720" && "$size" != "250x141" ]]; then
        echo "BAD SIZE ($size): $(basename "$md")"
        if $FIX_MODE; then
          # Fix by replacing with 1280x720
          new_url=$(echo "$thumb" | sed "s/_wide_${size}_/_wide_1280x720_/")
          sed -i '' "s|${thumb}|${new_url}|" "$md"
          echo "  FIXED → 1280x720"
          ((FIXED++))
        else
          ((FAILED++))
        fi
        continue
      fi

      # Verify URL returns 200
      code=$(curl -sI -o /dev/null -w "%{http_code}" "$thumb" 2>/dev/null || echo "000")
      if [[ "$code" != "200" ]]; then
        echo "CDN $code: $(basename "$md") → ${thumb:0:80}..."
        ((FAILED++))
      fi
    fi
  done
done

echo ""
echo "=== 结果 ==="
echo "失败: $FAILED"
$FIX_MODE && echo "修复: $FIXED"

if [[ $FAILED -gt 0 ]] && ! $FIX_MODE; then
  echo ""
  echo "运行 bash scripts/fix-thumbnails.sh --fix 自动修复尺寸问题"
fi
