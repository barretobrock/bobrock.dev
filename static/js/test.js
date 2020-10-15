import Footer from "./components/TestComponent";
import React from "react";
import ReactDOM from "react-dom";

const SomePage = () => {
    return <Footer />;
};

ReactDOM.render(<SomePage />, document.getElementById("content"));
