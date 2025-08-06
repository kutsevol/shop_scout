import { Button, Paper, Box } from "@mui/material";
import { useEffect, useState } from "react";

import { CountriesSelect } from "./CountriesSelect";
import { CustomButtonGroup } from "./CustomButtonGroup";
import { getCountries } from "../services/countries";
import type { Country } from "../types/country";

export const MainForm = () => {
  const [country1, setCountry1] = useState("");
  const [country2, setCountry2] = useState("");
  const [countries, setCountries] = useState<Country[]>([]);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    getCountries()
      .then((countries) => {
        setCountries(
          countries.sort((country1, country2) =>
            country1.name.localeCompare(country2.name)
          )
        );
      })
      .catch(() => {
        setErrorMessage("Error whith fatching Countries data");
      })
      .finally(() => setLoading(false));
  }, []);

  const handleChangeCountry1 = (value: string) => {
    setCountry1(value);
  };

  const handleChangeCountry2 = (value: string) => {
    setCountry2(value);
  };
  return (
    <Paper
      elevation={6}
      sx={{
        px: { xs: 3, sm: 3 },
        py: { xs: 3, sm: 3 },
        display: "flex",
        flexDirection: "column",
        flexWrap: "wrap",
        justifyContent: "left",
        gap: 2,
        borderRadius: 4,
        backgroundColor: "primary.800",
        width: "80vw",
        textAlign: "left",
        backdropFilter: "blur(8px)",
        boxShadow: "0 8px 32px rgba(0,0,0,0.2)",
      }}
    >
      <Box>
        <CustomButtonGroup />
      </Box>

      <Box
        sx={{
          display: "flex",
          flexWrap: "wrap",
          justifyContent: "space-between",
          gap: 2,

          textAlign: "left",
        }}
      >
        <CountriesSelect
          value={country1}
          helperText="Select country 1"
          countries={countries}
          onChange={(value) => handleChangeCountry1(value)}
        />

        <CountriesSelect
          value={country2}
          helperText="Select country 2"
          countries={countries}
          onChange={(value) => handleChangeCountry2(value)}
        />

        <Button
          variant="contained"
          size="large"
          color="secondary"
          sx={{
            height: "56px",
            alignSelf: "flex-start",
            flexGrow: 1,
            color: "primary.contrastText",
          }}
        >
          Compare
        </Button>
      </Box>
    </Paper>
  );
};
