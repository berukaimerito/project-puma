import authHeader from "./authHeader";
import axios from "axios";

const API_URL = "http://localhost:5000/"; // backend api

//TODO
// PROPER WAY TO GET WS STREAM

// var binanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_1m");

// binanceSocket.onmessage = function (event) {
// 	var message = JSON.parse(event.data);

// 	var candlestick = message.k;

// 	candleSeries.update({
// 		time: candlestick.t / 1000,
// 		open: candlestick.o,
// 		high: candlestick.h,
// 		low: candlestick.l,
// 		close: candlestick.c
// 	})
// }

const getHistoricalData = async (symbol, interval) => {
  return axios
    .post(
      API_URL + "historical_klines",
      { symbol, interval },
      { headers: authHeader() }
    )
    .then((response) => {
      return response.data;
    });
};

const binanceService = {
  getHistoricalData,
};

export default binanceService;
