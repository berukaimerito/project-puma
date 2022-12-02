import React from 'react'
import { LinkContainer } from 'react-router-bootstrap'
import { Container, Nav, Navbar, NavDropdown } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import { logout } from '../slices/auth'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faGaugeHigh } from '@fortawesome/free-solid-svg-icons'
import {faCode} from '@fortawesome/free-solid-svg-icons'
import {faUser} from '@fortawesome/free-solid-svg-icons'

const Header = () => {
  const { user: currentUser } = useSelector((state) => state.auth)
  console.log(currentUser)

  const dispatch = useDispatch()

  const navigate = useNavigate()

  const logoutHandler = () => {
    dispatch(logout())
    navigate('/')
  }

  const profileHandler = () => {
    navigate('/profile')
  }

  const portfolioHandler = () => {
    navigate('/portfolio')
  }

  return (
    <header>
      <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
        <Container>
          <LinkContainer to="/">
            <Navbar.Brand>PUMA</Navbar.Brand>
          </LinkContainer>

          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="justify-content-end" style={{ width: '100%' }}>
              {
                currentUser && (
                  <LinkContainer to="/dashboard">
                    <Nav.Link>
                      <FontAwesomeIcon icon={faGaugeHigh} /> Dashboard
                    </Nav.Link>
                  </LinkContainer>
                )
              }

              {
                currentUser && (
                  <LinkContainer to="/script">
                    <Nav.Link>
                    <FontAwesomeIcon icon={faCode} /> Script
                    </Nav.Link>
                  </LinkContainer>
                )
              }

              {currentUser ? (
                <NavDropdown icon={faUser} title={currentUser.name} id="username">
                  <NavDropdown.Item onClick={logoutHandler}>Logout</NavDropdown.Item>
                  <NavDropdown.Item onClick={profileHandler}>Profile</NavDropdown.Item>
                  <NavDropdown.Item onClick={portfolioHandler}>My-Portfolio</NavDropdown.Item>
                </NavDropdown>
              ) : (
                <>
             
                  <LinkContainer to="/login">
                    <Nav.Link>
                      <i className="fas fa-user"></i> Sign In
                    </Nav.Link>
                  </LinkContainer>

                  <LinkContainer to="/register">
                    <Nav.Link className="text-primary">
                      <i className="fas fa-user-plus"></i> Sign Up
                    </Nav.Link>
                  </LinkContainer>

                </>
              )}
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  )
}

export default Header
