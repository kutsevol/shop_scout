import type { Country } from "../types/country";
import type { Product } from "../types/product";

const BASE_URL = "/api";

function wait(delay: number) {
  return new Promise((resolve) => {
    setTimeout(resolve, delay);
  });
}

function withResolveDelay<T>(fn: T, delay: number) {
  return async () => {
    await wait(delay);
    return fn;
  };
}

// To have autocompletion and avoid mistypes
type RequestMethod = "GET" | "POST" | "PATCH";

async function request(
  url: string,
  requestParams?: Product,
  method: RequestMethod = "GET"
): Promise<Country[] | Product[]> {
  const options: RequestInit = { method };

  if (requestParams) {
    options.body = JSON.stringify(requestParams);
    options.headers = {
      "Content-Type": "application/json; charset=UTF-8",
    };
  }

  const response = await fetch(BASE_URL + url, options);

  if (!response.ok) {
    const errorBody = await response.json().catch(() => null);
    const errorMessage = errorBody?.detail || response.statusText;
    throw new Error(`HTTP error! status: ${response.status} - ${errorMessage}`);
  }

  return response.json();
}

export const client = {
  get: (url: string) => request(url),
  post: (url: string, data: any) => request(url, data, "POST"),
  patch: (url: string, data: any) => request(url, data, "PATCH"),
};
