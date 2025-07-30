import {
  Box,
  Checkbox,
  Container,
  FormControlLabel,
  FormGroup,
  Grow,
  Paper,
} from "@mui/material";

import Accordion from "@mui/material/Accordion";
import AccordionDetails from "@mui/material/AccordionDetails";
import AccordionSummary from "@mui/material/AccordionSummary";
import Typography from "@mui/material/Typography";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import { useState } from "react";

export const ProductsList = () => {
  const checked = true;

  const [expanded, setExpanded] = useState<string | false>(false);

  const handleChange =
    (panel: string) => (event: React.SyntheticEvent, isExpanded: boolean) => {
      setExpanded(isExpanded ? panel : false);
    };

  return (
    <>
      <Container maxWidth="lg">
        <Box
          sx={{
            position: "flex",
            width: "100%",
            marginTop: 5,
          }}
        >
          <Grow in={checked}>
            <div>
              <Accordion>
                <AccordionSummary
                  expandIcon={<ExpandMoreIcon />}
                  aria-controls="panel2-content"
                  id="panel2-header"
                >
                  <Typography component="span">Випічка</Typography>
                </AccordionSummary>
                <AccordionDetails>
                  <Typography>
                    <FormGroup>
                      <FormControlLabel control={<Checkbox />} label="Хліб" />
                      <FormControlLabel control={<Checkbox />} label="Пончик" />
                      <FormControlLabel
                        control={<Checkbox />}
                        label="Круассан"
                      />
                    </FormGroup>
                  </Typography>
                </AccordionDetails>
              </Accordion>
              <Accordion>
                <AccordionSummary
                  expandIcon={<ExpandMoreIcon />}
                  aria-controls="panel2-content"
                  id="panel2-header"
                >
                  <Typography component="span">Молочка</Typography>
                </AccordionSummary>
                <AccordionDetails>
                  <Typography>
                    <FormGroup>
                      <FormControlLabel control={<Checkbox />} label="Молоко" />
                      <FormControlLabel control={<Checkbox />} label="Творог" />
                      <FormControlLabel control={<Checkbox />} label="Сир" />
                    </FormGroup>
                  </Typography>
                </AccordionDetails>
              </Accordion>
            </div>
          </Grow>
        </Box>
      </Container>
    </>
  );
};
