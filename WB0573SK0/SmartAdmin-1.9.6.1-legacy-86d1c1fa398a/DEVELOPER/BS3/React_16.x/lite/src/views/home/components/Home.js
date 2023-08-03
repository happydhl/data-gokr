import React from "react";

import { BigBreadcrumbs, WidgetGrid, JarvisWidget } from "../../../common";

export default class Home extends React.Component {
  onClick = e => {
    e.preventDefault();
  };
  render() {
    return (
      <div id="content">
        <div className="row">
          <BigBreadcrumbs
            items={["Home"]}
            icon="fa fa-home"
            className="col-xs-12 col-sm-7 col-md-7 col-lg-4"
          />
        </div>

        <WidgetGrid>
          <div className="row">
            <article className="col-sm-12 col-md-12 col-lg-12">
              <JarvisWidget id="wid-id-0">
                <header>
                  <h2> Widget Title</h2>
                </header>

                <div>
                  <div className="widget-body">
                    <h1>
                      SmartAdmin React <i>lite</i>
                    </h1>
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                      Aspernatur beatae corporis dignissimos doloremque eaque
                      eum modi, quia reprehenderit unde voluptatem.
                    </p>
                  </div>
                </div>
              </JarvisWidget>
            </article>
          </div>
        </WidgetGrid>
      </div>
    );
  }
}
