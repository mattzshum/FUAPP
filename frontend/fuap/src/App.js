//Lib Imports
import logo from './logo.svg';
import './App.css';
import styled from 'styled-components';
import {BrowserRouter, Switch, Route} from 'react-router-dom';

//Component Imports
import Nav from './Components/Nav.js';

//Page Imports
import MainPage from './Pages/MainPage.js';
import TopFuck from './Pages/TopFucks.js';

function App() {
  return (
    <GlobalStyle>
      <BrowserRouter>
      <Nav />
        <div className='page-content'>
          <Route path='/' exact component={MainPage} />
          <Route path='/top-fucks' exact component={TopFuck} />
        </div>
      </BrowserRouter>
    </GlobalStyle>
  );
}

const GlobalStyle = styled.div`
  background-color:#E3E2DF;
  min-height:100vh;
  top:0;
  height:100%;
  width:100%;

  position:relative;
`

export default App;
