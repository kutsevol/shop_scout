# 📦 Price Comparison Platform — Project Requirements

## 1. Project Overview

This platform enables users to:

- Compare product prices across different stores within a single country.
- Compare prices of product baskets between countries.
- Analyze cost of living variations based on real-time product pricing.
- Use Large Language Models (LLMs) to simplify user requests and generate structured queries.
- Save personal product lists and monitor price history and trends over time.

---

## 2. Core Features

### 🛒 Price Comparison

- **Intra-country store comparison**: View price differences for the same product basket across multiple local stores.
- **Cross-country comparison**: Compare total basket costs across countries to estimate cost-of-living differences.
- **Custom product basket**: Users can create and manage personalized product lists.
- **Real-time prices**: Data sourced regularly from real e-commerce platforms.

### 🤖 LLM-Powered Query Engine

- Use of LLM agents to understand and transform user input (text/voice) into SQL-based or API-ready queries.
- Supports advanced filtering, sorting, aggregations (e.g., "Find cheapest vegetables in EU").
- Future integration possible with chatbot-style UX.
- Potential frameworks: OpenAI, Mistral, Ollama, etc.

### 👤 User Accounts & Personalized Experience

- **Authentication & authorization**: User account creation, login/logout, JWT-based session management.
- **Search & basket history**: Store and view history of comparisons and user interactions.
- **Price trends**: Track historical price changes for selected products.
- **Notifications (optional)**: Alert users when tracked product prices change.

---

## 3. System Architecture & Stack

### 📊 Backend

- **Language**: Python
- **Framework**: FastAPI
- **Main responsibilities**:
  - Serve API for product/basket data.
  - Basket comparison (intra-country and cross-country).
  - Handle user registration and authentication.
  - Process smart queries from LLM agents.
- **Security**: Input validation, rate limiting, and protection of user data.

### ⚙️ Data Layer (ETL/ELT)

- **Pipeline system**:
  - Periodically scrape or fetch store data via APIs or parsers.
  - Normalize and transform raw data for internal use.
  - Scheduling via Celery, cron, or cloud scheduler.
- **Storage**: PostgreSQL / Data warehouse solution.
- **Monitoring**: Logging + alerting on failures or outdated data feeds.

### 🖥️ Frontend

- **Language**: JavaScript
- **Framework**: React
- **Features**:
  - Basket creation & editing.
  - Store/region/country selection UI.
  - Comparison visualizations: tables, charts, maps.
  - User dashboard with price graphs, basket history, and LLM interaction.
- **Responsive design**: Mobile-first, compatible with major browsers.

---

## 4. Non-Functional Requirements

- **Scalability**: Designed for expansion across new countries and store sources.
- **Performance**: Efficient data loading and responsiveness.
- **Data freshness**: Prices updated on a regular schedule, timestamped.
- **Localization**: Multi-language support (e.g. EN, UA).
- **Availability**: Minimize downtime through retries and monitoring.
- **Security**:
  - Encrypted passwords, session-based auth (JWT).
  - Secure API routes.

---

## 5. Optional Integrations

- Public APIs from retail stores (where available).
- Web scrapers with anti-bot handling for data collection.
- Integration with government/proxy APIs for auxiliary data (e.g., inflation rates).
- BI/analytics dashboards for admin use in the future.

---

## 6. Future Enhancements

- Collaborative/shared baskets.
- Community-reported price validation.
- Location detection for local pricing.
- Export results (CSV/Excel/PDF).
- Integration with payment/checkout (stretch goal).
