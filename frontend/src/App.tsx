import { useEffect, useRef, useState } from "react";
import "./App.css";

import { HeroSection } from "./components/HeroSection";
import { ProductsList } from "./components/ProductsList";

import { MainActions } from "./components/MainActions/MainActions";
import { Footer } from "./components/Footer/Footer";
import { CountryForm } from "./components/CountryForm";
import ResultTable from "./components/ResultTable";

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
          <ProductsList />
          <CountryForm onClick={handleShowResultClick} />

          {showResult && (
            <div ref={tableRef}>
              <ResultTable />
            </div>
          )}
        </div>
      )}

      <Footer />
    </>
  );
}

export default App;
