// MOCK DATA
// mock data currencies

const portfolio = {
  totalBalance: 30000,
  totalProfitLoss: 60.93,
  last24hChange: 120,
};

// mock data portfolio
const portfolioHistoricalData = [
  { time: { year: 2018, month: 9, day: 23 }, value: 18.586765395788515 },
  { time: { year: 2018, month: 9, day: 24 }, value: 16.67923813275883 },
  { time: { year: 2018, month: 9, day: 25 }, value: 18.139367606990206 },
  { time: { year: 2018, month: 9, day: 26 }, value: 19.175341064495118 },
  { time: { year: 2018, month: 9, day: 27 }, value: 17.026133664805055 },
  { time: { year: 2018, month: 9, day: 28 }, value: 17.862891721122114 },
  { time: { year: 2018, month: 9, day: 29 }, value: 18.307393426640242 },
  { time: { year: 2018, month: 9, day: 30 }, value: 20.870050581795134 },
  { time: { year: 2018, month: 10, day: 1 }, value: 19.004329503393258 },
  { time: { year: 2018, month: 10, day: 2 }, value: 19.442993891919564 },
  { time: { year: 2018, month: 10, day: 3 }, value: 19.104414198492133 },
  { time: { year: 2018, month: 10, day: 4 }, value: 22.075521421139175 },
  { time: { year: 2018, month: 10, day: 5 }, value: 19.100220372613407 },
  { time: { year: 2018, month: 10, day: 6 }, value: 20.66834030878228 },
  { time: { year: 2018, month: 10, day: 7 }, value: 19.833283354440272 },
];

const currencies = [
  {
    name: "BTC",
    price: 20000,
    change24h: -3.6,
    holdings: 5000,
    avgBuyPrice: 200,
    profitOrLoss: +3.2,
    currencyHistoricalData: [
      { time: { year: 2021, month: 9, day: 23 }, value: 18.586765395788515 },
      { time: { year: 2021, month: 9, day: 24 }, value: 16.67923813275883 },
      { time: { year: 2021, month: 9, day: 25 }, value: 18.139367606990206 },
      { time: { year: 2021, month: 9, day: 26 }, value: 19.175341064495118 },
      { time: { year: 2021, month: 9, day: 27 }, value: 17.026133664805055 },
      { time: { year: 2021, month: 9, day: 28 }, value: 17.862891721122114 },
      { time: { year: 2021, month: 9, day: 29 }, value: 18.307393426640242 },
      { time: { year: 2021, month: 9, day: 30 }, value: 20.870050581795134 },
      { time: { year: 2021, month: 10, day: 1 }, value: 19.004329503393258 },
      { time: { year: 2021, month: 10, day: 2 }, value: 19.442993891919564 },
      { time: { year: 2021, month: 10, day: 3 }, value: 19.104414198492133 },
      { time: { year: 2021, month: 10, day: 4 }, value: 22.075521421139175 },
      { time: { year: 2021, month: 10, day: 5 }, value: 19.100220372613407 },
      { time: { year: 2021, month: 10, day: 6 }, value: 20.66834030878228 },
      { time: { year: 2021, month: 10, day: 7 }, value: 19.833283354440272 },
    ],
  },
  {
    name: "ETH",
    price: 1000,
    change24h: +2.6,
    holdings: 1000,
    avgBuyPrice: 300,
    profitOrLoss: +6.2,
    currencyHistoricalData: [
      { time: { year: 2022, month: 9, day: 23 }, value: 18.586765395788515 },
      { time: { year: 2022, month: 9, day: 24 }, value: 16.67923813275883 },
      { time: { year: 2022, month: 9, day: 25 }, value: 18.139367606990206 },
      { time: { year: 2022, month: 9, day: 26 }, value: 19.175341064495118 },
      { time: { year: 2022, month: 9, day: 27 }, value: 17.026133664805055 },
      { time: { year: 2022, month: 9, day: 28 }, value: 17.862891721122114 },
      { time: { year: 2022, month: 9, day: 29 }, value: 18.307393426640242 },
      { time: { year: 2022, month: 9, day: 30 }, value: 20.870050581795134 },
      { time: { year: 2022, month: 10, day: 1 }, value: 19.004329503393258 },
      { time: { year: 2022, month: 10, day: 2 }, value: 19.442993891919564 },
      { time: { year: 2022, month: 10, day: 3 }, value: 19.104414198492133 },
      { time: { year: 2022, month: 10, day: 4 }, value: 22.075521421139175 },
      { time: { year: 2022, month: 10, day: 5 }, value: 19.100220372613407 },
      { time: { year: 2022, month: 10, day: 6 }, value: 20.66834030878228 },
      { time: { year: 2022, month: 10, day: 7 }, value: 19.833283354440272 },
    ],
  },
];

const API_URI = "localhost:5000/users"; // backend api

const getPortfolioById = (id) => {
  return { portfolio, portfolioHistoricalData, currencies };
};

const portfolioService = {
  getPortfolioById,
};

export default portfolioService;

// // MOCK DATA
// let portfolio = {
//   _id: 1,
//   user: {
//     _id: 1,
//     name: "Sibora",
//     email: "bora@example.com",
//     password: "123",
//   },
//   symbol: "BTCUSDT",
//   amount: "10000",
//   current_prices: [],
// };

// const API_URI = "localhost:5000/portfolio"; // backend api

// const portfolioData = () => {
//   return portfolio;
// };

// const portfolioService = { portfolioData };

// export default portfolioService;
