import axios from "axios";
import authHeader from "./authHeader";

const API_URL = "http://localhost:5000/"; // backend api

const getPortfolioById = async () => {
  return axios
    .get(API_URL + "dashboard/portfolio", { headers: authHeader() })
    .then((response) => {
      console.log(response);
      console.log("1111");
      return response.data;
    });
};

const portfolioService = {
  getPortfolioById,
};

export default portfolioService;
