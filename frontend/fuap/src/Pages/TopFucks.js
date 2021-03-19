import React, {Component} from 'react';
import styled from 'styled-components';
import axios from 'axios';

export default class TopFuck extends Component{
    state={
        results: {},
    }
    
    componentDidMount() {
        googleTrends.realTimeTrends({
            geo: 'US',
            category: 'all',
        }, function (err, results) {
            if(err) {
                console.log(err);
            } else {
                console.log(results);
            }
        });
    }

    render(){
        return(
            <TopFuckStyle>
                
            </TopFuckStyle>
        )
    }
}

const googleTrends = require('google-trends-api');
const TopFuckStyle = styled.a`

`