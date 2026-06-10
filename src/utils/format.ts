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

/** Track consolidation mapping — display only, original article data unchanged */
const TRACK_MAP: Record<string, string> = {
  "SwiftUI & UI Frameworks": "Swift & UI",
  "SwiftUI": "Swift & UI",
  "UIKit": "Swift & UI",
  "Swift": "Swift & UI",
  "Widget & Live Activities": "Swift & UI",
  "App Intents": "Swift & UI",
  "Internationalization": "Swift & UI",
  "Essentials|Design": "Essentials",
  "Essentials|Machine Learning & AI": "Essentials",
  "Design|SwiftUI & UI Frameworks": "Design",
  "Machine Learning & AI|Design": "Machine Learning & AI",
  "AI & Machine Learning": "Machine Learning & AI",
  "Audio & Video|Spatial Computing": "Spatial Computing",
  "visionOS & Spatial Computing": "Spatial Computing",
  "visionOS": "Spatial Computing",
  "App Store, Distribution & Marketing": "App Store & Distribution",
  "App Store & Distribution": "App Store & Distribution",
  "App Store Distribution & Marketing": "App Store & Distribution",
  "Business & Education": "App Store & Distribution",
  "System Frameworks": "System & Services",
  "System Services": "System & Services",
  "Networking": "System & Services",
  "Accessories": "System & Services",
  "CarPlay": "System & Services",
  "watchOS": "System & Services",
  "tvOS": "System & Services",
  "App Services": "System & Services",
  "Xcode & Developer Tools": "Developer Tools",
  "Audio & Video": "Media & Web",
  "Photos & Camera": "Media & Web",
  "Safari & Web": "Media & Web",
  "Graphics, Games & Media": "Graphics & Games",
  "Swift & Data": "Swift & UI",
  "Accessibility & Inclusion": "Accessibility",
};

export function consolidateTrack(track: string): string {
  return TRACK_MAP[track] ?? track;
}

/** All unique consolidated tracks from sessions */
export function extractTracks(sessions: Array<{ track: string }>): string[] {
  const tracks = new Set(sessions.map((s) => consolidateTrack(s.track)));
  return Array.from(tracks).sort();
}
