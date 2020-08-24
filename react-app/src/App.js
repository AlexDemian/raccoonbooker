import React, { Component } from 'react';
import TableComponent from './Sheets/TableComponent.jsx'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container } from 'react-bootstrap';

import './App.css';
import {
  Route,
  Switch,
  Redirect,
  BrowserRouter
} from "react-router-dom"

import NavbarComponent from './Navbar/NavbarComponent';


export const siteUrls = [
  {path: '/sheets', label: 'Sheets', component: SheetsApp},
  {path: '/sheet-settings', label: 'Sheet settings', component: SheetSettingsApp},
  {path: '/account-settings', label: 'Account settings', component: SheetSettingsApp},
]

function SheetsApp() {
  
  let name = 'Sheet'

  let columns = [
    {label: '#', rowField: null},
    {label: 'Name', rowField: 'name'},
    {label: 'Description', rowField: 'description'},
    {label: 'Category', rowField: 'category'},
    {label: 'Price', rowField: 'value'},
    {label: 'Action', rowField: null}
  ]

  let rows = [
      {name: 'Fish', description: 'descr', category: 1, value: 100},
      {name: 'Garbage', description: 'descr', category: 2, value: 200}
  ]


  return <TableComponent name={name} columns={columns} rows={rows}/>
}

function SheetSettingsApp() {
  return <h1>SheetSettingsApp!</h1>
}




class App extends Component {
  
  generateRoutes() {
    return siteUrls.map((url, index) => {
      return <Route history={this.props} path={url.path} component={url.component} key={index}/>
    })
  }

  
  render() {
    return ([
      <NavbarComponent/>,
      <Container className="App">
        <BrowserRouter>
          <Switch>
            { this.generateRoutes() }
            <Redirect from='/' to={siteUrls[0].path}/>
          </Switch>
        </BrowserRouter>
      </Container>
    ]);
  }
}

export default App
