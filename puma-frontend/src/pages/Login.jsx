import React, { useState, useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Form, Button, Row, Col } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import FormContainer from '../components/FormContainer'
import { login } from '../slices/auth'

const reload = () => window.location.reload()

const Login = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const dispatch = useDispatch()

  const { isLoggedIn, loading, user: currentUser } = useSelector((state) => state.auth)

  const navigate = useNavigate()

  useEffect(() => {
    if (isLoggedIn && currentUser.name) {
      navigate('/dashboard')
      // reload()
    }
    
  }, [isLoggedIn,navigate])

  const submitHandler = (e) => {
    e.preventDefault()
    dispatch(login({ email, password }))
  }

  return (
    <FormContainer>
      <h1>Sign In</h1>
      <Form onSubmit={submitHandler}>
        <Form.Group controlId="username">
          <Form.Label>Username</Form.Label>
          <Form.Control
            type="username"
            placeholder="Enter username"
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

        <br />
        <div className="d-grid gap-2">
        <Button type="submit" variant="dark" size="lg" style={{marginTop: "20px"}}>
          Login
        </Button>
        </div>
      </Form>

      <Row className="py-3">
        <Col>
          New Customer? <Link to={'/register'}>Register</Link>
        </Col>
      </Row>
    </FormContainer>
  )
}

export default Login
