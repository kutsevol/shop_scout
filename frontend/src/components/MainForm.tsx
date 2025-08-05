import { Button, Paper } from "@mui/material";
import { useState } from "react";

import { CustomSelect } from "./CustomSelect";

const COUNTRIES = ["Ukraine", "Poland", "France", "Spain", "Germany"];

export const MainForm = () => {
  const [country1, setCountry1] = useState("");
  const [country2, setCountry2] = useState("");
  const [basketType, setBasketType] = useState("Default basket");

  const handleBasketTypeChange = (value: string) => {
    setBasketType(value);
  };

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
        px: { xs: 3, sm: 6 },
        py: { xs: 4, sm: 6 },
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "center",
        gap: 2,
        borderRadius: 4,
        backgroundColor: "primary.800",
        width: "80vw",
        textAlign: "left",
        backdropFilter: "blur(8px)",
        boxShadow: "0 8px 32px rgba(0,0,0,0.2)",
      }}
    >
      {/* <CustomSelect
        value={basketType}
        helperText="Select basket"
        data={["Default basket", "Create basket"]}
        onChange={(value) => handleBasketTypeChange(value)}
      /> */}

      <CustomSelect
        value={country1}
        helperText="Select country 1"
        data={COUNTRIES}
        onChange={(value) => handleChangeCountry1(value)}
      />

      <CustomSelect
        value={country2}
        helperText="Select country 2"
        data={COUNTRIES}
        onChange={(value) => handleChangeCountry2(value)}
      />

      <Button
        variant="contained"
        size="large"
        color="secondary"
        sx={{
          height: "56px",
          alignSelf: "flex-end",
          minWidth: 200,
          flexGrow: 1,
          color: "primary.contrastText",
        }}
      >
        Compare prices
      </Button>
    </Paper>
  );
};
