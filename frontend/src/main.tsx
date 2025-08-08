import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import {
  HashRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import { ThemeProvider, CssBaseline } from "@mui/material";
import "./index.css";
import App from "./App.tsx";
import { theme } from "./styles/theme.ts";
import { HomePage } from "./pages/HomePage.tsx";

createRoot(document.getElementById("root")!).render(
  <Router>
    <StrictMode>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Routes>
          <Route path="/" element={<App />}>
            <Route path="home" element={<Navigate to="/" />} />
            <Route index element={<HomePage />} />
          </Route>
        </Routes>
      </ThemeProvider>
    </StrictMode>
  </Router>
);
