import { Box, Typography, Button, Paper } from "@mui/material";
import { Header } from "./Header/Header";

type Props = {
  onClick: () => void;
};

export const HeroSection: React.FC<Props> = ({ onClick }) => {
  return (
    <Box
      sx={{
        position: "relative",
        width: "100vw",
        left: "calc(-50vw + 50%)",
        height: "100vh",
        overflow: "hidden",
      }}
    >
      {/* Фонове зображення з затемненням */}
      <Box
        sx={{
          position: "absolute",
          top: 0,
          left: 0,
          width: "100%",
          height: "100%",
          backgroundImage:
            "linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url(/img/supermarket2.jpg)",
          backgroundSize: "cover",
          backgroundPosition: "center",
          zIndex: 0,
        }}
      />

      {/* Контейнер вмісту */}
      <Box
        sx={{
          position: "relative",
          zIndex: 2,
          height: "100%",
          display: "flex",
          flexDirection: "column",
        }}
      >
        <Header />

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
          <Paper
            elevation={6}
            sx={{
              px: { xs: 3, sm: 6 },
              py: { xs: 4, sm: 6 },
              borderRadius: 4,
              backgroundColor: "rgba(255, 255, 255, 0.9)",
              maxWidth: 600,
              textAlign: "center",
              backdropFilter: "blur(8px)",
              boxShadow: "0 8px 32px rgba(0,0,0,0.2)",
            }}
          >
            <Typography variant="h3" component="h1" gutterBottom>
              Welcome to <strong>Shop Scout</strong>
            </Typography>
            <Typography variant="h6" paragraph>
              Your personal assistant for better product discovery and a smooth
              shopping experience.
            </Typography>
            <Button
              variant="contained"
              size="large"
              sx={{ mt: 3, borderRadius: 3, px: 4, py: 1 }}
              onClick={onClick}
            >
              Get Started
            </Button>
          </Paper>
        </Box>
      </Box>
    </Box>
  );
};
