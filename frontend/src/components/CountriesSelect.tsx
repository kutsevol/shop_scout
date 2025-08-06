import { FormControl, Select, MenuItem, FormHelperText } from "@mui/material";
import type { Country } from "../types/country";

type CustomSelectProps = {
  value: string;
  helperText: string;
  countries: Country[];
  onChange?: (value: string) => void;
};

export const CountriesSelect: React.FC<CustomSelectProps> = ({
  value,
  helperText,
  countries,
  onChange = () => {},
}) => {
  return (
    <FormControl sx={{ minWidth: 400, flexGrow: 1 }}>
      <Select
        value={value}
        onChange={(event) => onChange(event.target.value)}
        displayEmpty
        inputProps={{ "aria-label": "Without label" }}
      >
        {countries.map((country) => (
          <MenuItem value={country.name} key={country.name}>
            <span style={{ marginRight: 8 }}>{country?.emoji}</span>
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
