// const BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://0.0.0.0:8000/";

// function wait(delay: number) {
//   return new Promise((resolve) => setTimeout(resolve, delay));
// }

// export async function getData<T>(url: string): Promise<T> {
//   return wait(500)
//     .then(() => fetch(BASE_URL + url))
//     .then(async (response) => {
//       if (!response.ok) {
//         const errorText = await response.text();
//         throw new Error(`${response.status} ${errorText}`);
//       }
//       return response.json();
//     });
// }

/* eslint-disable @typescript-eslint/no-explicit-any */
// const BASE_URL = "/api";
// const BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://0.0.0.0:8000";
const BASE_URL = "/api";

// returns a promise resolved after a given delay
function wait(delay: number) {
  return new Promise((resolve) => {
    setTimeout(resolve, delay);
  });
}

// To have autocompletion and avoid mistypes
type RequestMethod = "GET" | "POST" | "PATCH" | "DELETE";

function request<T>(
  url: string,
  method: RequestMethod = "GET",
  data: any = null // we can send any data to the server
): Promise<T> {
  const options: RequestInit = { method };

  if (data) {
    // We add body and Content-Type only for the requests with data
    options.body = JSON.stringify(data);
    options.headers = {
      "Content-Type": "application/json; charset=UTF-8",
    };
  }

  // DON'T change the delay it is required for tests
  return fetch(BASE_URL+url, options).then(async (response) => {
    console.log("Status:", response.status);
    const text = await response.text();
    console.log("Raw response:", text);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return JSON.parse(text); // тільки якщо впевнений, що це JSON
  });
}

export const client = {
  get: <T>(url: string) => request<T>(url),
  post: <T>(url: string, data: any) => request<T>(url, "POST", data),
  patch: <T>(url: string, data: any) => request<T>(url, "PATCH", data),
  delete: (url: string) => request(url, "DELETE"),
};
