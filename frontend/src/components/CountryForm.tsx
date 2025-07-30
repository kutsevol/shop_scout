import {
  Box,
  Button,
  Container,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  type SelectChangeEvent,
} from "@mui/material";
import { useState } from "react";
import CompareArrowsIcon from "@mui/icons-material/CompareArrows";

type Props = {
  onClick: () => void;
};

export const CountryForm: React.FC<Props> = ({ onClick }) => {
  const [country1, setCountry1] = useState("");
  const [country2, setCountry2] = useState("");

  const handleChangeCountry1 = (event: SelectChangeEvent) => {
    setCountry1(event.target.value);
  };

  const handleChangeCountry2 = (event: SelectChangeEvent) => {
    setCountry2(event.target.value);
  };
  return (
    <Container maxWidth="lg">
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          gap: 4, // відстань між селектами
          mt: 4,
        }}
      >
        <FormControl sx={{ minWidth: 200 }} required>
          <InputLabel id="label1">Country1</InputLabel>
          <Select
            labelId="label1"
            id="country1"
            value={country1}
            label="Country1"
            onChange={handleChangeCountry1}
          >
            <MenuItem value={10}>Ukraine</MenuItem>
            <MenuItem value={20}>Country3</MenuItem>
            <MenuItem value={30}>Country4</MenuItem>
          </Select>
        </FormControl>

        <CompareArrowsIcon />

        <FormControl sx={{ minWidth: 200 }} required>
          <InputLabel id="label2">Country2</InputLabel>
          <Select
            labelId="label2"
            id="country2"
            value={country2}
            label="Country2"
            onChange={handleChangeCountry2}
          >
            <MenuItem value={40}>Country5</MenuItem>
          </Select>
        </FormControl>
        <Button variant="contained" size="large" onClick={onClick}>
          Розрахуй
        </Button>
      </Box>
    </Container>
  );
};
