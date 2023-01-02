import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Form, Button, Row, Col } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import FormContainer from '../components/FormContainer'
import Message from '../components/Message'
import authService from '../services/auth.service'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const reload = () => window.location.reload()

const Register = () => {
  const { isLoggedIn, loading, user: currentUser } = useSelector((state) => state.auth)

  const [name, setName] = useState(currentUser ? currentUser.name : '')
  const [surname, setSurname] = useState(currentUser ? currentUser.surname : '')
  const [email, setEmail] = useState(currentUser ? currentUser.email : '')
  
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [message, setMessage] = useState(null)

  const dispatch = useDispatch()

  //   const userRegister = useSelector((state) => state.userRegister)
  //   const { loading, error, userInfo } = userRegister

  useEffect(() => {
    // if (userInfo) {
    //   //   history.push(redirect)
    // }
  }, [])

  const submitHandler = (e) => {
    e.preventDefault()
    if (password !== confirmPassword) {
      setMessage('Passwords do not match')
    } else {
      authService.editProfile(name,password).then(data=>{
        console.log(data)
        toast("Profile Edited!")
      })
    }
  }

  return (
    <FormContainer>
      <h1>Edit profile</h1>
      {message && <Message variant="danger">{message}</Message>}
      <Form onSubmit={submitHandler}>
      <Row lg={2}>
        <Form.Group controlId="name">
          <Form.Label>Name</Form.Label>
          <Form.Control
            type="name"
            placeholder="Enter name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          ></Form.Control>
        </Form.Group>

        <Form.Group controlId="surname">
          <Form.Label>Surname</Form.Label>
          <Form.Control
            type="surname"
            placeholder="Enter surname"
            value={surname}
            onChange={(e) => setSurname(e.target.value)}
          ></Form.Control>
        </Form.Group>
        </Row>
        <Form.Group controlId="email">
          <Form.Label>Email Address</Form.Label>
          <Form.Control
            type="email"
            placeholder="Enter email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          ></Form.Control>
        </Form.Group>

        <Form.Group controlId="password">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="Enter password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          ></Form.Control>
        </Form.Group>

        <Form.Group controlId="confirmPassword">
          <Form.Label>Confirm Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="Confirm password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          ></Form.Control>
        </Form.Group>
        <br />
        <div className="d-grid gap-2">
        <Button type="submit" variant="dark" size="lg">
          Edit
        </Button>
        </div>
      </Form>
      <ToastContainer />
    </FormContainer>
    
  )
}

export default Register
