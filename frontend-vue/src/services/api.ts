import axios from 'axios';
import type { AxiosInstance } from 'axios';

const api: AxiosInstance = axios.create({
    baseURL: 'http://localhost:8000/api' || 'http://127.0.0.1:8000/api',
    timeout: 4000,
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
});

export default api;