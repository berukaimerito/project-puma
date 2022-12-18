import authHeader from "./authHeader";
import axios from "axios";

const API_URL = "http://localhost:5000/"; // backend api

const saveScript = async (username, script, symbol, interval) => {
  return axios
    .post(
      API_URL + "scripts",
      { username, script, symbol, interval },
      { headers: authHeader() }
    )
    .then((response) => {
      console.log(response.data);
      return response.data;
    });
};

const getScriptById = (symbol) => {
  return axios.get(API_URL + "scripts/" + symbol, { headers: authHeader() });
};

const deleteById = (symbol) => {
  return axios.delete(API_URL + "scripts/" + symbol);
};

const getAllScripts = (id) => {
  return axios.get(API_URL + "scripts", { headers: authHeader() });
};

const scriptService = {
  getScriptById,
  saveScript,
  getAllScripts,
  deleteById,
};

export default scriptService;
