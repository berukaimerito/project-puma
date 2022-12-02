// MOCK DATA
let portfolio = {
  _id: 1,
  user: {
    _id: 1,
    name: "Sibora",
    email: "bora@example.com",
    password: "123",
  },
  symbol: "BTCUSDT",
  amount: "10000",
  current_prices: [],
};

const API_URI = "localhost:5000/portfolio"; // backend api

const portfolioData = () => {
  return portfolio;
};

const portfolioService = { portfolioData };

export default portfolioService;
