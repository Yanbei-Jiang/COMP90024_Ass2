import React, {useState,useEffect} from "react";
import KMaps from "../components/KeplerMap"
import MultiCharts from "../components/MultiCharts";
import MainPage from "../components/MainPage";
import axios from "../common/axios";
import {Sidenav, Nav, Dropdown,Container, Content, Sidebar} from 'rsuite';
import {Dashboard, AdvancedAnalytics, UserBadge } from '@rsuite/icons';
import "rsuite/dist/rsuite.min.css";

export default function HomePage() {
    const [dataType, setDataType] = useState("")
    const [aurin,setAurin] = useState()
    const [tweets,setTweets] = useState()
    useEffect(()=>{
        axios.get("/data/get_aurin").then(response=>{
            if(response.data.status===200){
                console.log(response.data)
                setAurin(response.data)
            }
        })
        axios.get("/data/get_tweets").then(response=>{
            if(response.data.status===200){
                console.log(response.data)
                setTweets(response.data)
            }
        })
    },[])
    console.log(tweets)
    return(
        <div>
            <Container>
                <Sidebar>
                    <Sidenav defaultOpenKeys={["3"]} activeKey="1">
                        <Sidenav.Body>
                        <Nav>
                            <Nav.Item eventKey="1" icon={<UserBadge/>} onClick = {()=>setDataType("Home")}>
                                HomePage
                            </Nav.Item>
                            <Nav.Item eventKey="2" icon={<Dashboard/>} onClick = {()=>setDataType("Kepler")}>
                                Kepler Map
                            </Nav.Item>
                            <Dropdown eventKey="3" title="Data Sets"  icon={<AdvancedAnalytics/>}>
                                <Dropdown.Item eventKey="3-1" onClick={()=>setDataType("Aurin")}>AURIN</Dropdown.Item >
                                <Dropdown.Item eventKey="3-2" onClick={()=>setDataType("Tweets")}>Tweets</Dropdown.Item>
                            </Dropdown>
                            <Nav.Item></Nav.Item>
                        </Nav>
                        </Sidenav.Body>
                    </Sidenav>
                </Sidebar>

                <Container>
                    <Content >
                        {dataType === ""? (<MainPage/>) : null}
                        {dataType === "Home"? (<MainPage/>) : null}
                        {dataType === "Kepler"  ? (<KMaps data={tweets}/>) : null}
                        {dataType === "Aurin" ? (<MultiCharts type={"aurin"} data={aurin}/>) : null}
                        {dataType === "Tweets" ? (<MultiCharts type={"tweet"} data={tweets}/>) : null}
                    </Content>
                </Container>
            </Container>
        </div>
    )
}