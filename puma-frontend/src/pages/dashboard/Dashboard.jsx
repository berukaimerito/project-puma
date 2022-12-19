import React, { useEffect, useState } from 'react'
import Chart from '@qognicafinance/react-lightweight-charts'
import { Col, Container, Row } from 'react-bootstrap'
import { Dropdown } from 'react-bootstrap'
import ScriptList from '../../components/ScriptList'
import scriptService from '../../services/script.service'
import binanceService from '../../services/binance.service'

const Dashboard = () => {
  const [options, setOptions] = useState({
    alignLabels: true,
    timeScale: {
      rightOffset: 12,
      barSpacing: 3,
      fixLeftEdge: true,
      lockVisibleTimeRangeOnResize: true,
      rightBarStaysOnScroll: true,
      borderVisible: false,
      borderColor: '#fff000',
      visible: true,
      timeVisible: true,
      secondsVisible: false,
    },
  })

  const [candlestickSeries, setCandlestickSeries] = useState([
    // {
    //   time: `${new Date().getFullYear()}-${new Date().getMonth()}-${new Date().getDay()}`,
    //   open: 17200.34,
    //   high: 17102.99,
    //   low: 17000.57,
    //   close: 17000.85,
    // },
  ])

  const [currency, setCurrency] = useState('btcusdt')
  const [interval, setInterval] = useState('1')
  const [scripts, setScripts] = useState([])
  const [increment, setIncrement] = useState(1000)
  
  let date = 5000

  // binance ws api
  var binanceSocket = new WebSocket(
    `wss://stream.binance.com:9443/ws/${currency}@kline_${interval}m`
  )
    
  useEffect(() => {
    scriptService.getAllScripts().then((response)=> {
      let res = {
        msg: response
      }
      setScripts(res.msg === 'No scripts' ? [] : response)
    })

    binanceService.getHistoricalData(currency, `${interval}m`).then((data) => {
      setCandlestickSeries(data)
    })
   

    return () => {
      binanceSocket.close()
    }
  }, [currency, interval])

 

  // binanceSocket.onmessage = function (event) {
  //   var message = JSON.parse(event.data)

  //   var candlestick = message.k
  //   date = date + 1200
  //   console.log(date)

  //     var newData = {
  //       time: candlestick.t / 1000,
  //       open: candlestick.o,
  //       high: candlestick.h,
  //       low: candlestick.l,
  //       close: candlestick.c,
  //     }
  //     console.log(newData)
  //     console.log(candlestickSeries)
  //     // setCandlestickSeries((prevArray) => [...prevArray, newData])
   
  // }

  const selectInterval = (e) => {
    setInterval(e)
  }

  const selectCurrency = (e) => {
    setCurrency(e)
  }

  return (
    <div>
      <Container>
        <h1>Dashboard!</h1>
        <div>
          <Row>
            <Col sm={4}>
              <div style={{ marginTop: '60px' }}>
                {/* TODO: Replace with sriptcs list components */}
                <ScriptList scripts={scripts} setScripts={setScripts}></ScriptList>
              </div>
            </Col>
            <Col sm={8}>
              <div>
                <div className="d-flex justify-content-end" style={{ marginBottom: '20px' }}>
                  <Dropdown className="d-inline mx-2" onSelect={selectCurrency}>
                    <Dropdown.Toggle variant="secondary" id="dropdown-basic">
                      {currency}
                    </Dropdown.Toggle>
                    <Dropdown.Menu variant="dark">
                      <Dropdown.Item eventKey="btcusdt">BTC</Dropdown.Item>
                      <Dropdown.Item eventKey="ethusdt">ETH</Dropdown.Item>
                      <Dropdown.Item eventKey="bnbcusdt">BNB</Dropdown.Item>
                      <Dropdown.Item eventKey="xrpusdt">XRP</Dropdown.Item>
                      <Dropdown.Item eventKey="adausdt">ADA</Dropdown.Item>
                      <Dropdown.Item eventKey="solusdt">SOL</Dropdown.Item>
                      <Dropdown.Item eventKey="dogeusdt">DOGE</Dropdown.Item>
                      <Dropdown.Item eventKey="dotusdt">DOT</Dropdown.Item>
                    </Dropdown.Menu>
                  </Dropdown>
                  <Dropdown className="d-inline mx-2" onSelect={selectInterval}>
                    <Dropdown.Toggle variant="secondary" id="dropdown-basic">
                      {interval ? `${interval} min` : 'Interval'}
                    </Dropdown.Toggle>

                    <Dropdown.Menu variant="dark">
                      <Dropdown.Item eventKey="5">5 min</Dropdown.Item>
                      {/* <Dropdown.Item eventKey="10">10 min</Dropdown.Item> */}
                      <Dropdown.Item eventKey="15">15 min</Dropdown.Item>
                    </Dropdown.Menu>
                  </Dropdown>
                </div>
                <Chart
                  options={options}
                  candlestickSeries={[{ data: candlestickSeries }]}
                  autoWidth
                  height={420}
                />
              </div>
            </Col>
          </Row>
        </div>
      </Container>
    </div>
  )
}

export default Dashboard