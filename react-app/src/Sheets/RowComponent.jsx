import React, { Component } from 'react';
import { Form, Button } from 'react-bootstrap';

class RowComponent extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            fields: this.props.fields
        }
    }
    
    elementCounter = 0;

    getUniqueIndex () {
        this.elementCounter += 1
        return this.elementCounter
    }

    updateRow(event) {
        let fields = {...this.state.fields}
        fields.name = event.target.value
        this.setState({fields: fields});
    }

    renderCell(value) {
        return <td key={this.getUniqueIndex()}>{value}</td> 
    }

    renderPropCell(column) {        
        return this.renderCell(<Form.Control size="sm" value={this.state.fields[column.rowField]} onChange={this.updateRow.bind(this)}/>);
    }
    
    render() {
        return ([ 
            this.renderCell(this.props.index),
            this.props.columns.filter(
                column => column.rowField
            ).map((column) => {
                return this.renderPropCell(column)
            }),
            this.renderCell(<Button size="sm">DEL</Button>)
        ])
    }
}
export default RowComponent;