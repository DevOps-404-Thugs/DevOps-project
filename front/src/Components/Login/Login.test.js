import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import renderer from 'react-test-renderer';
import Login from './Login';

describe('Login component', () =>{
    test("match the snapshot", () =>{
        const component = renderer.create(
            <BrowserRouter>
                <Login/>
            </BrowserRouter>
        );
        let tree = component.toJSON();
        expect(tree).toMatchSnapshot();
    });  
});