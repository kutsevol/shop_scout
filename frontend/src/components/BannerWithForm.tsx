import { Box, Typography } from "@mui/material";

import { MainForm } from "./MainForm";

export const BannerWithForm = () => {
  return (
    <Box
      sx={{
        position: "relative",
        width: "100vw",
        left: "calc(-50vw + 50%)",
        height: "75vh",
        overflow: "hidden",
      }}
    >
      {/* Background image with overlay (darkened) */}
      <Box
        sx={{
          position: "absolute",
          top: 0,
          left: 0,
          width: "100%",
          height: "100%",
          backgroundImage:
            "linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url(/img/supermarket2.jpeg)",
          backgroundSize: "cover",
          backgroundPosition: "center",
          zIndex: 0,
        }}
      />

      <Box
        sx={{
          position: "relative",
          zIndex: 2,
          height: "100%",
          display: "flex",
          flexDirection: "column",
        }}
      >
        <Box
          sx={{
            flex: 1,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            px: 2,
          }}
        >
          <Typography
            variant="h3"
            component="h1"
            gutterBottom
            color="primary.contrastText"
            fontWeight={900}
          >
            Choose countries to compare product prices
          </Typography>
          <MainForm />
        </Box>
      </Box>
    </Box>
  );
};
