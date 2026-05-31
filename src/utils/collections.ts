import { getCollection, type CollectionEntry } from "astro:content";

export type SessionEntry = CollectionEntry<"wwdc2025">;

export interface YearInfo {
  year: number;
  slug: string;
  count: number;
}

const YEAR_COLLECTIONS: Record<string, number> = {
  wwdc2025: 2025,
};

export function getAvailableYears(): string[] {
  return Object.keys(YEAR_COLLECTIONS);
}

export function yearFromCollection(collectionName: string): number | undefined {
  return YEAR_COLLECTIONS[collectionName];
}

export async function getAllSessions(): Promise<SessionEntry[]> {
  const sessions = await getCollection("wwdc2025");
  sessions.sort((a, b) => b.data.date.getTime() - a.data.date.getTime());
  return sessions;
}

export async function getYearInfo(): Promise<YearInfo[]> {
  const years: YearInfo[] = [];
  for (const [collection, year] of Object.entries(YEAR_COLLECTIONS)) {
    try {
      const sessions = await getCollection(collection as "wwdc2025");
      years.push({ year, slug: `wwdc${year}`, count: sessions.length });
    } catch {
      years.push({ year, slug: `wwdc${year}`, count: 0 });
    }
  }
  years.sort((a, b) => b.year - a.year);
  return years;
}
