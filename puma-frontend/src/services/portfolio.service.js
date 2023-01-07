import axios from "axios";
import authHeader from "./authHeader";

const API_URL = "http://localhost:5000/"; // backend api

const getPortfolioById = async () => {
  return axios({
    method: "get",
    url: API_URL + "dashboard/portfolio",
    headers: {
      "X-API-KEY": "XXX",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
      Authorization: authHeader().Authorization,
    },
    withCredentials: false,
  }).then((response) => {
    console.log(response);
    return response.data;
  });
};

const portfolioService = {
  getPortfolioById,
};

export default portfolioService;
