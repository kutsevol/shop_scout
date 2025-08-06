import { useState } from "react";
import { Box, Button } from "@mui/material";

export const CustomButtonGroup = () => {
  const [active, setActive] = useState<"two" | "multiple">("two");

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
          backgroundColor: active === "two" ? "#ffffff" : "primary.900",
          height: active === "two" ? 26 : 25,
          color: active === "two" ? "#000" : "primary.contrastText",
        }}
        onClick={() => setActive("two")}
      >
        Two Countries
      </Button>
      <Button
        sx={{
          backgroundColor: active === "multiple" ? "#ffffff" : "primary.900",
          height: active === "multiple" ? 26 : 25,
          color: active === "multiple" ? "#000" : "primary.contrastText",
        }}
        onClick={() => setActive("multiple")}
      >
        Multiple Countries
      </Button>
    </Box>
  );
};
