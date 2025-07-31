import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { ThemeProvider, createTheme, CssBaseline } from "@mui/material";
import "./index.css";
import App from "./App.tsx";

const theme = createTheme({
  palette: {
    mode: "light", // або 'dark'
    primary: {
      main: "#0099ffff",
    },
    info: {
      main: "#000000ff", // наприклад, бірюзовий
    },
  },
  typography: {
    fontFamily: `"Montserrat", "Roboto", "Helvetica", "Arial", sans-serif`,
    button: {
      textTransform: "none", // прибирає uppercase з кнопок
      fontWeight: 500,
    },
  },
});

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <App />
    </ThemeProvider>
  </StrictMode>
);
