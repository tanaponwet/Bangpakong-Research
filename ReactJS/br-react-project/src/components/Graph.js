import React, {Component} from "react";
import "../styles/Graph.css"
import SimpleLineChart from "./SimpleLineChart";

import ShowChartIcon from '@mui/icons-material/ShowChart';

function Graph (props) {
    // const {data} = props;
        return (
            <main className="graph-box">
                <div className="header">
                <div className="title-1">
                    <ShowChartIcon className='icon' sx={{ fontSize: 24 }} />
                    <p className='text-1'>เปรียบเทียบค่าความเค็ม (g/l) ระหว่าง เครื่องวัด กับ กรมชลประทาน 24 ชม. ที่ผ่านมา</p>
                </div>
            </div>
                <div className="graph-con">
                    {/* <SimpleLineChart /> */}
                    <SimpleLineChart data={props.data}/>
                </div>
            </main>
        )
    
}

export default Graph;