import React from "react";
import { PieChart,PieArcSeries } from 'reaviz';
import chroma from "chroma-js"

export default function PieDiagram(props){

    return(
        <div>
        <PieChart
            width={700}
            height={400}
            data={props.data}
            displayAllLabels={true}
            series={<PieArcSeries colorScheme={chroma
                .scale(['pink','purple'])
                .correctLightness()
                .colors(props.data.length)}
                />}
        />
        </div>
    )
}