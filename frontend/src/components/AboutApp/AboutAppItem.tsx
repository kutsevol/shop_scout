import { Box, Paper, Typography } from "@mui/material";
import type { ReactNode } from "react";

type AboutAppItemProps = {
  icon: ReactNode;
  title: string;
  text: string;
};

export const AboutAppItem: React.FC<AboutAppItemProps> = ({
  icon,
  title,
  text,
}) => {
  return (
    <Box
      sx={{
        display: "flex",
        width: 300,
        justifyContent: "center",
        alignItems: "center",
        gap: 3,
      }}
    >
      <Paper
        elevation={0}
        sx={{
          px: { xs: 2, sm: 3 },
          py: { xs: 2, sm: 3 },
          display: "flex",
          flexWrap: "wrap",
          justifyContent: "center",
          borderRadius: 10,
          backgroundColor: "primary.50",
          backdropFilter: "blur(8px)",
        }}
      >
        {icon}
      </Paper>
      <Box>
        <Typography
          variant="h3"
          component="h6"
          gutterBottom
          color="common.black"
          fontWeight={900}
          fontSize={20}
        >
          {title}
        </Typography>
        <Typography component="p" gutterBottom color="common.black">
          {text}
        </Typography>
      </Box>
    </Box>
  );
};
