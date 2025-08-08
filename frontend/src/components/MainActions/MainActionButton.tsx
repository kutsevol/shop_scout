import { Button } from "@mui/material";
import type { ReactNode } from "react";

type MainActionButtonProps = {
  icon: ReactNode;
  text: string;
  onClick: () => void;
};

export const MainActionButton = ({
  icon,
  text,
  onClick,
}: MainActionButtonProps) => {
  return (
    <>
      <Button
        variant="outlined"
        startIcon={icon}
        sx={{
          width: "200px",
          height: "100px",
          boxShadow: 3,
          border: "none",
          color: "info.main",
        }}
        onClick={onClick}
      >
        {text}
      </Button>
    </>
  );
};
