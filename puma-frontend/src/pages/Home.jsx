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

  const { user: currentUser } = useSelector((state) => state.auth)

  useEffect(() => {
    // dispatch()
  }, [])

  const getStarted = () => {
    navigate('/login')
  }

  return (
    <main>
      <div
        className="Jumbotron-landing d-flex align-items-center min-vh-100"
        style={{ fontFamily: 'Lato' }}
      >
        <Container className="">
          <Row>
            <Col sm={6} className="text-center">
              <h1 style={{ fontSize: '4.2em', paddingTop: '60px' }}>Test your strategy</h1>
              <p style={{ fontSize: '1.2em' }}>Find out how well your bot can trade within minutes!</p>
              {
                currentUser ? (
                  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
                ) : (
                <Button variant="success" size="lg" onClick={getStarted}>
                  <h1>Get Started</h1>
                </Button>
                )
              }
              
            </Col>
            <Col sm={6}>
              <img src='/images/homepage.jpg' style={{
                maxHeight: '100%',
                maxWidth: '100%',
                backgroundSize: 'cover'
              }}/>
            </Col>
          </Row>
        </Container>
      </div>
    </main>
  )
}

export default Home
