import axios from "axios";

const API_URL = "http://localhost:5000/"; // backend api

const register = async (name, surname, email, password, confirmPassword) => {
  console.log(name, surname, email, password, confirmPassword);
  return axios
    .post(API_URL + "register", {
      username: name,
      surname,
      email,
      password,
      confirm: confirmPassword,
    })
    .then((response) => {
      console.log(response);
      return response.data;
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
      const user = { ...response.data[0], accessToken: response.data[1] };
      if (user.accessToken) {
        localStorage.setItem("user", JSON.stringify(user));
      }

      return user;
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
