import React, { useEffect, useState } from 'react'
import { priceData } from './priceData'
import Chart from '@qognicafinance/react-lightweight-charts'
import { Col, Container, Row } from 'react-bootstrap'
import { Dropdown } from 'react-bootstrap'
import ScriptList from '../../components/ScriptList'

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
    {
      data: priceData,
    },
  ])

  const [currency, setCurrency] = useState('')
  const [interval, setInterval] = useState('')

  // binance ws api
  var binanceSocket = new WebSocket(
    `wss://stream.binance.com:9443/ws/${currency}@kline_${interval}m`
  )

  useEffect(() => {
    console.log(candlestickSeries)
    console.log(options)

    console.log(interval)
    console.log(currency)

    // TODO: uncomment in order to get data in real time from binance api

    binanceSocket.onmessage = function (event) {
      var message = JSON.parse(event.data)

      var candlestick = message.k

      console.log(candlestick)

      var theTime = `${new Date(candlestick.t).getFullYear()}-${new Date(
        candlestick.t
      ).getMonth()}-${new Date(candlestick.t).getDay()}`

      var newData = {
        time: theTime,
        open: candlestick.o,
        high: candlestick.h,
        low: candlestick.l,
        close: candlestick.c,
      }

      setCandlestickSeries([
        {
          data: [...priceData, newData],
        },
      ])
    }

    return () => {
      binanceSocket.close()
    }
  }, [currency, interval])

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
                <ScriptList></ScriptList>
              </div>
            </Col>
            <Col sm={8}>
              <div>
                <div className="d-flex justify-content-end" style={{ marginBottom: '20px' }}>
                  <Dropdown className="d-inline mx-2" onSelect={selectCurrency}>
                    <Dropdown.Toggle variant="secondary" id="dropdown-basic">
                      {currency ? (currency === 'btcusdt' ? 'BTC' : 'ETH') : 'Currency'}
                    </Dropdown.Toggle>

                    <Dropdown.Menu variant="dark">
                      <Dropdown.Item eventKey="btcusdt">BTC</Dropdown.Item>
                      <Dropdown.Item eventKey="ethusdt">ETH</Dropdown.Item>
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
                  candlestickSeries={candlestickSeries}
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

