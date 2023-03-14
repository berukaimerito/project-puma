import React, { useEffect } from 'react'
import { Col, Row } from 'react-bootstrap'
import { Container } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Landing from '../code_editor/Landing'

const Script = () => {
  const dispatch = useDispatch()

  useEffect(() => {
    // dispatch()
  }, [])

  return (
    <Container>
      <Landing/>
    </Container>
  )
}

export default Script
