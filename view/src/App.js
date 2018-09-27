import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
class App extends Component {
    constructor(props){
        super(props);
        this.state = {
            data :[]
        };
    }
    componentDidMount () {
        axios.get('http://localhost:8000/')
          .then(response =>{
            const data =response.data;
            this.setState({data:data})

          })
}
  render() {
    return (
        <div>
          <table className="table">
            <tbody>
              <tr className="col">
                <th>Name</th>
                <th>Code</th>
                <th>Unit</th>
                <th>Forex_Selling</th>
                <th>Forex_buying</th>
               </tr>
              {this.state.data.map(i =>(
                <tr>
                  <td>{i.name}</td>
                  <td>{i.code}</td>
                  <td>{i.unit}</td>
                  <td>{i.selling}</td>
                  <td>{i.buying}</td>
                </tr>
              ))}
             </tbody>
          </table>
        </div>
    );
  }
}

export default App;
