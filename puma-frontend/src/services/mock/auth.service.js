// MOCK DATA
let users = [
  {
    _id: 1,
    email: 'bora@example.com',
    password: '123',
  },
  {
    _id: 2,
    email: 'boratest@example.com',
    password: '123',
  },
]

const API_URI = 'localhost:5000/users' // backend api

const register = (username, email, password) => {}

const login = (email, password) => {
  users.map((user) => {
    if (user.email === email && user.password === password) {
      localStorage.setItem('user', JSON.stringify(user))
      return user
    }
    return {}
  })
}

const logout = () => {
  localStorage.removeItem('user')
}

const authService = {
  register,
  login,
  logout,
}

export default authService
