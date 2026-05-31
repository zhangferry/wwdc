/** Format seconds to "Xh Ym" or "Ym" */
export function formatDuration(seconds: number): string {
  const h = Math.floor(seconds / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  if (h > 0) return `${h}h ${m}m`;
  return `${m}m`;
}

/** Format date to localized string */
export function formatDate(date: Date): string {
  return date.toLocaleDateString("zh-CN", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}

/** Level badge label */
export function levelLabel(level: string): string {
  const map: Record<string, string> = {
    beginner: "入门",
    intermediate: "进阶",
    advanced: "高级",
  };
  return map[level] ?? level;
}

/** All unique tracks from sessions */
export function extractTracks(sessions: Array<{ track: string }>): string[] {
  const tracks = new Set(sessions.map((s) => s.track));
  return Array.from(tracks).sort();
}
