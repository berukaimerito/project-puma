import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  stages: [
    { duration: '2m', target: 400 }, // ramp up to 400 users
    { duration: '3h56m', target: 400 }, // stay at 400 for ~4 hours
    { duration: '2m', target: 0 }, // scale down. (optional)
  ],
};

const API_BASE_URL = 'http://127.0.0.1:5000';

export default () => {

    http.batch([
      ['GET', `${API_BASE_URL}/homepage/`],
//      ['GET', `${API_BASE_URL}/login/`],
//      ['GET', `${API_BASE_URL}/register/`],
//      ['GET', `${API_BASE_URL}/scripts/`],
//      ['GET', `${API_BASE_URL}/dashboard/`],
//      ['GET', `${API_BASE_URL}/scripts/<symbol>/`],
//      ['GET', `${API_BASE_URL}/currencies/`],
    ]);

    sleep(1);
};
