import React, {Component} from "react";
import "../styles/Graph.css"
import SimpleLineChart from "./SimpleLineChart";

import ShowChartIcon from '@mui/icons-material/ShowChart';


function Graph (props) {
    // const {data} = props;
    // console.log(props.graph);
        return (
            <main className="graph-box">
                <div className="header">
                <div className="title-1">
                    <ShowChartIcon className='icon' sx={{ fontSize: 24 }} />
                    <p className='text-1'>{props.text}</p>
                </div>
            </div>
                <div className="graph-con">
                    {/* <SimpleLineChart /> */}
                    <SimpleLineChart data={props.data} graph={props.graph}/>
                </div>
            </main>
        )
    
}

export default Graph;