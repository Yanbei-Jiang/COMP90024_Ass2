import React from "react";
import {BarChart, BarSeries} from "reaviz"
import chroma from "chroma-js"



export default function BarDiagram(props){
    return (
        <BarChart
            width={700}
            height={400}
            data={props.data}
            margins={22.25}
        />
    )
}