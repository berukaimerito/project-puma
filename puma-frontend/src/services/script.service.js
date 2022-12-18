import authHeader from "./authHeader";

// MOCK DATA
let scripts = [
  {
    _id: "1",
    currency: "BTC",
    path: "images/btc.jpeg",
    code: `/**
    * Default code.
    */
    
    
    const basicFunction = () => {
     return 20+20;
    };
    
    const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    const target = 5;
    console.log(basicFunction());
    `,
  },
  {
    _id: "2",
    currency: "ETH",
    path: "images/eth.jpeg",
    code: `/**
    * Default code.
    */
    
    
    const basicFunction = () => {
     return 1+1;
    };
    
    const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    const target = 5;
    console.log(basicFunction());
    `,
  },
];

const API_URL = "localhost:5000/"; // backend api

const saveScript = (username, email, password) => {};

const getScriptById = (symbol) => {
  return axios.get(API_URL + "scripts/" + symbol, { headers: authHeader() });
};

const deleteById = (id) => {
  let scriptObjs;
  scriptObjs = scripts.filter((script) => script._id !== id);

  return scriptObjs;
};

const getAllScripts = (id) => {
  return scripts;
};

const scriptService = {
  getScriptById,
  saveScript,
  getAllScripts,
  deleteById,
};

export default scriptService;
