import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
  vus: 50, // usuários virtuais
  duration: '30s', // duração do teste
};

export default function () {
  let res = http.get('http://localhost:8000/'); // ajuste para seu endpoint
  check(res, {
    'status é 200': (r) => r.status === 200,
  });
  sleep(1);
}
