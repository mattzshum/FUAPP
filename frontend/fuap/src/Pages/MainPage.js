import React, {Component} from 'react';
import styled from 'styled-components';

export default class MainPage extends Component{
    render(){
        return(
            <StyledMainPage>
                <div className='fuck-you'>
                    <h1>Fuck <br/> You</h1>
                </div>
                <div className='summary'>
                    <p>A page to express your anger at the top 20 most searched word. It's a safe place to GIVE A FUCK</p>
                </div>
            </StyledMainPage>
        )
    }
}

const StyledMainPage = styled.a`
  display:grid;
  grid-template-columns: 50% 50%;
  grid-row-gap:0;

  .fuck-you{
    grid-column-start:1;
    grid-row-start:1;
    padding-left: 10rem;

    font-size:100px;
    font-weight: 1000;
    color:#9A1750;
  }
  .summary{
      grid-column-start:2;
      grid-row-start:1;
      /* background-color:white; */

      align-items:center;
      /* text-align:center; */
      padding-top:30%;
      /* padding-bottom:50%; */

      font-size: 25px;
  }
`