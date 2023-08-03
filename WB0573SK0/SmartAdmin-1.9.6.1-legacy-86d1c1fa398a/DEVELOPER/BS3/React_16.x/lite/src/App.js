import React, { Component } from "react";
import { HashRouter, Route, Switch } from "react-router-dom";
import { Provider } from "react-redux";

import store from "./store/configureStore";
import { Layout } from "./common/layout";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <HashRouter>
          <Switch>
            <Route path="/" name="Home" component={Layout} />
          </Switch>
        </HashRouter>
      </Provider>
    );
  }
}

export default App;
