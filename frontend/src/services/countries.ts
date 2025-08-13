import type { Country } from "../types/country";
import { client } from "../utils/httpClient";
// import { getData } from "../utils/httpClient";

// export async function getCountries(): Promise<Country[]> {
//   try {
//     return await getData<Country[]>("/countries");
//   } catch (error) {
//     console.error("Fetching countries failed: ", error);
//     throw new Error("Failed to load country list. Please try again later.");
//   }
// }

export const getCountries = () => {
  return client.get<Country[]>(`/countries/`);
};
