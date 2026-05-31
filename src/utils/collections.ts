import { getCollection, type CollectionEntry } from "astro:content";

export type SessionEntry = CollectionEntry<"wwdc2025"> | CollectionEntry<"wwdc2024"> | CollectionEntry<"wwdc2023"> | CollectionEntry<"wwdc2022"> | CollectionEntry<"wwdc2021"> | CollectionEntry<"wwdc2020">;

export interface YearInfo {
  year: number;
  slug: string;
  count: number;
}

const YEAR_COLLECTIONS: Record<string, number> = {
  wwdc2025: 2025,
  wwdc2024: 2024,
  wwdc2023: 2023,
  wwdc2022: 2022,
  wwdc2021: 2021,
  wwdc2020: 2020,
};

export function getAvailableYears(): string[] {
  return Object.keys(YEAR_COLLECTIONS);
}

export function yearFromCollection(collectionName: string): number | undefined {
  return YEAR_COLLECTIONS[collectionName];
}

export async function getAllSessions(): Promise<SessionEntry[]> {
  const [s2025, s2024] = await Promise.all([
    getCollection("wwdc2025"),
    getCollection("wwdc2024"),
  ]);
  const sessions = [...s2025, ...s2024];
  sessions.sort((a, b) => b.data.date.getTime() - a.data.date.getTime());
  return sessions;
}

export async function getYearInfo(): Promise<YearInfo[]> {
  const years: YearInfo[] = [];
  for (const [collection, year] of Object.entries(YEAR_COLLECTIONS)) {
    try {
      const sessions = await getCollection(collection as any);
      years.push({ year, slug: `wwdc${year}`, count: sessions.length });
    } catch {
      years.push({ year, slug: `wwdc${year}`, count: 0 });
    }
  }
  years.sort((a, b) => b.year - a.year);
  return years;
}
