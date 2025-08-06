const BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://localhost:5173/api";

export async function getData<T>(url: string): Promise<T> {
  const response = await fetch(BASE_URL + url);
  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`${response.status} ${errorText}`);
  }

  return response.json();
}
