import { useEffect, useState } from 'react'
import Table from 'react-bootstrap/Table'
import Chart from '@qognicafinance/react-lightweight-charts'
import io from 'socket.io-client';
import portfolioService from '../services/portfolio.service';


const options = {
  timeScale: {
    tickMarkFormatter: (time) => {
      const date = new Date(time.year, time.month, time.day)
      const formattedTick = date.getFullYear() + '/' + (date.getMonth() + 1) + '/' + date.getDate()
      return formattedTick
    },
  },
}

function PortfolioTable({ currencies }) {
  
  useEffect(() => {
    portfolioService.getPortfolioById().then(data => {
      console.log(data)
      console.log('2222')
    }).catch(err=>{
      console.log(err)
      console.log('err')

    })
    const newSocket = io(`wss://localhost:5000`);
    newSocket.on('data', (data) => {
      console.log(data)
    })

    newSocket.on('profits', (data) => {
      console.log(data)
    })
    
    
    return () => newSocket.close();
  }, []);
  
  return (
    <Table bordered hover>
      <thead>
        <tr>
          <th>Currency</th>
          <th>Price</th>
          <th>24hr</th>
          <th>Avg.Buy Price</th>
          <th>Profit/Loss</th>
        </tr>
      </thead>
      <tbody>
        {currencies.map((curr) => {
          const lineSeries = [
            {
              data: curr.currencyHistoricalData,
              options: {
                title: curr.name,
              },
            },
          ]
          return (
            <>
              <tr>
                <th>{curr.name}</th>
                <th>{curr.price}</th>
                <th>{curr.change24h}%</th>
                <th>${curr.avgBuyPrice}</th>
                <th>{curr.profitOrLoss}%</th>
                <th style={{ height: '50px', width: '300px' }}>
                  <Chart options={options} lineSeries={lineSeries} autoWidth height={100} />
                </th>
              </tr>
            </>
          )
        })}
      </tbody>
    </Table>
  )
}

export default PortfolioTable
