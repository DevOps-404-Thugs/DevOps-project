import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import renderer from 'react-test-renderer';
import Register from './Register';


describe('Register component', () =>{
    test("match the snapshot", () =>{
        const component = renderer.create(
            <BrowserRouter>
                <Register/>
            </BrowserRouter>
        );
        let tree = component.toJSON();
        expect(tree).toMatchSnapshot();
    });  
});