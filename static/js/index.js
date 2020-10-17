import React from "react";
import { render } from "react-dom";
import { Provider } from 'react-redux';
import store from "./store";
import Footer from "./components/TestComponent";


render(
    <Provider store={store}>
        <Footer />
    </Provider>,
    document.getElementById('content')
)

// const SomePage = () => {
//     return <h1><h1/>;
// };

//ReactDOM.render(<h1>Hey</h1> document.getElementById("content"));
