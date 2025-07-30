import type { SvgIconComponent } from "@mui/icons-material";
import { Box, Typography } from "@mui/material";

type Props = {
  icon: SvgIconComponent;
  text: string;
  onClick: () => void;
};

export const MainActionButton: React.FC<Props> = ({
  icon: Icon,
  text,
  onClick,
}) => {
  return (
    <Box
      sx={{
        width: 240,
        height: 240,
        borderRadius: 2,
        bgcolor: "primary.main",
        "&:hover": {
          bgcolor: "primary.dark",
        },
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        cursor: "pointer",
        transition: "0.3s",
      }}
      onClick={onClick}
    >
      <Icon sx={{ fontSize: 32, mb: 1 }} />
      <Typography variant="body1">{text}</Typography>
    </Box>
  );
};
