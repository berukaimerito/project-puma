import React, { useEffect } from 'react'
import { Col, Row } from 'react-bootstrap'
import { Container } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'

const Portfolio = () => {
  const dispatch = useDispatch()

  useEffect(() => {
    // dispatch()
  }, [])

  return (
    <Container>
      <main
        style={{
          position: 'relative',
        }}
      >
        <h1
          style={{
            minHeight: '500px', // change in the future
          }}
        >
          Portfolio page
        </h1>
      </main>
    </Container>
  )
}

export default Portfolio
