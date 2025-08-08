import { createTheme } from "@mui/material";
import { blue, orange } from "@mui/material/colors";

export const theme = createTheme({
  palette: {
    mode: "light",
    primary: blue,
    secondary: orange,
  },
  typography: {
    fontFamily: `"Mulish", "Roboto", "Helvetica", "Arial", sans-serif`,
    button: {
      textTransform: "none",
      fontWeight: 700,
    },
  },
  components: {
    MuiInputLabel: {
      styleOverrides: {
        root: {
          color: "#90caf9",
        },
      },
    },
    MuiOutlinedInput: {
      styleOverrides: {
        root: {
          backgroundColor: "#fff",
          color: "#000",
          "& .MuiOutlinedInput-notchedOutline": {
            borderColor: "#fff",
          },
          "&:hover .MuiOutlinedInput-notchedOutline": {
            borderColor: "#ccc",
          },
          "&.Mui-focused .MuiOutlinedInput-notchedOutline": {
            borderColor: "#90caf9",
          },
        },
        input: {
          color: "#000",
        },
      },
    },
    MuiSelect: {
      styleOverrides: {
        icon: {
          color: "#000",
        },
      },
    },
  },
});
