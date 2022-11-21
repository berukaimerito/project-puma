import React, { useEffect, useState } from 'react'
import { Container } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Chart from '@qognicafinance/react-lightweight-charts'
import PortfolioHeader from '../components/PortfolioHeader'

// mock data portfolio
const portfolioData = [
  { time: { year: 2018, month: 9, day: 23 }, value: 18.586765395788515 },
  { time: { year: 2018, month: 9, day: 24 }, value: 16.67923813275883 },
  { time: { year: 2018, month: 9, day: 25 }, value: 18.139367606990206 },
  { time: { year: 2018, month: 9, day: 26 }, value: 19.175341064495118 },
  { time: { year: 2018, month: 9, day: 27 }, value: 17.026133664805055 },
  { time: { year: 2018, month: 9, day: 28 }, value: 17.862891721122114 },
  { time: { year: 2018, month: 9, day: 29 }, value: 18.307393426640242 },
  { time: { year: 2018, month: 9, day: 30 }, value: 20.870050581795134 },
  { time: { year: 2018, month: 10, day: 1 }, value: 19.004329503393258 },
  { time: { year: 2018, month: 10, day: 2 }, value: 19.442993891919564 },
  { time: { year: 2018, month: 10, day: 3 }, value: 19.104414198492133 },
  { time: { year: 2018, month: 10, day: 4 }, value: 22.075521421139175 },
  { time: { year: 2018, month: 10, day: 5 }, value: 19.100220372613407 },
  { time: { year: 2018, month: 10, day: 6 }, value: 20.66834030878228 },
  { time: { year: 2018, month: 10, day: 7 }, value: 19.833283354440272 },
]

const Portfolio = () => {
  // const [options, setOptions] = useState({
  //   // adsasd
  // })

  // const [candlestickSeries, setCandlestickSeries] = useState([
  //   {
  //     data: '',
  //   },
  // ])

  const options = {
    timeScale: {
      tickMarkFormatter: (time) => {
        const date = new Date(time.year, time.month, time.day)
        const formattedTick =
          date.getFullYear() + '/' + (date.getMonth() + 1) + '/' + date.getDate()
        console.log({ formattedTick })
        return formattedTick
      },
    },
  }

  const lineSeries = [
    {
      data: portfolioData,
      options: {
        title: 'Portfolio Value',
      },
    },
  ]

  useEffect(() => {}, [])

  return (
    <div>
      <Container>
        <h1>Portfolio</h1>
        <PortfolioHeader />
        <div>
          <div
            className="d-flex justify-content-start"
            style={{ marginBottom: '20px', height: '200px' }}
          >
            The table .....
          </div>
          <h3>Profit historical data</h3>
          <Chart options={options} lineSeries={lineSeries} autoWidth height={400} />
          <br />
          <br />
        </div>
      </Container>
    </div>
  )
}
export default Portfolio
