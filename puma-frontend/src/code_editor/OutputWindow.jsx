import React from 'react'

const OutputWindow = ({ outputDetails }) => {
  const getOutput = () => {
    let statusId = outputDetails?.status?.id

    if (statusId === 6) {
      // compilation error
      return <pre style={{ color: 'red' }}>{atob(outputDetails?.compile_output)}</pre>
    } else if (statusId === 3) {
      return (
        <pre style={{ color: 'green' }}>
          {atob(outputDetails.stdout) !== null ? `${atob(outputDetails.stdout)}` : null}
        </pre>
      )
    } else if (statusId === 5) {
      return <pre style={{ color: 'red' }}>{`Time Limit Exceeded`}</pre>
    } else {
      return <pre>{atob(outputDetails?.stderr)}</pre>
    }
  }
  return (
    <>
      <h1>Output</h1>
      <div style={{ backgroundColor: '#1e293b', minHeight: '200px', marginBottom: '10px' }}>
        {outputDetails ? <>{getOutput()}</> : null}
      </div>
    </>
  )
}

export default OutputWindow
