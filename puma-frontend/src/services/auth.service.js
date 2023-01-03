import axios from "axios";
import authHeader from "./authHeader";

const API_URL = "http://localhost:5000/"; // backend api

const editProfile = async (name, password) => {
  return axios
    .put(
      API_URL + "profile",
      {
        username: name,
        password,
      },
      { headers: authHeader() }
    )
    .then((response) => {
      return response.data;
    });
};

const register = async (name, surname, email, password, confirmPassword) => {
  return axios
    .post(API_URL + "register", {
      username: name,
      surname,
      email,
      password,
      confirm: confirmPassword,
    })
    .then((response) => {
      return response.data;
    });
};

const login = async (username, password) => {
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
  editProfile,
};

export default authService;
