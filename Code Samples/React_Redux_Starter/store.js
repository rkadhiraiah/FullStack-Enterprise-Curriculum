import { configureStore, createSlice } from '@reduxjs/toolkit';

// 1. Create a Slice (State + Reducers + Actions)
const authSlice = createSlice({
  name: 'auth',
  initialState: { isAuthenticated: false, user: null },
  reducers: {
    loginSuccess: (state, action) => {
      // RTK uses Immer under the hood, allowing "mutating" syntax
      state.isAuthenticated = true;
      state.user = action.payload;
    },
    logout: (state) => {
      state.isAuthenticated = false;
      state.user = null;
    },
  },
});

export const { loginSuccess, logout } = authSlice.actions;

// 2. Configure the Global Store
export const store = configureStore({
  reducer: {
    auth: authSlice.reducer,
  },
  // RTK automatically adds Redux Thunk middleware here
});

export default store;
