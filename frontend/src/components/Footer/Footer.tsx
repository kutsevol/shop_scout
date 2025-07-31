import { Box, Typography, Container } from "@mui/material";

export const Footer = () => {
  return (
    <Box
      sx={{
        bgcolor: "primary.main",
        color: "text.primary",
        py: 3,
        mt: 6,
        borderTop: "1px solid #ccc",
      }}
    >
      <Container
        maxWidth="xl"
        sx={{
          display: "flex",
          flexDirection: { xs: "column", sm: "row" },
          justifyContent: "space-between",
          alignItems: "center",
          textAlign: { xs: "center", sm: "left" },
        }}
      >
        <Typography variant="body2">
          © {new Date().getFullYear()} Shop Scout. All rights reserved.
        </Typography>
        <Typography variant="body2">Contact: support@shopscout.com</Typography>
      </Container>
    </Box>
  );
};
