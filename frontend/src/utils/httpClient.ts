const BASE_URL = "http://localhost:5173/api";

export async function getData<T>(url: string): Promise<T> {
  return await fetch(BASE_URL + url).then((response) => {
    if (!response.ok) {
      throw new Error(`${response.status} ${response.text}`);
    }
    return response.json();
  });
}
