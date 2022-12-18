import React from 'react'
import { Button, Card, Col, Row } from 'react-bootstrap'
import { useNavigate } from 'react-router'
import scriptService from '../services/script.service'

function ScriptList({ scripts }) {
  console.log(scripts)

  const navigate = useNavigate()

  const handleUse = (id) => {
    navigate(`/scripts/${id}`)
  }

  const handleDelete = (id) => {
    if (window.confirm('Are you sure you want to delete this script?')) {
      console.log('delete')
      scriptService.deleteById(id).then((data)=> console.log(data))
    }
  }

  return (
    <div>
      {scripts.length === 0 ? (
        <p>No scripts</p>
      ) : (
        <>
          <h1>My Scripts</h1>
          <Row
            lg={3}
            style={{
              maxHeight: 'calc(100vh - 210px)',
              overflowY: 'auto',
            }}
          >
            {scripts.map((script) => {
              return (
                <Card style={{ width: '18rem', marginTop: '5px' }}>
                  {/* <Card.Img variant="top" src={script.path} height={50} /> */}
                  <Card.Body>
                    <Card.Title>{script.symbol}</Card.Title>
                    <Row>
                      <Col sm={6}>
                        <Button variant="primary" onClick={() => handleUse(script.symbol)}>
                          Use
                        </Button>
                      </Col>
                      <Col sm={6}>
                        <Button variant="danger" onClick={() => handleDelete(script.symbol)}>
                          Delete
                        </Button>
                      </Col>
                    </Row>
                  </Card.Body>
                </Card>
              )
            })}
          </Row>
        </>
      )}
    </div>
  )
}

export default ScriptList
