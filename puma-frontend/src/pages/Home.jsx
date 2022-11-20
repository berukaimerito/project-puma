import React, { useEffect } from 'react'
import { Col, Row } from 'react-bootstrap'
import { Container, Button } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHome } from '@fortawesome/free-solid-svg-icons'
import Footer from '../components/Footer'
import { useNavigate } from 'react-router'

const Home = () => {
  const dispatch = useDispatch()
  const navigate = useNavigate()

  useEffect(() => {
    // dispatch()
  }, [])

  const getStarted = () => {
    navigate('/register')
  }

  return (
    <main>
      <div
        className="Jumbotron-landing d-flex align-items-center min-vh-100"
        style={{ fontFamily: 'Lato' }}
      >
        <Container className="text-center">
          <h1 style={{ fontSize: '4.2em' }}>Test your strategy</h1>
          <p style={{ fontSize: '0.8em' }}>Find out how well your bot can trade within minutes!</p>
          <Button variant="warning" size="lg" onClick={getStarted}>
            <h1>Get Started</h1>
          </Button>
        </Container>
      </div>
    </main>
  )
}

export default Home
