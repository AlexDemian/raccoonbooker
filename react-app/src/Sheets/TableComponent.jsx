import React, { Component } from 'react';
import ColumnComponent from "./ColumnComponent";
import RowComponent from "./RowComponent";
import { Table, Button } from 'react-bootstrap';


class TableComponent extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            name: this.props.name,
            columns: this.props.columns,
            rows: this.props.rows,
        };        
    }
    
    addRow() {
        let rows = [... this.state.rows]
        rows.push({})
        this.setState({rows: rows})
    }
    
    updateRow() {}

    renderColumns () {
        return <tr>{this.state.columns.map(
            (column, index) => {
                return <ColumnComponent {...column} key={index}/>
            }
        )}</tr>
    }

    renderRows() {
        return this.state.rows.map(
            (row, index) => {
                return <tr key={index}>{<RowComponent index={index+1} columns={this.state.columns} fields={row}/>}</tr>
            }
        )
    }
    
    render() {
      return ([
        <Table size="sm">
                <caption>{this.state.name}</caption>
                <thead>
                    {this.renderColumns()}
                </thead>
                <tbody>
                    {this.renderRows()}
                </tbody>
        </Table>,
        <Button onClick={this.addRow.bind(this)}>Add row</Button>
    ]);
    }
};

TableComponent.defaultProps = {name: "New sheet"};

export default TableComponent;

