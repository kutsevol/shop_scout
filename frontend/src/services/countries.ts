import type { Country } from "../types/country";
import { client } from "../utils/httpClient";

export const getCountries = () => {
  return client.get<Country[]>(`/countries/`);
};
