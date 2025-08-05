import { Box } from "@mui/material";
import ShoppingCartOutlinedIcon from "@mui/icons-material/ShoppingCartOutlined";
import { AboutAppItem } from "./AboutAppItem";
import FmdGoodOutlinedIcon from "@mui/icons-material/FmdGoodOutlined";

export const AboutApp = () => {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        gap: 4,
        mt: 4,
      }}
    >
      <AboutAppItem
        icon={<ShoppingCartOutlinedIcon color="primary" />}
        title="Title"
        text="Text about what can we do"
      />

      <AboutAppItem
        icon={<FmdGoodOutlinedIcon color="primary" />}
        title="Title"
        text="Text about what can we do"
      />

      <AboutAppItem
        icon={<ShoppingCartOutlinedIcon color="primary" />}
        title="Title"
        text="Text about what can we do"
      />
    </Box>
  );
};
