import api from './api';
import type { ProductInfo } from '../types';

export const getProdcutInfo = async (): Promise<ProductInfo[]> => {
    const response = await api.get<ProductInfo[]>('/products/');
    return response.data;
};

// export const createOrder = async (orderData: any): Promise<Order> => {
//     const response = await api.post<Order>('/products/', orderData);
//     return response.data;
// };