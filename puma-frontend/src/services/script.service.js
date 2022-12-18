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

const getScriptById = async (symbol) => {
  return axios
    .get(API_URL + "scripts/" + symbol, { headers: authHeader() })
    .then((response) => {
      console.log(response.data);
      return response.data;
    });
};

const deleteById = async (symbol) => {
  return axios.delete(API_URL + "scripts/" + symbol).then((response) => {
    console.log(response.data);
    return response.data;
  });
};

const runScript = async (symbol) => {
  return axios.post(API_URL + "scripts/" + symbol + "/run").then((response) => {
    console.log(response.data);
    return response.data;
  });
};

const stopScript = async (symbol) => {
  return axios
    .post(API_URL + "scripts/" + symbol + "/stop")
    .then((response) => {
      console.log(response.data);
      return response.data;
    });
};

const getAllScripts = async () => {
  return axios
    .get(API_URL + "scripts", { headers: authHeader() })
    .then((response) => {
      console.log(response.data);
      return response.data;
    });
};

const scriptService = {
  getScriptById,
  saveScript,
  getAllScripts,
  deleteById,
  runScript,
  stopScript,
};

export default scriptService;
