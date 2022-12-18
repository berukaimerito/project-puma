import authHeader from "./authHeader";
import axios from "axios";

const API_URL = "http://localhost:5000/"; // backend api

const getHistoricalData = async (symbol, interval) => {
  return axios
    .post(
      API_URL + "historical_klines",
      { symbol, interval },
      { headers: authHeader() }
    )
    .then((response) => {
      //   console.log(response.data);
      return response.data;
    });
};

const binanceService = {
  getHistoricalData,
};

export default binanceService;
