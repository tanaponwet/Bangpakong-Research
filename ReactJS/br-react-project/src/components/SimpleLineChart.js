import React, { PureComponent } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';


export default class SimpleLineChart extends PureComponent {
  constructor(props) {
    super(props);
    this.state = { data: props.data, graph: props.graph };
  }
  
  componentDidUpdate(prevProps) {
    if (prevProps.data !== this.props.data) {
      this.setState({ data: this.props.data });
    }
  }


  render() {
    // console.log(this.state.graph);
    const lines = this.state.graph.map((line,index) => (
      <Line key={index} type={line.type} dataKey={line.dataKey} stroke={line.color} name={line.linemane} />
    ));


    return (
      <ResponsiveContainer width="100%" height="100%">
        <LineChart
          width={500}
          height={300}
          data={this.state.data}
          margin={{
            top: 5,
            right: 30,
            left: 0,
            bottom: 5,
          }}
        >
          {/* <CartesianGrid strokeDasharray="3 3" /> */}
          <XAxis dataKey={"time"} />
          <YAxis />
          <Tooltip />
          <Legend />
          {lines}
          {/* <Line type="monotone" dataKey="bangkla" stroke="#1389FF" name='ชลประทาน'/>
          <Line type="monotone" dataKey="meter" stroke="#82ca9d" name='วัดคลองเขื่อน'/> */}
        </LineChart>
      </ResponsiveContainer>
    );
  }
}
