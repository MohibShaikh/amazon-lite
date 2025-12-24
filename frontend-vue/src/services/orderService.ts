import api from './api';
import type { Order } from '../types';

export const getOrders = async (): Promise<Order[]> => {
    const response = await api.get<Order[]>('/orders/');
    return response.data;
};

export const createOrder = async (orderData: any): Promise<Order> => {
    const response = await api.post<Order>('/orders/', orderData);
    return response.data;
};