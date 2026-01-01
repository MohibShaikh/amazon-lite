import Products from "@/components/Products.vue";

export interface Product {
    id: number;
    name: string;
    price: string;
    stock: number;
}

export interface OrderItem {
    product: Product;
    quantity: number;
}

export interface Order {
    order_id: string;
    status: string;
    items: OrderItem[];
    total_price: number;
}


export interface ProductInfo {
    products : Product[];
    count : number;
    max_price : number;

}