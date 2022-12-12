import http from 'k6/http';
import { check, group, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '5m', target: 100 }, // simulate ramp-up of traffic from 1 to 100 users over 5 minutes.
    { duration: '10m', target: 100 }, // stay at 100 users for 10 minutes
    { duration: '5m', target: 0 }, // ramp-down to 0 users
  ],
  thresholds: {
    'http_req_duration': ['p(99)<150'], // 99% of requests must complete below 1.5s
  },
};

export default () => {

    let response = http.get('http://127.0.0.1:5000/homepage');
//    let response = http.get('http://127.0.0.1:5000/login');
//    let response = http.get('http://127.0.0.1:5000/register');
//    let response = http.get('http://127.0.0.1:5000/scripts');
//    let response = http.get('http://127.0.0.1:5000/dashboard');
//    let response = http.get('http://127.0.0.1:5000/scripts/<symbol>');
//    let response = http.get('http://127.0.0.1:5000/currencies');

    sleep(1);

};
