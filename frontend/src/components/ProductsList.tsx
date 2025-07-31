import { Box, Checkbox, FormControlLabel, FormGroup } from "@mui/material";

import Accordion from "@mui/material/Accordion";
import AccordionDetails from "@mui/material/AccordionDetails";
import AccordionSummary from "@mui/material/AccordionSummary";
import Typography from "@mui/material/Typography";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";

const PRODUCTS = [
  {
    id: 1,
    name: "Bread",
    category: "CategoryName1",
  },
  {
    id: 2,
    name: "Bread2",
    category: "CategoryName1",
  },
  {
    id: 3,
    name: "Bread3",
    category: "CategoryName1",
  },
  {
    id: 4,
    name: "Milk",
    category: "CategoryName2",
  },
  {
    id: 5,
    name: "Milk2",
    category: "CategoryName2",
  },
  {
    id: 6,
    name: "Milk3",
    category: "CategoryName2",
  },
];

const categories = [...new Set(PRODUCTS.map((item) => item.category))];

export const ProductsList = () => {
  return (
    <Box
      sx={{
        display: "inline-block",
        width: "100%",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <div>
        {categories.map((category) => (
          <Accordion key={category}>
            <AccordionSummary
              expandIcon={<ExpandMoreIcon />}
              aria-controls="panel1-content"
              id="panel1-header"
            >
              <Typography component="span">{category}</Typography>
            </AccordionSummary>
            <AccordionDetails>
              <FormGroup>
                {PRODUCTS.filter(
                  (product) => product.category === category
                ).map((product) => (
                  <FormControlLabel
                    key={product.id}
                    control={<Checkbox />}
                    label={product.name}
                  />
                ))}
              </FormGroup>
            </AccordionDetails>
          </Accordion>
        ))}
      </div>
    </Box>
  );
};
