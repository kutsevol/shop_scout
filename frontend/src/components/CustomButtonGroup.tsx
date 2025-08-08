import { useState } from "react";
import { Box, Button } from "@mui/material";

export const CustomButtonGroup = () => {
  const [isMultiple, setIsMultiple] = useState(false);

  return (
    <Box
      sx={{
        backgroundColor: "primary.900",
        display: "inline-flex",
        borderRadius: "4px",
        overflow: "hidden",
      }}
    >
      <Button
        sx={{
          backgroundColor: isMultiple ? "primary.900" : "#ffffff",
          height: isMultiple ? 25 : 26,
          color: isMultiple ? "primary.contrastText" : "#000",
        }}
        onClick={() => setIsMultiple(false)}
      >
        Two Countries
      </Button>
      <Button
        sx={{
          backgroundColor: isMultiple ? "#ffffff" : "primary.900",
          height: isMultiple ? 26 : 25,
          color: isMultiple ? "#000" : "primary.contrastText",
        }}
        onClick={() => setIsMultiple(true)}
      >
        Multiple Countries
      </Button>
    </Box>
  );
};
