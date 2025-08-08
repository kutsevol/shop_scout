import { Box } from "@mui/material";
import ShoppingCartOutlinedIcon from "@mui/icons-material/ShoppingCartOutlined";
import ShoppingCartIcon from "@mui/icons-material/ShoppingCart";
import FmdGoodOutlinedIcon from "@mui/icons-material/FmdGoodOutlined";
import { ShortInfoItem } from "./ShortInfoItem";

export const ShortInfoList = () => {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "center",
        gap: 5,
        mt: 4,
      }}
    >
      <ShortInfoItem
        icon={<ShoppingCartOutlinedIcon color="primary" />}
        title="Build Your Basket"
        text="Select the products you regularly buy and see how much they cost in stores across different countries."
      />

      <ShortInfoItem
        icon={<ShoppingCartIcon color="primary" />}
        title="Use Starter Basket"
        text="Not sure where to begin? Choose from our pre-made baskets to quickly compare essential items worldwide."
      />

      <ShortInfoItem
        icon={<FmdGoodOutlinedIcon color="primary" />}
        title="Explore the Map"
        text="Get a global view of prices — click on countries to discover local costs and compare living standards."
      />
    </Box>
  );
};
