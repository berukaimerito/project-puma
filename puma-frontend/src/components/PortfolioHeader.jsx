import React from 'react'
import { Row, Card } from 'react-bootstrap'

function PortfolioHeader() {
  return (
    <div>
      <Row lg={3}>
        <Card style={{ width: '18rem' }}>
          <Card.Body>
            <Card.Title>$ 12000</Card.Title>
            <Card.Subtitle className="mb-2 text-muted">Toatal Balance</Card.Subtitle>
          </Card.Body>
        </Card>
        <Card style={{ width: '18rem' }}>
          <Card.Body>
            <Card.Title>$ 490</Card.Title>
            <Card.Subtitle className="mb-2 text-muted">
              24hr portfolio change <p style={{ color: 'green' }}>(+2.35%)</p>
            </Card.Subtitle>
          </Card.Body>
        </Card>
        <Card style={{ width: '18rem' }}>
          <Card.Body>
            <Card.Title>-$18</Card.Title>
            <Card.Subtitle className="mb-2 text-muted">
              Total profit loss <p style={{ color: 'red' }}>(-0.25%)</p>
            </Card.Subtitle>
          </Card.Body>
        </Card>
      </Row>
    </div>
  )
}

export default PortfolioHeader
