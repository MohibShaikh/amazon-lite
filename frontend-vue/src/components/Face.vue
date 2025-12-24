<script setup lang="ts">
import { ref, onMounted } from "vue";
import { getOrders } from "../services/orderService";
import type { Order } from "../types";

const title = "Order Management Dashboard";
const orders = ref<Order[]>([]);
const isLoading = ref(true);
const isVisible = ref(true);

const fetchOrders = async () => {
  try {
    orders.value = await getOrders();
  } catch (error) {
    console.error("Critical error fetching orders:", error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(fetchOrders);

// Helper function for status styling
const getStatusClass = (status: string) => {
  const s = status.toLowerCase();
  if (s === 'delivered' || s === 'completed') return 'status-success';
  if (s === 'pending') return 'status-warning';
  return 'status-default';
};
</script>

<template>
  <div class="dashboard-container">
    <header class="header">
      <h1>{{ title }}</h1>
      <button @click="isVisible = !isVisible" class="btn-toggle">
        {{ isVisible ? 'Collapse View' : 'Expand View' }}
      </button>
    </header>

    <div v-if="isLoading" class="loading-state">
      <div class="spinner"></div>
      <p>Synchronizing data...</p>
    </div>

    <div v-else-if="orders.length === 0" class="empty-state">
      <p>No active orders found.</p>
    </div>

    <transition name="fade">
      <div v-show="isVisible" class="order-grid">
        <div v-for="order in orders" :key="order.order_id" class="order-card">
          <div class="card-header">
            <span class="order-number">#{{ order.order_id.slice(0, 8) }}</span>
            <span :class="['status-badge', getStatusClass(order.status)]">
              {{ order.status }}
            </span>
          </div>

          <div class="card-body">
            <div class="data-row">
              <span class="label">Date Created</span>
              <span class="value">{{ new Date(order.created_at).toLocaleDateString() }}</span>
            </div>
            <div class="data-row total-row">
              <span class="label">Grand Total</span>
              <span class="price">${{ order.total_price }}</span>
            </div>
          </div>

          <div class="card-footer">
            <button class="btn-detail">View Full Details</button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<style scoped>
/* Modern Color Palette */
:host {
  --bg-color: #f8fafc;
  --card-bg: #ffffff;
  --primary: #2563eb;
  --text-main: #1e293b;
  --text-muted: #64748b;
  --border: #e2e8f0;
}

.dashboard-container {
  max-width: 1100px;
  margin: 2rem auto;
  padding: 0 1rem;
  font-family: 'Inter', system-ui, sans-serif;
  color: #1e293b;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 1rem;
}

.header h1 {
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: -0.025em;
}

/* Grid Layout */
.order-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

/* Professional Card Styling */
.order-card {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.order-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
}

.card-header {
  padding: 1rem;
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.order-number {
  font-weight: 600;
  color: #475569;
  font-family: monospace;
}

.card-body {
  padding: 1.25rem;
}

.data-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.75rem;
}

.label {
  color: #64748b;
  font-size: 0.875rem;
}

.total-row {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px dashed #e2e8f0;
}

.price {
  font-size: 1.25rem;
  font-weight: 800;
  color: #0f172a;
}

/* Status Badges */
.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}

.status-success { background: #dcfce7; color: #166534; }
.status-warning { background: #fef9c3; color: #854d0e; }
.status-default { background: #f1f5f9; color: #475569; }

/* Buttons */
.btn-toggle, .btn-detail {
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-toggle {
  background: white;
  border: 1px solid #cbd5e1;
}

.btn-toggle:hover { background: #f1f5f9; }

.btn-detail {
  width: 100%;
  background: #2563eb;
  color: white;
  border: none;
  margin-top: 0.5rem;
}

.btn-detail:hover { background: #1d4ed8; }

/* Transitions */
.fade-enter-active, .fade-leave-active { transition: opacity 0.3s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>