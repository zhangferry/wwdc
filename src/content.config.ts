import { defineCollection, z } from "astro:content";

const sessionSchema = z.object({
  id: z.string(),
  title: z.string(),
  titleZh: z.string(),
  track: z.string(),
  level: z.enum(["beginner", "intermediate", "advanced"]),
  duration: z.number(),
  date: z.string().transform((val) => new Date(val)),
  thumbnail: z.string(),
  videoUrl: z.string().url(),
  tags: z.array(z.string()).default([]),
});

const wwdc2025 = defineCollection({
  type: "content",
  schema: sessionSchema,
});

export const collections = { wwdc2025 };

export type SessionData = z.infer<typeof sessionSchema>;
