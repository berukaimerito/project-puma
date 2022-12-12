import http from 'k6/http';
import { sleep } from 'k6'; //sleep will allow our code to wait after it's calling of the method for a each vus

export let options = {

//virtual users calling our API

    vus: 1,
    duration: '10s'

};

//default function is going to be executed during the test
//and then 'options' object will hold all the options for the test themselves

export default () => {

//function will call the endpoint to test

    http.get('http://127.0.0.1:5000/homepage');
//    http.get('http://127.0.0.1:5000/login');
//    http.get('http://127.0.0.1:5000/register');
//    http.get('http://127.0.0.1:5000/scripts');
//    http.get('http://127.0.0.1:5000/dashboard');
//    http.get('http://127.0.0.1:5000/scripts/<symbol>');
//    http.get('http://127.0.0.1:5000/currencies');

    sleep(1); // let's see how many requests per second we can handle

};
