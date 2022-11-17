import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Footer from './components/Footer'
import Header from './components/Header'
import Dashboard from './pages/Dashboard'
import Home from './pages/Home'
import Login from './pages/Login'
import Portfolio from './pages/Portfolio'
import Profile from './pages/Profile'
import Register from './pages/Register'

import './App.css'
import Script from './pages/Script'

function App() {
  return (
    <Router>
      <Header />
      <main>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/portfolio" element={<Portfolio />} />
          <Route path="/script" element={<Script />} />
        </Routes>
      </main>
    </Router>
  )
}

export default App

