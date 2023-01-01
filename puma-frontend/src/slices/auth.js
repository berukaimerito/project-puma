import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import authService from "../services/auth.service";

const user = JSON.parse(localStorage.getItem("user"));

export const register = createAsyncThunk(
  "auth/register",
  async ({ name, surname, email, password, confirmPassword }, thunkAPI) => {
    try {
      const response = await authService.register(
        name,
        surname,
        email,
        password,
        confirmPassword
      );

      return response.data;
    } catch (error) {
      // const message = (error.response && error.response.data && error.response.data.message) || error.message || error.toString()
      return thunkAPI.rejectWithValue();
    }
  }
);

export const login = createAsyncThunk(
  "auth/login",
  async ({ email, password }, thunkAPI) => {
    try {
      const data = await authService.login(email, password);
      return { user: data };
    } catch (error) {
      return thunkAPI.rejectWithValue();
    }
  }
);

export const logout = createAsyncThunk("auth/logout", async () => {
  authService.logout();
});

const initialState = user
  ? { isLoggedIn: true, loading: false, user }
  : { isLoggedIn: false, loading: false, user: null };

const authSlice = createSlice({
  name: "auth",
  initialState,
  extraReducers: {
    [register.fulfilled]: (state, action) => {
      state.isLoggedIn = false;
      state.loading = false;
    },
    [register.rejected]: (state, action) => {
      state.isLoggedIn = false;
      state.loading = false;
    },
    [login.fulfilled]: (state, action) => {
      state.isLoggedIn = true;
      state.user = action.payload.user;
      state.loading = false;
    },
    [login.rejected]: (state, action) => {
      state.isLoggedIn = false;
      state.user = null;
      state.loading = false;
    },
    [login.pending]: (state, action) => {
      state.isLoggedIn = false;
      state.user = null;
      state.loading = true;
    },
    [logout.fulfilled]: (state, action) => {
      state.isLoggedIn = false;
      state.user = null;
      state.loading = false;
    },
  },
});

const { reducer } = authSlice;
export default reducer;
