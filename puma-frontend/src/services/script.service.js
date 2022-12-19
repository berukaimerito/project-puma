import authHeader from "./authHeader";
import axios from "axios";

const API_URL = "http://localhost:5000/"; // backend api

const saveScript = async (code, symbol) => {
  return axios
    .post(
      API_URL + "scripts",
      { symbol, code },
      {
        headers: {
          Authorization: authHeader().Authorization,
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
          "Content-Type": "application/json",
          "X-API-KEY": "XXX",
        },
        withCredentials: false,
      }
    )
    .then((response) => {
      console.log(response.data);
      return response.data;
    });
};

const editScript = async (symbol, code) => {
  return axios
    .post(
      API_URL + "scripts/" + symbol,
      { code },
      {
        headers: {
          Authorization: authHeader().Authorization,
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
          "Content-Type": "application/json",
          "X-API-KEY": "XXX",
        },
        withCredentials: false,
      }
    )
    .then((response) => {
      console.log(response.data);
      return response.data;
    });
};

const getScriptById = async (symbol) => {
  return axios({
    method: "get",
    url: API_URL + "scripts/" + symbol,
    headers: {
      "X-API-KEY": "XXX",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
      Authorization: authHeader().Authorization,
    },
    withCredentials: false,
  }).then((response) => {
    console.log(response.data);
    return response.data;
  });
};

const deleteById = async (symbol) => {
  return axios({
    method: "delete",
    url: API_URL + "dashboard",
    headers: {
      "Content-Type": "application/json",
      "X-API-KEY": "XXX",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
      Authorization: authHeader().Authorization,
    },
    data: { symbol },
  }).then((response) => {
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
    .post(API_URL + "dashboard", {}, { headers: authHeader() })
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
  editScript,
};

export default scriptService;
