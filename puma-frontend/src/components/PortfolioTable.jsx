
import { useEffect, useState } from 'react'
import Table from 'react-bootstrap/Table'
import Chart from '@qognicafinance/react-lightweight-charts'
import io from 'socket.io-client';
import portfolioService from '../services/portfolio.service';
import Message from './Message';
import PortfolioHeader from '../components/PortfolioHeader'


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
  const [data, setData] = useState([])
  
  useEffect(() => {
    setInterval(()=> {
      portfolioService.getPortfolioById().then(data => {
        console.log(data)
        setData(data || [])
      }).catch(err=>{
        console.log(err)
      })
    }, 2000)
    
    // const newSocket = io(`http://localhost:5000`);
    // newSocket.on('data', (data) => {
    //   console.log(data)
    // })

    // newSocket.on('profits', (data) => {
    //   console.log(data)
    // })
    
    
    return () => {};
  }, []);
  
  return (
    <>
    <PortfolioHeader portfolio={data && data.length > 1 && data[0].profit} />
        <div style={{ marginTop: '50px' }}>

          <br />
          <br />
        </div>
    { data && data.length > 0? (
    <Table bordered hover>
       <thead>
        <tr>
          <th>Symbol</th>
          <th>Open price</th>
          <th>Open time</th>
          <th>Status</th>
          <th>Profit/Loss</th>
          <th>Close price</th>
          <th>Close time</th>
        </tr>
      </thead>
      <tbody>
        {data.map((curr) => {
          return (
            <>
              <tr>
                <th>{curr.symbol}</th>
                <th>{curr.buy_price}</th>
                <th>{new Date(curr.open_timestamp)}</th>
                <th>{curr.on_going}</th>
                <th>{curr.profit}</th>
                <th>{curr.close_price}</th>
                <th>{new Date(curr.close_timestamp)}</th>
              </tr>
            </>
          )
        })}
      </tbody>
      </Table>
       ) : (
        <Message variant="danger">Scripts does not have data</Message>
      )}
      {/* <Table bordered hover>
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
    </Table> */}
    </>
  )
}

export default PortfolioTable


