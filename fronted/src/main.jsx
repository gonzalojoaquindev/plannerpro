import * as React from "react";
import * as ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import "./index.css";
import Root from "./routes/root";
import ErrorPage from "./components/error-page";
import Contact from "./routes/contact";
import Clients from "./routes/clients";
import Signal from "./routes/signal";
import Pruebas from "./routes/pruebas";
import Mesh from "./routes/mesh";
import Monitor from "./routes/monitor";
import Map from "./routes/map";
import ClientsInventory from "./routes/clients_inventory";
import ApsInventory from "./routes/aps_inventory";




const router = createBrowserRouter([
  {
    path: "/",
    //establesco <root> como ruta raíz
    element: <Root />,
    //establesco el <ErrorPage> como el elemento en caso de errores de la ruta raiz
    errorElement: <ErrorPage />,
    children: [
      {
        path: "monitor-mesh",
        element: <Monitor />
      },
      {
        path: "signal",
        element: <Signal />
      },
      {
        path: "contacts/:contactId",
        element: <Contact />,
      },
      {
        path: "clients",
        element: <Clients />
      },
      {
        path: "map",
        element: <Map />
      },
      {
        path: "pruebas",
        element: <Pruebas />
      },
      {
        path: "mesh-tree",
        element: <Mesh />
      },
      {
        path: "clients_inventory",
        element: <ClientsInventory />
      },
      {
        path: "aps_inventory",
        element: <ApsInventory />
      },


    ]
  }
]);


ReactDOM.createRoot(document.getElementById("root")).render(
  /*   <React.StrictMode> */
  <RouterProvider router={router} />
  /*   </React.StrictMode> */

);
