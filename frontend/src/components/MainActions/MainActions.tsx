import { Box } from "@mui/material";
import AddShoppingCartIcon from "@mui/icons-material/AddShoppingCart";
import ShoppingCartIcon from "@mui/icons-material/ShoppingCart";
import AttachMoneyIcon from "@mui/icons-material/AttachMoney";

import { MainActionButton } from "./MainActionButton";

type MainActionsProps = {
  onClick: () => void;
};

export const MainActions: React.FC<MainActionsProps> = ({ onClick }) => {
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
      <MainActionButton
        icon={<AddShoppingCartIcon />}
        text="Create Basket"
        onClick={onClick}
      />

      <MainActionButton
        icon={<ShoppingCartIcon />}
        text="View Standard Basket"
        onClick={onClick}
      />

      <MainActionButton
        icon={<AttachMoneyIcon />}
        text="Enter Your Own Prices"
        onClick={onClick}
      />

      <MainActionButton
        icon={<AttachMoneyIcon />}
        text="Open Map"
        onClick={onClick}
      />
    </Box>
  );
};
