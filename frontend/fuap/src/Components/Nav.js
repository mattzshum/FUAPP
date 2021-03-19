import React, {Component} from 'react';
import styled from 'styled-components';
import {Link} from 'react-router-dom';

export default class Nav extends Component{
    render(){
        return(
            <StyledNav>
                <div className='link-container'>
                    <ul>
                        <li className='main-page'><Link to='/'>HOME</Link></li>
                        <li className='top-fucks'><Link to='/top-fucks'>TOP FUCKS</Link></li>
                    </ul>
                </div>
            </StyledNav>
        )
    }
}

const StyledNav = styled.a`
    min-height:15vh;
    margin:auto;
    display:grid;
    grid-template-columns: 33% 17% 50%;
    text-align:center;
    background-color: #E3E2DF;
    /* color:; */
    width:100%;

    .link-container{
        grid-column-start:3;
        grid-row-start:1;
        align-items:center;
        top:50%;
        margin: 0 auto;
        a{
            color:black;
            text-decoration:none;
        }
        ul li{
            display:inline;
            text-align:center;
            font-size:20px;
            font-weight: 400;
            padding-left: 3rem;
        }
    }
`