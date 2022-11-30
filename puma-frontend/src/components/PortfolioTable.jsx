import Table from 'react-bootstrap/Table';

function PortfolioTable() {
  return (
    <Table bordered hover>
      <thead>
        <tr>
          <th>Currency</th>
          <th>Price</th>
          <th>24hr</th>
          <th>Holdings</th>
          <th>Avg.Buy Price</th>
          <th>Profit/Loss</th>
        </tr>
      </thead>
      <tbody>
        <tr>
            <th>BTC</th>
            <th>$30000</th>
            <th>+2.46%</th>
            <th>$2000</th>
            <th>$40000</th>
            <th>+3.49%</th>
        </tr>
        <tr>
            <th>ETH</th>
            <th>$30000</th>
            <th>+2.46%</th>
            <th>$2000</th>
            <th>$40000</th>
            <th>+3.49%</th>
        </tr>
      </tbody>
    </Table>
  );
}

export default PortfolioTable;