import React, { Component } from 'react';

class ColumnComponent extends Component {
    render () {
        return <td>{this.props.label}</td>
    }
}
export default ColumnComponent;