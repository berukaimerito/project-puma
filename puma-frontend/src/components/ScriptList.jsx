import React from 'react'
import { Button, Card, Col, Row } from 'react-bootstrap'
import { useNavigate } from 'react-router'

function ScriptList({ scripts }) {
  console.log(scripts)

  const navigate = useNavigate()

  const handleUse = (id) => {
    navigate(`/script/${id}`)
  }

  const handleDelete = (id) => {
    if (window.confirm('Are you sure you want to delete this script?')) {
      console.log('delete')
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
                    <Card.Title>{script.currency}</Card.Title>
                    <Row>
                      <Col sm={6}>
                        <Button variant="primary" onClick={() => handleUse(script._id)}>
                          Use
                        </Button>
                      </Col>
                      <Col sm={6}>
                        <Button variant="danger" onClick={() => handleDelete(script._id)}>
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
