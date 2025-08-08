const BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://localhost:5173/api";

function wait(delay: number) {
  return new Promise((resolve) => setTimeout(resolve, delay));
}

export async function getData<T>(url: string): Promise<T> {
  return wait(500)
    .then(() => fetch(BASE_URL + url))
    .then(async (response) => {
      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`${response.status} ${errorText}`);
      }
      return response.json();
    });
}
