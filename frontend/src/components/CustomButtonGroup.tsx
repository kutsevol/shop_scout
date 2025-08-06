import { Box, Button } from "@mui/material";
import type { ButtonGroup } from "../types/buttons";

type CustomButtonGroupProps = {
  active: ButtonGroup;
  buttons: ButtonGroup[];
  onClick?: (value: string) => void;
};

export const CustomButtonGroup: React.FC<CustomButtonGroupProps> = ({
  active,
  buttons,
  onClick = () => {},
}) => {
  return (
    <Box
      sx={{
        backgroundColor: "primary.900",
        display: "inline-flex",
        borderRadius: "4px",
        overflow: "hidden",
      }}
    >
      {buttons.map((button) => (
        <Button
          key={button.value}
          sx={{
            backgroundColor: active === button ? "#ffffff" : "primary.900",
            height: active === button ? 26 : 25,
            color: active === button ? "#000" : "primary.contrastText",
          }}
          onClick={() => onClick(button.value)}
        >
          {button.text}
        </Button>
      ))}
    </Box>
  );
};
