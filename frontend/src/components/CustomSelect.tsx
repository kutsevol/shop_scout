import { FormControl, Select, MenuItem, FormHelperText } from "@mui/material";

type CustomSelectProps = {
  value: string;
  helperText: string;
  data: string[];
  onChange?: (value: string) => void;
};
export const CustomSelect: React.FC<CustomSelectProps> = ({
  value,
  helperText,
  data,
  onChange = () => {},
}) => {
  return (
    <FormControl sx={{ minWidth: 400, flexGrow: 1 }}>
      <FormHelperText sx={{ color: "primary.contrastText" }}>
        {helperText}
      </FormHelperText>
      <Select
        value={value}
        onChange={(event) => onChange(event.target.value)}
        displayEmpty
        inputProps={{ "aria-label": "Without label" }}
      >
        {data.map((item) => (
          <MenuItem value={item} key={item}>
            {item}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
};
