import type { Country } from "../types/country";
import { getData } from "../utils/httpClient";

export async function getCountries(): Promise<Country[]> {
  return await getData<Country[]>("/countries.json");
}
