import axios from "axios";

const API_URL = "http://localhost:5000/"; // backend api

const register = (name, surname, email, password, confirmPassword) => {
  console.log(name, surname, email, password, confirmPassword);
  return axios.post(API_URL + "register", {
    username: name,
    surname,
    email,
    password,
  });
};

const login = async (username, password) => {
  console.log(username);
  return axios
    .post(API_URL + "login", {
      username: username,
      password: password,
    })
    .then((response) => {
      if (response.data.accessToken) {
        localStorage.setItem("user", JSON.stringify(response.data));
      }
      console.log(response.data);
      return response.data;
    });
};

// const login = (email, password) => {
//   users.map((user) => {
//     if (user.email === email && user.password === password) {
//       localStorage.setItem("user", JSON.stringify(user));
//       return user;
//     }
//     return {};
//   });
// };

const logout = () => {
  localStorage.removeItem("user");
};

const authService = {
  register,
  login,
  logout,
};

export default authService;
