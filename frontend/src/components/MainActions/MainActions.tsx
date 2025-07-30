import { ThemeProvider, Box } from "@mui/material";
import AddShoppingCartIcon from "@mui/icons-material/AddShoppingCart";
import ShoppingCartIcon from "@mui/icons-material/ShoppingCart";
import AttachMoneyIcon from "@mui/icons-material/AttachMoney";

import { MainActionButton } from "./MainActionButton";

type Props = {
  onClick: () => void;
};

const theme = {
  palette: {
    primary: {
      main: "#ccd9e7ff",
      dark: "#95cdf2ff",
    },
  },
};

export const MainActions: React.FC<Props> = ({ onClick }) => {
  return (
    <ThemeProvider theme={theme}>
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
          icon={AddShoppingCartIcon}
          text="Create Basket"
          onClick={onClick}
        />

        <MainActionButton
          icon={ShoppingCartIcon}
          text="View Standard Basket"
          onClick={onClick}
        />

        <MainActionButton
          icon={AttachMoneyIcon}
          text="Enter Your Own Prices"
          onClick={onClick}
        />

        <MainActionButton
          icon={AttachMoneyIcon}
          text="Open Map"
          onClick={onClick}
        />
      </Box>
    </ThemeProvider>
  );
};
