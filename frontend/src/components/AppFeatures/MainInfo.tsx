import { Box, Button, Typography } from "@mui/material";

export const MainInfo = () => {
  return (
    <Box
      sx={{
        mt: 5,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        padding: "60px 100px 60px 100px",
        backgroundColor: "primary.50",
      }}
    >
      <Typography variant="h3" component="h1" gutterBottom fontWeight={900}>
        Planning a Move Abroad? Make Smart Financial Decisions!
      </Typography>
      <Typography component="p">
        Easily create your personal shopping basket and compare the cost of
        everyday goods across different countries. Whether you're relocating,
        traveling, studying, or just curious — our tool helps you understand
        price differences, budget smarter, and choose the best destination for
        your lifestyle.
      </Typography>
      <Typography component="p" sx={{ mt: 5 }}>
        ✨ Visualize cost of living across the globe with interactive
        comparisons.
      </Typography>
      <Typography component="p">
        🛒 Customize your own basket with the products you actually use.
      </Typography>
      <Typography component="p">
        🌍 Explore countries and cities to see how far your money will go.
      </Typography>
      <Typography component="p">
        📊 Make data-driven choices before making a big move.
      </Typography>{" "}
      <Typography component="p"></Typography>🚀 Save time, money, and surprises
      when planning your next chapter abroad.
      <Button
        variant="contained"
        size="large"
        color="secondary"
        sx={{
          margin: 3,
          color: "primary.contrastText",
        }}
      >
        Start
      </Button>
    </Box>
  );
};
