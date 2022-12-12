import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  stages: [
    { duration: '10s', target: 100 }, // below normal load
    { duration: '1m', target: 100 },
    { duration: '10s', target: 1400 }, // spike to 1400 users
    { duration: '3m', target: 1400 }, // stay at 1400 for 3 minutes
    { duration: '10s', target: 100 }, // scale down. Recovery stage.
    { duration: '3m', target: 100 },
    { duration: '10s', target: 0 },
  ],
};
export default function () {
  const BASE_URL = 'http://127.0.0.1:5000';

  const responses = http.batch([
    ['GET', `${BASE_URL}/homepage/`],
//    ['GET', `${BASE_URL}/login/`],
//    ['GET', `${BASE_URL}/register/`],
//    ['GET', `${BASE_URL}/scripts/`],
//    ['GET', `${BASE_URL}/dashboard/`],
//    ['GET', `${BASE_URL}/scripts/<symbol>/`],
//    ['GET', `${BASE_URL}/currencies/`],
  ]);

  sleep(1);
}
