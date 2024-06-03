import React, { useRef, useState } from 'react'
import MyComponent from '../components/Crud';


import { DxfViewer } from "dxf-viewer"
/* import DxfViewerWorker from "worker-loader!./DxfViewerWorker" */



const Pruebas = () => {
    const canvasContainer = useRef()
    const [dxf, setDxf] = useState(null);

    function option() {
        return (
            {
                clearColor: new three.Color("#fff"),
                autoResize: true,
                colorCorrection: true,
                sceneOptions: {
                    wireframeMesh: true
                }

            })
    }

    //* *  */ const dxfViewer = new DxfViewer(canvasContainer) */

    const loadDxf = () => {
        fetch("evac_tron_23_01_2024.dxf").then((response) => {
            response.blob().then((blob) => {
                setDxf(blob);
            });
        });
    }

    return (
        <>
            {/* <iframe src="https://www.google.com/maps/d/embed?mid=1F8DluKXCT8mSJkea1kTg28_KHElYx7I&ehbc=2E312F" width="1200" height="800"></iframe>
            

 */}

            <div>
                <button onClick={loadDxf}>Cargar archivo DXF</button>
                {dxf && <DxfViewer dxf={dxf} />}
                <div class="canvasContainer" ref={canvasContainer}></div>

            </div>

            no se
        </>
    )
}

export default Pruebas;

