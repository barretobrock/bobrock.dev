import { createStore } from "redux";
import rootReducer from '../reducers/index';

// Create store - we can later set an initial state
const store = createStore(rootReducer);

export default store;