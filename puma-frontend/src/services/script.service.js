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
      return response.data;
    });
};

const getScriptById = async (symbol) => {
  return axios({
    method: "post",
    url: API_URL + "scripts-by/" + symbol,
    headers: {
      "X-API-KEY": "XXX",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
      Authorization: authHeader().Authorization,
    },
    data: {},
    withCredentials: false,
  }).then((response) => {
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
    return response.data;
  });
};

const runScript = async (symbol, code) => {
  return axios({
    method: "post",
    url: API_URL + "scripts/" + symbol + "/run",
    headers: {
      "Content-Type": "application/json",
      "X-API-KEY": "XXX",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
      Authorization: authHeader().Authorization,
    },
    data: {
      symbol,
      code,
    },
  }).then((response) => {
    return response.data;
  });
};


const stopScript = async (symbol, code) => {
  return axios({
    method: "post",
    url: API_URL + "scripts/" + symbol + "/stop",
    headers: {
      "Content-Type": "application/json",
      "X-API-KEY": "XXX",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
      Authorization: authHeader().Authorization,
    },
    data: {
      symbol,
      code,
    },
  }).then((response) => {
    return response.data;
  });
};


const getAllScripts = async () => {
  return axios
    .post(API_URL + "dashboard", {}, { headers: authHeader() })
    .then((response) => {
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
