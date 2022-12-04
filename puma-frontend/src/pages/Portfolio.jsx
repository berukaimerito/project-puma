import React, { useEffect, useState } from 'react'
import { Container } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Chart from '@qognicafinance/react-lightweight-charts'
import PortfolioHeader from '../components/PortfolioHeader'
import PortfolioTable from '../components/PortfolioTable'
import portfolioService from '../services/mock/portfolio.service'

const options = {
  timeScale: {
    tickMarkFormatter: (time) => {
      const date = new Date(time.year, time.month, time.day)
      const formattedTick = date.getFullYear() + '/' + (date.getMonth() + 1) + '/' + date.getDate()
      console.log({ formattedTick })
      return formattedTick
    },
  },
}

const Portfolio = () => {
  const [portfolio, setPortfolio] = useState({})
  const [currencies, setCurrencies] = useState([])
  const [portfolioHistoricalData, setPortfolioHistoricalData] = useState([])

  const lineSeries = [
    {
      data: portfolioHistoricalData,
      options: {
        title: 'Portfolio Value',
      },
    },
  ]

  useEffect(() => {
    const { currencies, portfolio, portfolioHistoricalData } = portfolioService.getPortfolioById(2)
    setPortfolioHistoricalData(portfolioHistoricalData)
    setCurrencies(currencies)
    setPortfolio(portfolio)
  }, [])

  return (
    <div>
      <Container>
        <h1>Portfolio</h1>
        <PortfolioHeader portfolio={portfolio} />
        <div style={{ marginTop: '50px' }}>
          <PortfolioTable currencies={currencies} />

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
