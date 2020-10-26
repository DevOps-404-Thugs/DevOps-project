import React, { useEffect, useState } from 'react'

//取参参考这个代码哈
class Upload extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            id: this.props.match.params.id
        };
		}
		
    render(){
			return(
        <div>
          <p>{this.state.id}</p>
        </div>
      );
    }
}
export default Upload;