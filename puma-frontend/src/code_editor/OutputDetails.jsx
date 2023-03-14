import React from 'react'

const OutputDetails = ({ outputDetails }) => {
  console.log(outputDetails)
  return (
    <div style={{ marginTop: '20px' }}>
      <p>
        Status: <span>{outputDetails?.status?.description}</span>
      </p>
      <p className="text-sm">
        Memory: <span>{outputDetails?.memory}</span>
      </p>
      <p className="text-sm">
        Time: <span>{outputDetails?.time}</span>
      </p>
    </div>
  )
}

export default OutputDetails
