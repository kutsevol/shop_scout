import { useEffect, useRef, useState } from "react";
import "./App.css";

import { Container, Paper, Stack } from "@mui/material";

import { HeroSection } from "./components/HeroSection";
import { ProductsList } from "./components/ProductsList";
import { MainActions } from "./components/MainActions/MainActions";
import { Footer } from "./components/Footer/Footer";
import { CountryForm } from "./components/CountryForm";
import { ResultTable } from "./components/ResultTable";

function App() {
  const [createBasket, setCreateBasket] = useState(false);
  const productsRef = useRef<HTMLDivElement>(null);

  const [showResult, setShowResult] = useState(false);
  const tableRef = useRef<HTMLDivElement>(null);

  const handleCreateBasketClick = () => {
    setCreateBasket(true);
  };

  const handleShowResultClick = () => {
    setShowResult(true);
  };

  useEffect(() => {
    if (createBasket && productsRef.current) {
      productsRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [createBasket]);

  return (
    <>
      {/* <Header /> */}
      <HeroSection onClick={handleCreateBasketClick} />

      <MainActions onClick={handleCreateBasketClick} />

      {createBasket && (
        <div ref={productsRef}>
          <Container maxWidth="lg">
            <Paper
              elevation={3}
              sx={{
                borderRadius: 4,
                backgroundColor: "rgba(239, 239, 239, 0.9)",
                margin: 5,
                padding: 5,
              }}
            >
              <Stack spacing={4}>
                <ProductsList />
                <CountryForm onClick={handleShowResultClick} />
              </Stack>

              {showResult && (
                <div ref={tableRef}>
                  <ResultTable />
                </div>
              )}
            </Paper>
          </Container>
        </div>
      )}

      <Footer />
    </>
  );
}

export default App;
