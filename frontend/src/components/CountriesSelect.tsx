import {
  FormControl,
  Select,
  MenuItem,
  FormHelperText,
  type SelectChangeEvent,
  Typography,
} from "@mui/material";
import type { Country } from "../types/country";
import { useState } from "react";

type CountriesSelectProps = {
  value: string;
  helperText: string;
  countries: Country[];
  onCountryChange?: (value: string) => void;
};

export const CountriesSelect = ({
  value,
  helperText,
  countries,
  onCountryChange = () => {},
}: CountriesSelectProps) => {
  const [valueSelect, setValueSelect] = useState(value);

  const handleCountryChange = (event: SelectChangeEvent) => {
    setValueSelect(event.target.value);
    onCountryChange(event.target.value);
  };

  return (
    <FormControl sx={{ minWidth: 400, flexGrow: 1 }}>
      <Select
        value={valueSelect}
        onChange={handleCountryChange}
        displayEmpty
        inputProps={{ "aria-label": "Without label" }}
      >
        {countries.map((country) => (
          <MenuItem value={country.name} key={country.name}>
            <Typography component="span" sx={{ marginRight: 1 }}>
              {country?.emoji}
            </Typography>
            {country.name}
          </MenuItem>
        ))}
      </Select>
      <FormHelperText sx={{ color: "primary.contrastText", marginLeft: 0 }}>
        {helperText}
      </FormHelperText>
    </FormControl>
  );
};
