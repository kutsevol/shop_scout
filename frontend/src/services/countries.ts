import type { Country } from "../types/country";
import { getData } from "../utils/httpClient";

export async function getCountries(): Promise<Country[]> {
  try {
    return await getData<Country[]>("/countries.json");
  } catch (error) {
    console.error("Fetching countries failed: ", error);
    throw new Error("Failed to load country list. Please try again later.");
  }
}
