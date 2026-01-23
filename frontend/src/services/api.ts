/**
 * API client for RBAT backend
 */

import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
const API_V1 = `${API_BASE_URL}/api/v1`;

const api = axios.create({
  baseURL: API_V1,
  headers: {
    'Content-Type': 'application/json',
  },
});

// AI Agent APIs
export const agentAPI = {
  query: (data: { query: string; conversation_history?: any[] }) =>
    api.post('/agent/query', data),

  recommendCrops: (data: {
    region: string;
    season?: string;
    water_availability?: string;
    budget_sar?: number;
  }) => api.post('/agent/recommend-crops', data),

  analyzeLivestock: (data: {
    region: string;
    livestock_type?: string;
    investment_amount?: number;
  }) => api.post('/agent/analyze-livestock', data),

  forecastMarket: (data: { product: string; months_ahead: number }) =>
    api.post('/agent/forecast-market', data),

  generateReport: (data: { topic: string; region?: string }) =>
    api.post('/agent/generate-report', data),

  weatherAdvisory: (data: { region: string; days_ahead: number }) =>
    api.post('/agent/weather-advisory', data),

  chat: (data: { message: string; conversation_history: any[] }) =>
    api.post('/agent/chat', data),
};

// Crops APIs
export const cropsAPI = {
  list: (params?: { skip?: number; limit?: number; category?: string; search?: string }) =>
    api.get('/crops', { params }),

  get: (id: number) => api.get(`/crops/${id}`),

  getSuitability: (id: number, region_id?: number) =>
    api.get(`/crops/${id}/suitability`, { params: { region_id } }),

  categories: () => api.get('/crops/categories/list'),
};

// Livestock APIs
export const livestockAPI = {
  list: (params?: { skip?: number; limit?: number; category?: string; search?: string }) =>
    api.get('/livestock', { params }),

  get: (id: number) => api.get(`/livestock/${id}`),

  getBreeds: (id: number) => api.get(`/livestock/${id}/breeds`),

  categories: () => api.get('/livestock/categories/list'),
};

// Fisheries APIs
export const fisheriesAPI = {
  list: (params?: { skip?: number; limit?: number; type?: string; search?: string }) =>
    api.get('/fisheries', { params }),

  get: (id: number) => api.get(`/fisheries/${id}`),

  getSpecies: (id: number) => api.get(`/fisheries/${id}/species`),

  types: () => api.get('/fisheries/types/list'),
};

// Climate APIs
export const climateAPI = {
  listRegions: (params?: { skip?: number; limit?: number }) =>
    api.get('/climate/regions', { params }),

  getRegion: (id: number) => api.get(`/climate/regions/${id}`),

  getClimateData: (params: {
    region_id: number;
    start_date?: string;
    end_date?: string;
  }) => api.get('/climate/data', { params }),

  getForecast: (params: { region_id: number; days?: number }) =>
    api.get('/climate/forecast', { params }),

  getCurrentConditions: (region_id: number) =>
    api.get(`/climate/current/${region_id}`),
};

// Reports APIs
export const reportsAPI = {
  generate: (data: {
    title: string;
    topic: string;
    region?: string;
    include_crops?: boolean;
    include_livestock?: boolean;
    include_fisheries?: boolean;
    include_climate?: boolean;
    include_market_analysis?: boolean;
    include_forecasts?: boolean;
    format?: string;
  }) => api.post('/reports/generate', data),

  templates: () => api.get('/reports/templates'),
};

export default api;
