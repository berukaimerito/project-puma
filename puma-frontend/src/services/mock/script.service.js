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
    `,
  },
];

const API_URI = "localhost:5000/users"; // backend api

const saveScript = (username, email, password) => {};

const getScriptById = (id) => {
  let scriptObj;
  scriptObj = scripts.filter((script) => script._id === id);

  return scriptObj;
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
