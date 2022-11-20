import React, { useEffect, useState } from 'react'
import { priceData } from './priceData'
import Chart from '@qognicafinance/react-lightweight-charts'
import { Container } from 'react-bootstrap'

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

  // binance ws api
  var binanceSocket = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@kline_1m')

  useEffect(() => {
    console.log(candlestickSeries)
    console.log(options)

    // TODO: uncomment in order to get data in real time from binance api

    // binanceSocket.onmessage = function (event) {
    //   var message = JSON.parse(event.data)

    //   var candlestick = message.k

    //   console.log(candlestick)

    //   var theTime = `${new Date(candlestick.t).getFullYear()}-${new Date(
    //     candlestick.t
    //   ).getMonth()}-${new Date(candlestick.t).getDay()}`

    //   var newData = {
    //     time: theTime,
    //     open: candlestick.o,
    //     high: candlestick.h,
    //     low: candlestick.l,
    //     close: candlestick.c,
    //   }

    //   setCandlestickSeries([
    //     {
    //       data: [...priceData, newData],
    //     },
    //   ])
    // }
  }, [])

  return (
    <div>
      <Container>
        <h1>Dashboard!</h1>
        <Chart options={options} candlestickSeries={candlestickSeries} autoWidth height={420} />
      </Container>
    </div>
  )
}

export default Dashboard

// const Dashboard = () => {
//   const chartContainerRef = useRef()
//   const chart = useRef()
//   const resizeObserver = useRef()

//   useEffect(() => {
//     chart.current = createChart(chartContainerRef.current, {
//       width: chartContainerRef.current.clientWidth / 2,
//       height: 500, //"300px", //chartContainerRef.current.clientHeight,
//       layout: {
//         backgroundColor: '#253248',
//         textColor: 'rgba(255, 255, 255, 0.9)',
//       },
//       grid: {
//         vertLines: {
//           color: '#334158',
//         },
//         horzLines: {
//           color: '#334158',
//         },
//       },
//       crosshair: {
//         mode: CrosshairMode.Normal,
//       },
//       priceScale: {
//         borderColor: '#485c7b',
//       },
//       timeScale: {
//         borderColor: '#485c7b',
//       },
//     })

//     console.log(chart.current)

//     const candleSeries = chart.current.addCandlestickSeries({
//       upColor: '#4bffb5',
//       downColor: '#ff4976',
//       borderDownColor: '#ff4976',
//       borderUpColor: '#4bffb5',
//       wickDownColor: '#838ca1',
//       wickUpColor: '#838ca1',
//     })

//     candleSeries.setData(priceData)
//   }, [priceData])

//   // Resize chart on container resizes.
//   // useEffect(() => {
//   //   resizeObserver.current = new ResizeObserver((entries) => {
//   //     const { width, height } = entries[0].contentRect
//   //     chart.current.applyOptions({ width, height })
//   //     setTimeout(() => {
//   //       chart.current.timeScale().fitContent()
//   //     }, 0)
//   //   })

//   //   resizeObserver.current.observe(chartContainerRef.current)

//   //   return () => resizeObserver.current.disconnect()
//   // }, [])

//   return (
//     <div>
//       <h1>Dashboard!ss</h1>

//       <div
//         ref={chartContainerRef}
//         className="chart-container"
//         // style={{ height: '100%' }}
//       />
//     </div>
//   )
// }

// export default Dashboard
